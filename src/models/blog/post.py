import uuid
import datetime
from src.common.database import Database
from src.models.blog.constants import *


class Post(object):
    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        self.id = uuid.uuid4().hex if id is None else id # uuid4 = Randomise, hex generate a 32 bits

    def save_to_mongo(self):
        Database.insert(PostCollection,self.json())

    def json(self):
        return{
            'id': self.id,
            'blog_id': self.blog_id,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'created_date': self.created_date
        }

    @classmethod
    def retrieve_post_from_post_id(cls, post_id):
        post_data = Database.find_one(PostCollection,query={'id': post_id})
        return cls(blog_id=post_data['blog_id'],
                   title = post_data['title'],
                   content = post_data['content'],
                   author = post_data['content'],
                   date = post_data['created_date'],
                   id=post_data['id'])

    @staticmethod
    def retrieve_posts_from_blog(blog_id):
        return [post for post in Database.find(PostCollection,query={'blog_id': blog_id})]