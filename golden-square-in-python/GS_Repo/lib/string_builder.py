class StringBuilder:
    def __init__(self):
        self.str = ""
    def add(self, str):
        # ouput None as their is no return keyword 
        self.str += str
    def size(self):
        return len(self.str)
    def output(self):
        return self.str