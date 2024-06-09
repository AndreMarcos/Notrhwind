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
        