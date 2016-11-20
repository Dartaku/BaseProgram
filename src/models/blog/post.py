import uuid
import datetime
from src.common.database import Database
from src.models.blog.constants import *


class Post(object):
    def __init__(self, blog_id, title, content, author, created_date=datetime.datetime.utcnow(), _id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = created_date
        self._id = uuid.uuid4().hex if _id is None else _id # uuid4 = Randomise, hex generate a 32 bits

    def save_to_mongo(self):
        Database.insert(PostCollection,self.json())

    def json(self):
        return{
            '_id': self._id,
            'blog_id': self.blog_id,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'created_date': self.created_date
        }

    @classmethod
    def retrieve_post_from_post_id(cls, post_id):
        post_data = Database.find_one(PostCollection,query={'_id': post_id})
        return cls(**post_data)

    @staticmethod
    def retrieve_posts_from_blog(blog_id):
        return [post for post in Database.find(PostCollection,query={'blog_id': blog_id})]