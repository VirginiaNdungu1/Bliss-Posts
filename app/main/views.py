from . import main
from flask import render_template, url_for, redirect, request, flash
from ..models import Role, User, Category, Post, Comment
from .. import db
from .forms import PostsForm
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


@main.route("/category/<int:id>", methods=["GET", "POST"])
@login_required
def category_posts(id):
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
    return render_template("posts.html", title=title, posts_form=posts_form, category=category)
