import clients

from model.users_db.Client import Client
from model.users_db.Librarian import Librarian
from model.books.Book import Book
from model.books.Borrowing_Order import Borrowing_Order
from model.Main_File import Main_File
from utils.Constants import Constants

#
#
# new_client = Client(50, "israa", 26, "0595260660", "5", "546")
# print(new_client.get_id())
# print(new_client.get_full_name())
# print(new_client.get_age())
# print(new_client.get_phone_number())
# print(new_client.get_username())
# print(new_client.get_password())
#
# new_client_two = Client(100, "afnan", 22, "05952604152", "ojlk", "lkj")
# new_client_two.set_id(9)
# new_client_two.set_full_name("selene")
# new_client_two.set_age(100)
# new_client_two.set_phone_number("0595000000")
#
# print(new_client_two.get_id())
# print(new_client_two.get_full_name())
# print(new_client_two.get_age())
# print(new_client_two.get_phone_number())
# print(new_client_two.get_username())
# print(new_client_two.get_password())
#
# new_librarian = Librarian(50, "Israa", 25, 1, "ljl", "lkjlkj")
# print(new_librarian.get_id())
# print(new_librarian.get_full_name())
# print(new_librarian.get_age())
# print(new_librarian.get_employment_type())
# print(new_librarian.get_username())
# print(new_librarian.get_password())
#
# new_librarian_two = Librarian(5, "afnan", 22, 0, "oihi", "kjhjk")
# new_librarian_two.set_age(20)
# new_librarian_two.set_id(100)
# new_librarian_two.set_full_name("IsraaQudwa")
# new_librarian_two.set_employment_type(0)
#
# print(new_librarian_two.get_id())
# print(new_librarian_two.get_full_name())
# print(new_librarian_two.get_age())
# print(new_librarian_two.get_employment_type())
# print(new_librarian_two.get_username())
# print(new_librarian_two.get_password())
#
# new_book = Book(5, "to kill a mockingjay", "description", "whats her name", True)
# print(new_book.get_book_id())
# print(new_book.get_book_title())
# print(new_book.get_book_description())
# print(new_book.get_book_author())
# print(new_book.get_book_status())
#
# new_book_two = Book(1, "title", "describ", "author name", True)
# new_book_two.set_book_id(100)
# new_book_two.set_book_title("book titles are over rated")
# new_book_two.set_book_description("described")
# new_book_two.set_book_author("no idea")
# new_book_two.set_book_status(False)
#
# print(new_book_two.get_book_id())
# print(new_book_two.get_book_title())
# print(new_book_two.get_book_description())
# print(new_book_two.get_book_author())
# print(new_book_two.get_book_status())
#
# new_order = Borrowing_Order(5, "10 oct,2022", 500, 60, "ACTIVE_ORDER")
# print(new_order.get_order_id())
# print(new_order.get_order_client_id())
# print(new_order.get_order_book_id())
# print(new_order.get_order_date())
# print(new_order.get_order_status())
#
# new_order_two = Borrowing_Order(5, "10 oct,2022", 500, 60, "ACTIVE_ORDER")
# new_order_two.set_order_id(9)
# new_order_two.set_order_client_id(70)
# new_order_two.set_order_book_id(6000)
# new_order_two.set_order_date("9 nov,2012")
# new_order_two.set_order_status("EXPIRED_ORDER")
#
# print(new_order_two.get_order_id())
# print(new_order_two.get_order_client_id())
# print(new_order_two.get_order_book_id())
# print(new_order_two.get_order_date())
# print(new_order_two.get_order_status())


# client_list = list(new_client)
# book_list = list(new_book)
# librarian_list = list(new_librarian)
# order_list = list(new_order)
#
# client_list.append(new_client_two)
# print(client_list)
#
# book_list.append(new_book_two)
# print(book_list)
#
# librarian_list.append(new_librarian_two)
# print(librarian_list)
#
# order_list.append(new_order_two)
# print(order_list)

'''
input id
for loop search in client id
for loop search in librarian id
if client list id, go to client choices
if librarian list id, go to librarian choices
if neither give error message

client id: borrow book- book list (available books), librarian list, new order
            return book- order list (of the client) for loop to search

librarian id: available book list (id ,title)
                book details (based on user choice)
                add new book
                order list
                client list
'''
'''
#registeration
print(f"Welcome, please add your username and password \n")
user_name = input("Username: ")
password = input("Password: ")
name = input("Full Name: ")
age = input("Age: ")
employment_type = input("Employment Type: ")

auth = App_Auth()
auth.register_new_librarian(Librarian(id= 1, full_name= name, age= age, employment_type= employment_type, user_name=user_name, password=password))
'''

# Main_File().find_librarian("710439")
# Main_File().find_client("5468465")
#
# Main_File().find_book_using_title("book3 title")
# Main_File().find_book_using_book_id(3)
# new_client1 = Client(50, "israa", "26", "0595260660", "5")
#
# new_book = Main_File().add_new_book(Book(3, "title", "description", "author name", Constants.ACTIVE_BOOK))
# print(Main_File().get_book_list())

