from abc import ABC
from model.users_db.People import People


class Client(People, ABC):

    def __init__(self, id: int, full_name, age, id_no, phone_number: str, user_name="", password=""):
        self.__phone_number = str(phone_number)
        super(Client, self).__init__(id=id, full_name=full_name, age=age, id_no=id_no,
                                     user_name=user_name, password=password)

    def set_phone_number(self, phone_number):
        self.__phone_number = str(phone_number)

    def get_phone_number(self):
        return self.__phone_number
