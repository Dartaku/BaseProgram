from flask import Flask, render_template, request, session, make_response
from flask_mail import Mail, Message

from src.common.database import Database
from src.models.blog.blog import Blog
from src.models.blog.post import Post
from src.models.users.TBD.user2 import User

__author__ = 'Dartaku'


app = Flask(__name__) #'__main__'
app.config.from_object('config')
app.secret_key='Dartaku'
app.config.update(
    DEBUG=True,
    # EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='blackcrowmiroku@gmail.com',
    MAIL_PASSWORD='Lustmeingmail2014'
)
mail = Mail(app)


@app.before_first_request
def initialize_database():
    Database.initialize()


from src.models.users.views import user_blueprint
app.register_blueprint(user_blueprint, url_prefix="/users")


@app.route('/') #www.mysite.com/api/login
def home_template():
    return render_template("fullwidthheightpagehome.html")


@app.route('/register') #www.mysite.com/api/register
def register_template():
    return render_template("register.html")


@app.route('/auth/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']
    #print(email)
    #print(password)
    if User.login_valid(email, password):
        User.login(email)
        return render_template("profile.html", email=session['email'])
    else:
        session['email'] = None
        print("User do not exists or Wrong password")
        return render_template("profile.html", email="User do not exists or wrong password")


@app.route('/auth/register', methods=['POST'])
def register_user():
    email = request.form['email']
    password = request.form['password']

    User.register(email, password)
    return render_template("profile.html", email=session['email'])


@app.route('/blogs/<string:user_id>')
@app.route('/blogs')
def user_blogs(user_id = None):
    if user_id is not None:
        user = User.get_by_id(user_id)
    else:
        user = User.get_by_email(session['email'])

    blogs = user.get_blogs()

    return render_template("user_blogs.html", email=user.email, blogs=blogs)


@app.route('/blogs/new', methods=['POST', 'GET'])
def create_new_blog():
    if request.method == 'GET':
        return render_template('new_blog.html')
    else:
        title = request.form['title']
        description = request.form['description']
        user = User.get_by_email(session['email'])

        new_blog = Blog(user.email, title, description, user._id)
        new_blog.save_to_mongo()

        return make_response(user_blogs(user._id))


@app.route('/posts/<string:blog_id>')
def blog_posts(blog_id):
    blog = Blog.from_mongo(blog_id)
    posts = blog.get_posts()

    return render_template('posts.html', posts=posts, blog_title=blog.title, blog_id=blog._id)


@app.route('/posts/new/<string:blog_id>', methods=['POST', 'GET'])
def create_new_post(blog_id):
    if request.method == 'GET':
        return render_template('new_post.html', blog_id=blog_id)
    else:
        title = request.form['title']
        content = request.form['content']
        user = User.get_by_email(session['email'])

        new_post = Post(blog_id, title, content, user._id)
        new_post.save_to_mongo()

        return make_response(blog_posts(blog_id))


@app.route('/email') #www.mysite.com/api/register
def email_template():
    return render_template("email.html")


@app.route('/email/send', methods=['POST'])
def test_send_email():
    msg = Message(
        request.form['title'],
        sender=request.form['sender'],
        recipients=[request.form['recipients']]
    )
    msg.body = request.form['email_body']

    with app.app_context():
        mail.send(msg)
        return "Sent"



