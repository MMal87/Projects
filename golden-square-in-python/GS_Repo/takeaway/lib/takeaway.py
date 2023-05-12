from text_message import TextMessageSender


class Order():

    def __init__(self):
        self.order = []
        pass
  
    def add(self, dish_and_price):
        
        return self.order.append(dish_and_price)
    
    def view_order(self):
        
        return self.order
    
    def final_bill(self):
        total_bill = sum([float(item.split(":")[1]) for item in self.order])
        return f"{self.order}\nGrand Total: {total_bill}"
    
    def send_confirmation(self, phone_number):
        send_message = TextMessageSender(phone_number)
        return send_message.send_message()


