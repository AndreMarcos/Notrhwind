from controllers.order_controller import OrderController
from dao.order_dao import DaoSQLAlchemy

db_config = 'postgresql://user:senha@localhost:15432/northwind'

order_dao = DaoSQLAlchemy(db_config)
order_controller = OrderController(order_dao)

order_controller.add_order()