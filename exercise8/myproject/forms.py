from flask_login.utils import confirm_login
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from myproject.models import User

class loginForm(FlaskForm):
  email = StringField('Enter Email', validators=[DataRequired()])
  password = PasswordField('Enter Password', validators=[DataRequired()])
  submit = SubmitField('Login')
  
class RegForm(FlaskForm):
  email = StringField('Enter Email', validators=[DataRequired(), Email()])
  username = StringField('Enter Username', validators=[DataRequired()])
  password = PasswordField('Enter Password', validators=[DataRequired(), EqualTo('confirm_password', message='Passwords Must Match')])
  confirm_password = PasswordField('Enter Password Again', validators=[DataRequired()])
  submit = SubmitField('Sign-Up')
  
  def check_email(self, field):
    if User.query.filter_by(email=field.data).first():
      raise ValidationError('Email Already Exists')
  def check_username(self, field):
    if User.query.filter_by(username=field.data).first():
      raise ValidationError('Username Taken')      