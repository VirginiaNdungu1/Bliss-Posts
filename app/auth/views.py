from . import auth
from flask import render_template, redirect, url_for, request
from ..models import User
from .forms import RegistrationForm
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
