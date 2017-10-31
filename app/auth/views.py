from . import auth
from flask_login import login_user
from flask import render_template, redirect, url_for, request, flash
from ..models import User
from .forms import RegistrationForm, LoginForm
from .. import db


@auth.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, fullname=form.fullname.data, username=form.username.data,
                    profession=form.profession.data, quote=form.quote.data, user_pwd=form.user_pwd.data)
        db.session.add(user)
        db.session.commit()
        return render_template('auth/register.html', registration_form=form)
    title = "Bliss Account"
    return render_template('auth/register.html', registration_form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data)
        return redirect(request.args.get('next') or url_for(main.index))
        flash("Inavalid Username or Password")
    title = "Bliss Posts Login"
    return render_template('auth/login.html', title=title,  login_form=login_form)
