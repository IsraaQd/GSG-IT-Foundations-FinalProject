from utils.Constants import Constants


class Book:

    def __init__(self, book_id: int, title: str, description: str, author: str, book_status: Constants):
        self.__book_id: int = book_id
        self.__title = title.title()
        self.__description = description
        self.__author = author.title()
        self.__book_status = book_status

    def set_book_id(self, book_id):
        self.__book_id = book_id

    def get_book_id(self):
        return self.__book_id

    def set_book_title(self, title):
        self.__title = title

    def get_book_title(self):
        return self.__title.title()

    def set_book_description(self, description):
        self.__description = description

    def get_book_description(self):
        return self.__description

    def set_book_author(self, author):
        self.__author = author

    def get_book_author(self):
        return self.__author.title()

    def set_book_status(self, book_status):
        self.__book_status = bool(book_status)

    def get_book_status(self):
        return self.__book_status
