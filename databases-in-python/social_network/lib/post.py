class Post:
    def __init__(self, id, title, content, user_id, views):
        self.id = id
        self.title = title
        self.content = content
        self.user_id = user_id
        self.views = views
    # # This method allows our tests to assert that the objects it expects
    # # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"Post({self.id}, {self.title}, {self.content}, {self.views}, {self.user_id})"