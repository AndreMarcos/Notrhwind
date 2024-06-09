from dao.order_dao import OrderDAO
from views.input_view import InputView

class OrderController:
    def __init__(self, dao):
        self.dao = dao

    def add_order(self):
        last_order_id = self.dao.get_last_order_id()
        order_details = InputView.get_order_details(last_order_id)
        self.dao.insert_order(order_details)
