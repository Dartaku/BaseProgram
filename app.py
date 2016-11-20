from src.models.blog.post import Post
from src.models.blog.blog import Blog
from src.common.database import Database
from src.models.blog.menu import Menu
from flask import Flask

__author__ = 'Dartaku'

Database.initialize()



'''
Testing Post Function
post = Post(blog_id="123",
            title="Hello World",
            content="Hello Content",
            author="Dartaku")

post.save_to_mongo()

posts = Post.retrieve_posts_from_blog('123')

for post in posts:
    print(post)
'''



'''
Testing Blog Function
blog = Blog("Dartaku",
            "Sample Title",
            "Sample Description")

blog.new_post()

blog.save_to_mongo()

from_database = Blog.from_mongo(blog.id)

print(blog.get_posts())
'''

'''
Testing Menu Function

menu = Menu()
menu.run_menu()
'''

'''
Testing Flask Function
'''
app = Flask(__name__) #'__main__'


@app.route('/') #www.mysite.com/api/
def hello_method():
    return "Hello, world. This is my GitHub Repository App.!"

if __name__== '__main__':
    app.run(port=5000)