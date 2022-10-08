from typing import List

from model.books.Book import Book
from model.books.Borrowing_Order import Borrowing_Order
from model.users_db.Client import Client
from model.users_db.Librarian import Librarian
from utils.Constants import Constants


class Main_File:

    def __init__(self):
        self.__client_list: list[Client] = [
            Client(1, "israa", "26", "68478654", "0595260660"),
            Client(2, "afnan", "22", "5468465", "05952604152")
        ]
        self.__librarian_list: list[Librarian] = [
            Librarian(id=1, full_name="Israa", age="26", id_no="710410339", employment_type= Constants.FULL_TIME,user_name="israa", password="123"),
            Librarian(2, "Israa", "25", "69875465", Constants.FULL_TIME,"israa", "569"),
            Librarian(3, "afnan", "22", "48945465", Constants.PART_TIME,"afnan", "98462")
        ]
        self.__book_list: list[Book] = [
            Book(book_id=1, title="book 1 title", description="book 1 description", author="author1", book_status=Constants.ACTIVE_BOOK),
            Book(book_id=2, title="book2 title", description="book2 description", author="author1", book_status=Constants.ACTIVE_BOOK),
            Book(book_id=3, title="book3 title", description="book3 description", author="author2", book_status=Constants.INACTIVE_BOOK)
        ]
        self.__order_list: list[Borrowing_Order] = [
            Borrowing_Order(1, "8 Aug, 2021","client id" ,"book id",Constants.ACTIVE_ORDER),
            Borrowing_Order(2, "day", "client","book",Constants.EXPIRED_ORDER),
            Borrowing_Order(3, "day", "client","book",Constants.CANCELED_ORDER)
        ]
        self.__borrowed_books: list = []
        self.__available_books: list = []
        self.__borrow_orders: list = []


    def total_borrowed_books(self):
        for books in self.__book_list:
            if books.get_book_status() == Constants.INACTIVE_BOOK:
                self.__borrowed_books.append(books)
        print(len(self.__borrowed_books))

    def total_available_books(self):
        for books in self.__book_list:
            if books.get_book_status() == Constants.ACTIVE_BOOK:
                self.__available_books.append(books)
        print(len(self.__available_books))

    def total_borrowed_orders(self):
        for books in self.__order_list:
            if books.get_order_status() == Constants.ACTIVE_ORDER:
                self.__borrow_orders.append(books)
        print(len(self.__borrow_orders))

    def get_book_list(self):
        return self.__book_list

    def get_client_list(self):
        return self.__client_list

    def get_librarian_list(self):
        return self.__librarian_list

    def get_order_list(self):
        return self.__order_list

    def get_available_books(self):
        return self.__available_books

    def get_borrowed_books(self):
        return self.__borrowed_books

    def get_borrow_orders(self):
        return self.__borrow_orders

    def get_last_client_id(self) -> int:
        return self.__client_list[len(self.__client_list) - 1].get_id()

    def get_last_book_id(self) -> int:
        return self.__book_list[len(self.__book_list) - 1].get_book_id()

    def get_last_librarian_id(self) -> int:
        return self.__librarian_list[len(self.__librarian_list) - 1].get_id()

    def get_last_order_id(self) -> int:
        return self.__order_list[len(self.__order_list) - 1].get_order_id()
