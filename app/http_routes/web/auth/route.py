from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.models.user import User

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email

import re

auth = Blueprint('auth', __name__)

class LoginForm(FlaskForm):
    email = StringField('Username or Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        email_or_username = request.form['email']
        password = request.form['password']
        
        if re.match(r"[^@]+@[^@]+\.[^@]+", email_or_username): 
            user = User.query.filter_by(email=email_or_username).first()
        else:
            user = User.query.filter_by(username=email_or_username).first()
        
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('dashboard.index'))
        
        flash("Email/Username atau password salah", "danger")
    
    return render_template('pages/auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Berhasil logout", "info")
    return redirect('/')
