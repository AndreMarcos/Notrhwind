from dao.order_dao import OrderDAO
from views.input_view import InputView

class OrderController:
    def __init__(self, dao):
        self.dao = dao

    def add_order(self):
        last_order_id = self.dao.get_last_order_id()
        order_details = InputView.get_order_details(last_order_id)
        self.dao.insert_order(order_details)

    def print_order_info(self, order_id):
        order_info = self.dao.get_order_info(order_id)
        print(f"ID do Pedido: {order_info[0][0]}")
        print(f"Data do Pedido: {order_info[0][1]}")
        print(f"Cliente: {order_info[0][3]}")
        print(f"Funcionário: {order_info[0][4]}")
        print(f" Preço (R$): {order_info[0][6]}")
    
    def print_order_info_sqlalchemy(self, order_id):
        order_info = self.dao.get_order_info(order_id)
        print(f"ID do Pedido: {order_info['order_id']}")
        print(f"Data do Pedido: {order_info['order_date']}")
        print(f"Cliente: {order_info['customer_name']}")
        print(f"Funcionário: {order_info['employee_name']}")
        print(f'Preço (R$): {order_info["price"]}')
    
    
    def print_employee_ranking(self, start_date, end_date):
        ranking = self.dao.get_employee_ranking(start_date, end_date)
        print("Ranking dos Funcionários:")
        for employee in ranking:
            print(f" - {employee[0]}: {employee[1]} pedidos, Total Vendido: {employee[2]}")
    
           
    def print_employee_ranking_sqlalchemy(self, start_date, end_date):
        ranking = self.dao.get_employee_ranking(start_date, end_date)
        print("Ranking dos Funcionários:")
        for employee in ranking:
            print(f" - {employee.firstname} {employee.lastname}: {employee.total_orders} pedidos, Total Vendido: {employee.total_sold}")