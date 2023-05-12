from lib.takeaway import Order
from unittest.mock import Mock

""""When selecting a dish, it is added to the list """
order = Order()
order.add = Mock()
order.add.return_value = "Cheeseburger: 6.99"

assert order.add == "Cheeseburger: 6.99"


"""When selecting a dish, it is added to the list and vieww_order will display the current order"""



"""When selecting a dish, and then selecting final_bill, it will return a list of the dishe sekected and the cost of the final bill"""