class Peep:
    def __init__(self, id, title, content, created_at, user_id):
        self.id = id
        self.title = title
        self.content = content
        self.created_at = created_at
        self.user_id = user_id
        
    # # This method allows our tests to assert that the objects it expects
    # # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"Peep({self.id}, {self.title}, {self.content}, {self.created_at}, {self.user_id})"