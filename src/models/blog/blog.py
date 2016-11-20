import datetime
import uuid
from src.models.blog.post import Post
from src.common.database import Database
from src.models.blog.constants import *

__author__ ='Dartaku'


class Blog(object):
    def __init__(self, author, title, description, id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input("Enter your post title: ")
        content = input("Enter post content: ")
        date = input("Enter post date, or leave blank for today (in format DDMMYY): ")

        if date == "":
                date = datetime.datetime.utcnow()
        else:
            date = datetime.datetime.strptime(date, "%d%m%Y")

        post = Post(blog_id=self.id,
                    title = title,
                    content = content,
                    author = self.author,
                    date=date)
        post.save_to_mongo()

    def save_to_mongo(self):
        Database.insert(BlogCollection, self.json())

    def get_posts(self):
        return Post.retrieve_posts_from_blog(self.id)

    def json(self):
        return {
            'author': self.author,
            'title': self.title,
            'description': self.description,
            'id': self.id
        }

    @classmethod
    def from_mongo(cls, id):
        blog_data = Database.find_one(BlogCollection, query ={'id': id})
        return cls(author = blog_data['author'],
                   title = blog_data['title'],
                   description = blog_data['description'],
                   id = blog_data['id'])