from abc import ABC
from model.users_db.People import People
from utils.Constants import Constants


class Librarian(People, ABC):

    def __init__(self, id: int, full_name, age, id_no, employment_type: Constants, user_name: str, password: str):
        self.__employment_type: bool = bool(employment_type)
        super(Librarian, self).__init__(id=id, full_name=full_name, age=age, id_no=id_no,
                                        user_name=user_name, password=password)

    def set_employment_type(self, employment_type):
        self.__employment_type: bool = bool(employment_type)

    def get_employment_type(self):
        return self.__employment_type
