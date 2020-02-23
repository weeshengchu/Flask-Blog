from flask import render_template, request, Blueprint
from flaskblog.models import Post

# 11. Blueprints and Configuration
main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    # 8. displaying post
    # 9. pagination
    # from flaskblog.models import Post -> posts = Post.query.all() -> for post in posts: -> print(post) -> dir(post) -> posts = Post.query.paginate(per_page=5, page=2)
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(
        Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route('/about')
def about():
    return render_template('about.html', title='About')
