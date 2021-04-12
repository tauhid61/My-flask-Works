from myproject import db, login_manager
from flask_login import UserMixin
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(64), unique=True, index=True)
  username = db.Column(db.String(64), unique=True, index=True)
  pass_hash = db.Column(db.String(128)) 
  
  def __init__(self, email, username, pass_hash):
    self.email = email
    self.username = username
    self.pass_hash = bcrypt.generate_password_hash(pass_hash)
    
  def check_pass(self, password):
    return bcrypt.check_password_hash(self.pass_hash, password)
  