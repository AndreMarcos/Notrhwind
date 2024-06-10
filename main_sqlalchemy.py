from controllers.order_controller import OrderController
from dao.order_dao import DaoSQLAlchemy

db_config = 'postgresql://user:senha@localhost:15432/northwind'

order_dao = DaoSQLAlchemy(db_config)
order_controller = OrderController(order_dao)

order_controller.add_order()

print("Detalhes do Pedido:")
order_id = int(input("Digite o ID do Pedido para visualizar os detalhes: "))
order_controller.print_order_info(order_id)

print("Ranking dos Funcionários:")
start_date = input("Digite a data inicial (YYYY-MM-DD): ")
end_date = input("Digite a data final (YYYY-MM-DD): ")
order_controller.print_employee_ranking(start_date, end_date)