from .base_dao import BaseDAO

class OrderDAO(BaseDAO):
    def get_last_order_id(self):
        connection = self.connect()
        cursor = connection.cursor()
        query = "SELECT MAX(orderid) FROM northwind.orders"
        cursor.execute(query)
        last_order_id = cursor.fetchone()[0]
        cursor.close()
        connection.close()
        return last_order_id

    def insert_order(self, order_data):
        connection = self.connect()
        cursor = connection.cursor()
        query = """
        INSERT INTO northwind.orders (orderid, customerid, employeeid, orderdate, requireddate, shipperid, freight, shipname, shipaddress, shipcity, shipregion, shippostalcode, shipcountry)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            order_data['orderid'],
            order_data['customerid'],
            order_data['employeeid'],
            order_data['orderdate'],
            order_data['requireddate'],
            order_data['shipperid'],
            order_data['freight'],
            order_data['shipname'],
            order_data['shipaddress'],
            order_data['shipcity'],
            order_data['shipregion'],
            order_data['shippostalcode'],
            order_data['shipcountry']
        ))
        connection.commit()
        cursor.close()
        connection.close()
        
        print(f"Ordem {order_data['orderid']} adicionada com sucesso!")

    def get_order_info(self, order_id):
        connection = self.connect()
        cursor = connection.cursor()
        query = """
        SELECT o.orderid, o.orderdate, c.companyname, e.firstname || ' ' || e.lastname AS employeename, p.productname, od.quantity, od.unitprice
        FROM northwind.orders o
        JOIN northwind.customers c ON o.customerid = c.customerid
        JOIN northwind.employees e ON o.employeeid = e.employeeid
        JOIN northwind.order_details od ON o.orderid = od.orderid
        JOIN northwind.products p ON od.productid = p.productid
        WHERE o.orderid = %s
        """
        cursor.execute(query, (order_id,))
        order_info = cursor.fetchall()
        cursor.close()
        connection.close()
        return order_info

    def get_employee_ranking(self, start_date, end_date):
        connection = self.connect()
        cursor = connection.cursor()
        query = """
        SELECT e.firstname || ' ' || e.lastname AS employeename, COUNT(o.orderid) AS total_orders, SUM(o.freight) AS total_sold
        FROM northwind.orders o
        JOIN northwind.employees e ON o.employeeid = e.employeeid
        WHERE o.orderdate BETWEEN %s AND %s
        GROUP BY e.firstname, e.lastname
        ORDER BY total_sold DESC
        """
        cursor.execute(query, (start_date, end_date))
        ranking = cursor.fetchall()
        cursor.close()
        connection.close()
        return ranking

from .base_dao import BaseDAOSQLAlchemy
from sqlalchemy import func
from models.northwind_models import Order, Employee
  
class DaoSQLAlchemy(BaseDAOSQLAlchemy):
    def get_last_order_id(self):
        session = self.get_session()
        last_order_id = session.query(func.max(Order.orderid)).scalar()
        session.close()
        return last_order_id
    
    def insert_order(self, order_data):
        session = self.get_session()
        order = Order(**order_data)
        session.add(order)
        session.commit()
        order_id = order.orderid  
        session.close()
        return order_id
    
    def get_order_info(self, order_id):
        session = self.get_session()
        order = session.query(Order).filter(Order.orderid == order_id).first()
        order_info = {
            'order_id': order.orderid,
            'order_date': order.orderdate,
            'customer_name': order.customer.companyname,
            'employee_name': f'{order.employee.firstname} {order.employee.lastname}',
            'items': [{
                'product': item.product.productname,
                'quantity': item.quantity,
                'price': item.unitprice
            } for item in order.order_details]
        }
        session.close()
        return order_info
    
    def get_employee_ranking(self, start_date, end_date):
        session = self.get_session()
        ranking = session.query(
            Employee.firstname,
            Employee.lastname,
            func.count(Order.orderid).label('total_orders'),
            func.sum(Order.freight).label('total_sold')
        ).join(Order).filter(
            Order.orderdate.between(start_date, end_date)
        ).group_by(
            Employee.employeeid
        ).order_by(
            desc('total_sold')
        ).all()
        session.close()
        return ranking