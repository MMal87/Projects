class User():
    def __init__(self, id, name, password, email):
        self.id = id
        self.name = name
        self.password = password
        self.email = email
    
    
    def __eq__(self, other):#allows us to compare if one instance of user is equal to another, by comparing all properties shown above
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"user({self.id}, {self.name}, {self.password}, {self.email})"