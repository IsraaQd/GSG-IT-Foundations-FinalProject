from auth_controller.App_Auth import AppAuth
from model.Main_File import Main_File
from model.books.Book import Book
from model.books.Borrowing_Order import Borrowing_Order
from model.users_db.Client import Client
from model.users_db.Librarian import Librarian
from utils.Constants import App_Utils, Constants


def add_new_client():
    full_name = input("Enter Client Full Name: ")
    age = input("Enter Client Age: ")
    id_no = input("Enter Client ID number: ")
    phone_number = input("Enter Client Phone Number: ")
    if App_Utils.check_value_if_empty(full_name, age, id_no, phone_number):
        print("Invalid input")
        return

    client = Client(id=Main_File().get_last_client_id() + 1, full_name=full_name, age=age, id_no=id_no,
                    phone_number=phone_number)
    AppAuth().register_new_client(client)
    Main_File().get_client_list().append(client)


def add_new_book():
    title = input("Enter book title: ")
    description = input("Enter book description: ")
    author = input("Enter author name: ")
    book_status = bool(input("Enter True for Active, False for inactive book: "))
    if App_Utils.check_value_if_empty(title, description, author, book_status):
        print("Invalid input")
        return

    book = Book(book_id=Main_File().get_last_book_id() + 1, title=title, description=description, author=author,
                book_status=book_status)
    AppAuth().register_new_book(book)
    Main_File().get_book_list().append(book)


def find_user_with_id():
    user_id = input("Enter user id: ")
    if App_Utils.check_value_if_empty(user_id):
        exit()
    for users in Main_File().get_client_list():
        if user_id == str(users.get_id()):
            print("Full Name: ", users.get_full_name())
            print("Age: ", users.get_age())
            print("Phone Number: ", users.get_phone_number())
            break
    else:
        return "User not found, please try again!"


def find_book_with_id():
    book_id = input("Enter book id: ")
    if App_Utils.check_value_if_empty(book_id):
        exit()
    for books in Main_File().get_book_list():
        if book_id == str(books.get_book_id()):
            print("Book title: ", books.get_book_title())
            print("Book description: ", books.get_book_description())
            print("Book author: ", books.get_book_author())
            print("Book status: ", books.get_book_status())
            break
    else:
        return "Book not found, please try again!"


# Login
print(f"Welcome to Library Management System\n")

user_name = input("Enter Username: ")
password = input("Enter Password: ")

if App_Utils.check_value_if_empty(user_name, password):
    exit()

auth = AppAuth()

if auth.librarian_login(user_name, password) is True:
    pass
else:
    print("Invalid credentials, please try again!")
    exit()

print(f"What do you want to do?\n"
      "1: Add new client\n"
      "2: Find user using ID\n"
      "3: Add new book\n"
      "4: Find book using ID\n")

choice1 = input("Enter your choice: ")
if not App_Utils.check_value_if_empty(choice1):
    if choice1 == "1":
        add_new_client()
    if choice1 == "2":
        find_user_with_id()
    if choice1 == "3":
        add_new_book()
    if choice1 == 4:
        find_book_with_id()


else:
    print("Invalid Entry!")
    exit()
