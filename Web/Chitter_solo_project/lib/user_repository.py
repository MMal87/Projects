from lib.user import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all users
    def all(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
            item = User(row["id"], row["name"], row["password"], row["email"])
            users.append(item)
            
        return users
    
    def create(self, user):
        self._connection.execute('INSERT INTO users (name, password, email) VALUES (%s, %s, %s)', [
            user.name, user.password, user.email])
        return None