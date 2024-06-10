from controllers.order_controller import OrderController
from dao.order_dao import OrderDAO

db_config = {
    'dbname': 'northwind',
    'user': 'user',
    'password': 'senha',
    'host': 'localhost',
    'port': '15432'
}

order_dao = OrderDAO(db_config)
order_controller = OrderController(order_dao)

order_controller.add_order()