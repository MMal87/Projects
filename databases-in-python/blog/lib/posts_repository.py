from lib.posts import Posts
from lib.comments import Comments


class PostRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_with_comments(self, post_id):
        rows = self._connection.execute('SELECT posts.id, posts.title, posts.content AS post_content, comments.id AS comment_id, comments.author_name, comments.content AS comment_content, post_id FROM posts JOIN comments ON posts.id = comments.post_id WHERE posts.id = %s', [post_id])
        
        comments = []
        for row in rows:
            print(f"Position 1 {row}")
            comment = Comments(row["comment_id"], row["author_name"], row["comment_content"], row["post_id"])
            
            comments.append(comment)
            
            
            
        post = Posts(rows[0]["post_id"], rows[0]["title"], rows[0]["post_content"], comments)
        print(f"Position 2 {post}")
        return post    
