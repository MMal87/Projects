from lib.takeaway import Order
from lib.menu import Menu
from lib.text_message import TextMessageSender

import pytest

"""
When the user is shown a menu (Dishes), and multiple dishes are selected from the menu (select_dish()), and the textMessageSender class is called,
the order will be displayed with the total cost of dish, and a text message will be sent.
"""

def test_adding_multiple_items_to_order_and_viewing_order_and_recieving_message():
    menu = Menu()
    menu.show_menu()
    order = Order()
    order.add("Grilled Chicken Sandwich: 8.99")
    order.add("Caesar Salad: 6.99")
    order.add("Cheeseburger: 7.99")
    order.view_order()
    order.final_bill() == "['Grilled Chicken Sandwich: 8.99', 'Caesar Salad: 6.99', 'Cheeseburger: 7.99']\nGrand Total: 23.97"
    assert order.send_confirmation("07809720762") is not None


"""WHen entering a number of items, the final bill will be returned along with a list of items ordered"""

def test_adding_multiple_items_to_order_and_viewing_order_and_final_bill():
    menu = Menu()
    menu.show_menu()
    order = Order()
    order.add("Grilled Chicken Sandwich: 8.99")
    order.add("Caesar Salad: 6.99")
    order.add("Cheeseburger: 7.99")
    order.view_order()
    assert order.final_bill() == "['Grilled Chicken Sandwich: 8.99', 'Caesar Salad: 6.99', 'Cheeseburger: 7.99']\nGrand Total: 23.97"