from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate

base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(base_dir, 'dogbase.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)

class Puppy(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.column(db.Text)
  breed = db.Column(db.Text)

  # puppy-toy one-many relationship
  toys = db.relationship('Toys', backref='Puppy', lazy='dynamic')
  # puppy-owner one-one relationship
  owner = db.relationship('Owner', backref='Puppy', uselist=False)

  def __init__(self, name, breed):
    self.name = name
    self.breed = breed
  def __repr__(self):
    if self.owner:
      return f"Puppy name is {self.name} and owner is {self.owner.name}"
    else:
      return f"Puppy name is {self.name} and has no owner assigned yet."

  def report_toys(self):
    for toy in self.toys:
      print(toy.toy_name)

class Toys(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  toy_name = db.Column(db.Text)
  puppy_id = db.Column(db.Integer, db.ForeignKey('puppy.id'))

  def __init__(self, toy_name, puppy_id):
    self.toy_name = toy_name
    self.puppy_id = puppy_id


class Owner(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text)
  puppy_id = db.Column(db.Integer, db.ForeignKey('puppy.id'))

  def __init__(self, name, puppy_id):
    self.name = name
    self.puppy_id = puppy_id

if __name__=='__main__':
  os.system('flask db migrate')
  os.system('flask db upgrade')