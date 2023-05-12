from lib.post import Post

class PostRepository:
    def __init__(self, connection):
        self._connection = connection
    def all(self):
        rows = self._connection.execute('SELECT * from posts')
        posts = []
        for row in rows:
            item = Post(row['id'], row['title'], row['content'], row['views'], row['user_id'])
            posts.append(item)
        return posts
    
    def create(self, post):
        self._connection.execute("INSERT INTO posts (id, title, content, views, user_id) VALUES (%s, %s, %s, %s, %s)", [post.id, post.title, post.content, post.views, post.user_id])
        return None
       
    def delete(self, post_id):
        self._connection.execute("DELETE from posts WHERE id = %s", [post_id])
        return None