from lib.peep import Peep

class PeepRepository:
    def __init__(self, connection):
        self._connection = connection
    def all(self):
        rows = self._connection.execute('SELECT peeps.id, peeps.title, peeps.content, peeps.created_at, user_id, users.name FROM peeps JOIN users ON peeps.user_id = users.id ORDER BY created_at DESC')
        peeps = []
        for row in rows:
            item = Peep(row['id'], row['title'], row['content'], row['created_at'], row['user_id'], row['name'])
            peeps.append(item)
        return peeps
    
    def create(self, peep):
        self._connection.execute("INSERT INTO peeps (title, content, created_at, user_id) VALUES (%s, %s, %s, %s)", [peep.title, peep.content, peep.created_at, peep.user_id])
        return None
    
    
