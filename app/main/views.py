from . import main
from flask import render_template, url_for, redirect, request
from ..models import Role, User, Category, Post, Comment
from .. import db


@main.route("/")
def index():
    title = 'Welcome to Bliss Posts'

    return render_template("index.html", title=title)
