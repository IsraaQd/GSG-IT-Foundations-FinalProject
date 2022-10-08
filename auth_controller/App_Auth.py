from model.Main_File import Main_File
from model.books.Book import Book
from model.users_db.Client import Client
from model.users_db.Librarian import Librarian


class AppAuth:
    librarian_list: list = Main_File().get_librarian_list()
    client_list: list = Main_File().get_client_list()
    book_list: list = Main_File().get_book_list()

    def librarian_login(self, user_name: str, password: str) -> bool:
        for items in self.librarian_list:
            if items.get_user_name() == user_name and items.get_password() == password:
                return True
        return False

    def register_new_librarian(self, user_name: Librarian):
        if not self.check_user_name_duplication(user_name=user_name.get_user_name()):
            self.librarian_list.append(user_name)
        else:
            print("User already used!")

    def check_user_name_duplication(self, user_name: str):
        for item in self.librarian_list:
            if item.get_user_name() == user_name:
                return True
        return False

    def client_login(self, user_name: str, password: str) -> bool:
        for items in self.client_list:
            if items.get_user_name() == user_name and items.get_password() == password:
                return True
        return False

    def register_new_client(self, user_name: Client):
        if not self.check_user_name_duplication(user_name=user_name.get_user_name()):
            self.client_list.append(user_name)
        else:
            print("User already used!")

    def check_client_duplication(self, user_name: str):
        for item in self.client_list:
            if item.get_user_name() == user_name:
                return True
        return False

    def register_new_book(self, new_book: Book):
        if not self.check_user_name_duplication(new_book.get_book_title()):
            self.book_list.append(new_book)
        else:
            print("User already used!")

    def check_book_duplication(self, book_title):
        for item in self.book_list:
            if item.Book.get_book_title() == book_title:
                return True
        return False
