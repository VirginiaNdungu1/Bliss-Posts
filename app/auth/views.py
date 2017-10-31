from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import REquired, EqualTo
from ..models import Role, User, Category, Post, Comment


class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(), Email()])
    fullname = StringField('Enter your Full Name', validators=[Required()])
    username = StringField('Enter your username', validators=[Required()])
    profession = StringField('Enter your Profession', validators=[Required()])
    quote = StringField('Life Philosophy', validators=[Required()])
    profile_pic
    user_pwd = PasswordField('Enter Password', validators=[Required(), EqualTo(
        'user_pwd_confirm', message='Passwords Must Match')])
    user_pwd_confirm = PasswordField(
        'Confirm Password', validators=[Required()])
    submit = SubmitField('Sign Up')
