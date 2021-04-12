from logging import DEBUG

from wtforms.validators import Email
from myproject.forms import RegForm, loginForm
import os
from flask import render_template, redirect, flash, request
from flask.helpers import url_for
from flask_login import login_required, login_user, logout_user
from werkzeug.urls import url_decode
from myproject import app, db 
from myproject.models import User

## ! page 1
@app.route('/')
def home():
  return render_template('home.htm')

## ! page 2
@app.route('/welcome')
@login_required
def welcome():
  return render_template('welcome.htm')

## ! page 3
@app.route('/logout')
@login_required
def logout():
  logout_user()
  flash('You have been Logged-out')
  return redirect(url_for('home'))

## ! page 4
@app.route('/login', methods=['GET', 'POST'])
def login():
  form = loginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user.check_pass(password=form.password.data):
      login_user(user)
      flash('You are successfully logged-in')
      next = request.args.get('next')
      if next==None or not next[0]=='/':
        next = url_for('home')
      return redirect(next)
  return render_template('login.htm', form=form)

## ! page 5
@app.route('/reg', methods=['GET', 'POST'])
def reg():
  form = RegForm()
  if form.validate_on_submit():
    user = User(email=form.email.data,
                username=form.username.data,
                pass_hash=form.password.data)
    db.session.add(user)
    db.session.commit()
    flash('Thanks for registering')
    return redirect(url_for('login'))
  return render_template('register.htm', form=form)

if __name__ == '__main__':
  os.system('flask db migrate')
  os.system('flask db upgrade')
  app.run(debug=True)