from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flaskblog.posts.forms import PostForm
from flaskblog.models import Post
from flaskblog import db
from flask_login import current_user, login_required

# 11. Blueprints and Configuration
posts = Blueprint('posts', __name__)

# dummy post
# posts = [
#     {
#         'author': 'Wee Sheng',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'Feb 5, 2020'
#     },
#     {
#         'author': 'Corey Schafer',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'April 20, 2018'
#     }
# ]

# 8. CUD posts
@posts.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        # 8. Saving updated post to home page
        post = Post(title=form.title.data,
                    content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post', form=form, legend='New Post')


@posts.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@posts.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        # 8. return 403 page when /3/update
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        # 8. updating the post
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')

# 8. deleting the post
@posts.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))
