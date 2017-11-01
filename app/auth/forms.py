from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Required, EqualTo, Email
from wtforms import ValidationError
from ..models import Role, User, Category, Post, Comment


class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(), Email()])
    fullname = StringField('Enter your Full Name', validators=[Required()])
    username = StringField('Enter your username', validators=[Required()])
    profession = StringField('Enter your Profession', validators=[Required()])
    quote = StringField('Life Philosophy', validators=[Required()])
    # profile_pic
    user_pwd = PasswordField('Enter Password', validators=[Required(), EqualTo(
        'user_pwd_confirm', message='Passwords Must Match')])
    user_pwd_confirm = PasswordField(
        'Confirm Password', validators=[Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self, data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError("There is an account with that email")

    def validate_user(self, data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError("That username is taken")


class LoginForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(), Email()])
    password = PasswordField('Enter Password', validators=[Required()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
