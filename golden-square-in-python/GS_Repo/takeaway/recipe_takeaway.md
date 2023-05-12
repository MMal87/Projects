1. Describe the Problem
As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.
Use the twilio-python package to implement this next one. You will need to use mocks too.

As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.

Fair warning: if you push your Twilio API Key to a public GitHub repository, anyone will be able to see and use it. What are the security implications of that? How will you keep that information out of your repository?

2. Design the Class System
Consider diagramming out the classes and their relationships. Take care to focus on the details you see as important, not everything. The diagram below uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com

Nouns:
list of dishes with prices
dishes
receipt
text


Verbs:
order
see a list
select dishes
verify correct order
see a reciept
recieve a text


┌────────────────────────────┐
│ Order                      │
│                            │
│ -select item from Dishes   │
│ - return list of dishes    |
     selected                │
│ -  return total cost of    |
  dishes with dish names     │
│                            │
└───────────┬────────────────┘
            │
            │ owns a list of
            ▼
┌─────────────────────────┐
│ Dishes                  │
│                         │
│ - list of dishes        │
│ -                       │
│ -                       │
│                         │
└─────────────────────────┘
             owns a list of
            ▼
┌─────────────────────────┐
│ Text messages           │
│                         │
│ - twilio stuff          │
│ -                       │
│ -                       │
│                         │
└─────────────────────────┘
Also design the interface of each class in more detail.

class Order:
    # User-facing properties:
    #   dish: an instance of Dishes

    def __init__(self):
        self.order #a list of all dishes selected
        pass # No code here yet
    
    def add(self, menu):
        # Parameters:
        #   menu, an instance of Menu class
        # Side-effects:
        #   user adds a menu item to the order list
        pass # No code here yet

    def view_order(self):
        # Parameters:
        #   none
        # Returns:
        #   A list of ordered items with price
        pass # No code here yet

    def final_bill(self):
    parameters:
    none
    #Returns:
         order list


class Menu:
    # User-facing properties:
    #   dish
    price

   
    def show_menu():
        #add dishes and prices to a list


class TexMessageSender():
    #User facing properties:
    phone number
    #allows a message to be sent to confirm order to the user: "Thank you! Your order was placed and will be delivered before 18:52"


3. Create Examples as Integration Tests
Create examples of the classes being used together in different situations and combinations that reflect the ways in which the system will be used.

# EXAMPLE

"""
When the user is shown a menu (Dishes), and multiple dishes are selected from the menu (select_dish()), and the textMessageSender class is called,
the order will be displayed with the total cost of dish, and a text message will be sent.
"""
Menu:
Grilled Chicken Sandwich - $8.99
Caesar Salad - $6.99
Cheeseburger - $7.99
French Fries - $3.99

menu = Menu()
menu.show_menu()
order = Order()
dish_1 = order.add("Grilled Chicken Sandwich", 8.99)
dish_2 = order.add("Caesar Salad", 6.99)
dish_3 = order.add("Cheeseburger", 7.99)
order.view_order()
order.final_bill()
send_message = TextMessageSender("07834763544")


# EXAMPLE

"""
When user is shown menu, they can add an item to their order
"""
menu = Menu()
menu.show_menu()
order = Order()
dish_1 = order.add("Grilled Chicken Sandwich", 8.99)
order.view_order()
assert order.final_bill == "8.99"


"""

"""
menu = Menu()
menu.show_menu()
order = Order()
dish_1 = order.add("Grilled Chicken Sandwich", 8.99)
dish_2 = order.add("Caesar Salad", 6.99)
dish_3 = order.add("Cheeseburger", 7.99)
order.view_order()
assert order.final_bill() == 23.97

Unit tests
"""
given 1 dish, it is added to the list
"""

order = Order()
dish_1 = order.add("Grilled Chicken Sandwich", 8.99)
assert order.view_order() == "Grilled Chicken Sandwich", 8.99


"""
Given a mock dish, we can test each element of the order class

