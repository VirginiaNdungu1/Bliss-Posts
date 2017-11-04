from . import main
from flask import render_template, url_for, redirect, request, flash
from ..models import Role, User, Category, Post, Comment
from .. import db
from .forms import PostsForm, CommentsForm
from flask_login import login_required, current_user


@main.route("/")
def index():
    title = 'Welcome to Bliss Posts'
    return render_template("index.html", title=title)


@main.route("/category")
def category():
    # get categories

    all_categories = Category.get_category()
    print(all_categories)

    title = "Bliss Posts..."
    return render_template("category.html", title=title, all_categories=all_categories)


@main.route("/category/newpost/<int:id>", methods=["GET", "POST"])
@login_required
def new_posts(id):
    posts_form = PostsForm()

    # filter category by id
    category = Category.query.filter_by(id=id).first()

    if posts_form.validate_on_submit():
        title = posts_form.title.data
        description = posts_form.description.data

        # instance of Post
        post = Post(category_id=category.id, title=title,
                    description=description, user=current_user)

        post.save_post()
        flash("Successfull Upload")
        return redirect(request.args.get('next') or url_for('main.category_posts', id=category.id))

    title = "More Bliss Posts...."
    return render_template("new_post.html", title=title, posts_form=posts_form, category=category)


@main.route('/category/<int:id>')
@login_required
def category_posts(id):
    category = Category.query.get(id)

    if category is None:
        return "Section Not Found"
    posts = Post.get_post(id)

    return render_template("posts.html", category=category, posts=posts)


@main.route('/category/newcomment/<int:id>', methods=["GET", "POST"])
@login_required
def new_comment(id):
    comment_form = CommentsForm()

    # filter post by id
    post = Post.query.filter_by(id=id).first()

    if comment_form.validate_on_submit():
        comment_description = comment_form.comment_description.data

        # instance of comment
        comment = Comment(
            posts_id=post.id, comment_description=comment_description, user=current_user)
        comment.save_comment()
        return redirect(url_for('main.post_comments', id=post.id))
    return render_template('new_comment.html', comment_form=comment_form)


@main.route('/category/post/<int:id>', methods=["GET", "POST"])
@login_required
def post_comments(id):
    post = Post.query.get(id)

    if post is None:
        abort(404)
    comments = Comment.get_comment(id)

    return render_template("comments.html", post=post, comments=comments)
