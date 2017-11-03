from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Required, EqualTo, Email
from wtforms import ValidationError
from ..models import Role, User, Category, Post, Comment


class PostsForm(FlaskForm):
    title = StringField('Title of Post Here...', validators=[Required()])
    description = StringField('New Message...', validators=[Required()])
    submit = SubmitField('New Post')
