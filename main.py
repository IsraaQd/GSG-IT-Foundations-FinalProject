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
        return "Invalid input"

    client = Client(id=Main_File().get_last_client_id() + 1, full_name=full_name, age=age, id_no=id_no,
                    phone_number=phone_number)
    AppAuth().register_new_client(client)


def add_new_librarian():
    full_name = input("Enter Librarian Full Name: ")
    age = input("Enter Librarian Age: ")
    id_no = input("Enter Librarian ID number: ")
    employment_type = bool(input("Enter True for full-time, False for part-time: ").title())
    if App_Utils.check_value_if_empty(full_name, age, id_no):
        print("Invalid input")
        return

    librarian = Librarian(id=Main_File().get_last_librarian_id() + 1, full_name=full_name, age=age, id_no=id_no,
                          employment_type=Constants.FULL_TIME or Constants.PART_TIME, user_name="", password="")
    AppAuth().register_new_librarian(librarian)


def add_new_book():
    title = input("Enter book title: ")
    description = input("Enter book description: ")
    author = input("Enter author name: ")
    if App_Utils.check_value_if_empty(title, description, author):
        print("Invalid input")
        return

    book = Book(book_id=Main_File().get_last_book_id() + 1, title=title, description=description, author=author,
                book_status=Constants.ACTIVE_BOOK)
    AppAuth().register_new_book(book)
    print(len(Main_File().get_book_list()))


def add_new_order():
    date = input("Enter date: ")
    client_id = int(input("Enter client id: "))
    book_id = int(input("Enter book id: "))
    if App_Utils.check_value_if_empty(date):
        print("Invalid input")
        return

    order = Borrowing_Order(order_id=Main_File().get_last_order_id() + 1, date=date, client_id=client_id,
                            book_id=book_id, order_status=Constants.ACTIVE_ORDER)
    for books in Main_File().total_available_books():
        if book_id == books.get_book_id:
            AppAuth().register_new_order(order)
            break
    else:
        return "Book not available! please choose another book!"


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


def find_librarian_with_id():
    librarian_id = input("Enter librarian id: ")
    if App_Utils.check_value_if_empty(librarian_id):
        exit()
    for librarians in Main_File().get_librarian_list():
        if librarian_id == str(librarians.get_id()):
            print("Full Name: ", librarians.get_full_name())
            print("Age: ", librarians.get_age())
            print("ID Number: ", librarians.get_id_no())
            print("Employment type: ", librarians.get_employment_type())
            break
    else:
        return "Librarian not found, please try again!"


def find_order_with_id():
    order_id = input("Enter order id: ")
    if App_Utils.check_value_if_empty(order_id):
        exit()
    for orders in Main_File().get_order_list():
        if order_id == str(orders.get_id()):
            print("Book ID: ", orders.get_order_book_id())
            print("Client ID: ", orders.get_order_client_id())
            print("Date: ", orders.get_order_date())
            print("Order Status: ", orders.get_order_status())
            break
    else:
        return "Order not found, please try again!"


def return_borrowed_book():
    order_id = input("Enter order ID: ")
    for orders in Main_File().get_order_list():
        if order_id == str(orders.get_order_id()):
            if orders.get_order_status() == Constants.ACTIVE_ORDER:
                orders.set_order_status(Constants.EXPIRED_ORDER)
            else:
                return "No Active order with this ID number"
        break
    else:
        return "Order not found, please try again!"



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
      "4: Find book using ID\n"
      "5: Add new librarian\n"
      "6: Find librarian using ID\n"
      "7: Add new Borrowing Order\n"
      "8: Return a borrowed book")

choice1 = input("Enter your choice: ")
if not App_Utils.check_value_if_empty(choice1):
    if choice1 == "1":
        add_new_client()
    if choice1 == "2":
        find_user_with_id()
    if choice1 == "3":
        add_new_book()
    if choice1 == "4":
        find_book_with_id()
    if choice1 == "5":
        add_new_librarian()
    if choice1 == "6":
        find_librarian_with_id()
    if choice1 == "7":
        add_new_order()
    if choice1 == "8":
        return_borrowed_book()

else:
    print("Invalid Entry!")
    exit()
