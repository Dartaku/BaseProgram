import datetime
import uuid
from src.models.blog.post import Post
from src.common.database import Database
from src.models.blog.constants import *

__author__ ='Dartaku'

class Blog(object):
    def __init__(self, author, title, description, author_id, _id=None):
        self.author = author
        self.author_id = author_id
        self.title = title
        self.description = description
        self._id = uuid.uuid4().hex if _id is None else _id

    def new_post(self, title, content, date=datetime.datetime.utcnow()):
        post = Post(blog_id=self._id,
                    title = title,
                    content = content,
                    author = self.author,
                    created_date=date)
        post.save_to_mongo()

    def save_to_mongo(self):
        Database.insert(BlogCollection, self.json())

    def get_posts(self):
        return Post.retrieve_posts_from_blog(self._id)

    def json(self):
        return {
            'author': self.author,
            'author_id': self.author_id,
            'title': self.title,
            'description': self.description,
            '_id': self._id
        }

    @classmethod
    def from_mongo(cls, id):
        blog_data = Database.find_one(BlogCollection,
                                      query={'_id': id})
        return cls(**blog_data)

    @classmethod
    def find_by_author_id(cls, author_id):
        blogs = Database.find(BlogCollection,
                              query={'author_id': author_id})
        return [cls(**blog) for blog in blogs]