import datetime

from utils.Constants import Constants


class Borrowing_Order:
    def __init__(self, order_id: int, date, client_id: int, book_id: int, order_status: Constants):
        self.__order_id: int = order_id
        self.__date = date
        self.__client_id: int = client_id
        self.__book_id: int = book_id
        self.__order_status = order_status

    def set_order_id(self, order_id):
        self.__order_id = order_id

    def get_order_id(self):
        return self.__order_id

    def set_order_date(self, date):
        self.__date = date

    def get_order_date(self):
        return self.__date

    def set_order_client_id(self, client_id):
        self.__client_id = client_id

    def get_order_client_id(self):
        return self.__client_id

    def set_order_book_id(self, book_id):
        self.__book_id = book_id

    def get_order_book_id(self):
        return self.__book_id

    def set_order_status(self, order_status):
        self.__order_status = order_status

    def get_order_status(self):
        return self.__order_status
