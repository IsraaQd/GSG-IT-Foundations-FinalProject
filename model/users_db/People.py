import abc


class People:
    def __init__(self, id: int, full_name: str, age: str, id_no: str, user_name: str, password: str):
        self.__id: int = id
        self.__full_name = full_name.title()
        self.__age = age
        self.__id_no = id_no
        self.__user_name = user_name
        self.__password = password

    @abc.abstractmethod
    def set_id(self, id):
        self.__id = id

    @abc.abstractmethod
    def get_id(self):
        return self.__id

    @abc.abstractmethod
    def set_full_name(self, full_name):
        self.__full_name = full_name.title()

    @abc.abstractmethod
    def get_full_name(self):
        return self.__full_name

    @abc.abstractmethod
    def set_age(self, age):
        self.__age = age

    @abc.abstractmethod
    def get_age(self):
        return self.__age

    @abc.abstractmethod
    def set_id_no(self, id_no):
        self.__id_no = id_no

    @abc.abstractmethod
    def get_id_no(self):
        return self.__id_no

    @abc.abstractmethod
    def set_user_name(self, user_name):
        self.__user_name = user_name

    @abc.abstractmethod
    def get_user_name(self):
        return self.__user_name

    @abc.abstractmethod
    def set_password(self, password):
        self.__password = password

    @abc.abstractmethod
    def get_password(self):
        return self.__password
