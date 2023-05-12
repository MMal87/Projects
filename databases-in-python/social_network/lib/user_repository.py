from lib.user import *

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all users
    def all(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
            item = User(row["id"], row["name"], row["email"])
            users.append(item)
        return users
    
    def create(self, user):
        self._connection.execute('INSERT INTO users (name, email) VALUES (%s, %s)', [
            user.name, user.email])
        return None

    # Delete an user by their id
    def delete(self, user_id):
        self._connection.execute(
            'DELETE FROM users WHERE id = %s', [user_id])
        return None

