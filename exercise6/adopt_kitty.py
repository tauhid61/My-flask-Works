# Libraries
from flask import Flask, render_template, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from form_kitty import addKitty, delKitty, addOwner 

#################################################################################################

# setting attributes
base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ex6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(base_dir, 'kittybase.db')
db = SQLAlchemy(app)
Migrate(app, db)

#################################################################################################

# creating database tables
class Kitty(db.Model):
  __tablename__ = 'kitties'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text)
  owner = db.relationship('Owner', backref='Kitty', uselist=False)

  def __init__(self, name):
    self.name = name

  # def __repr__(self):
  #   if self.owner:
  #     return f"{self.id}. {self.name}|{self.owner.name}"
  #   else:
  #     return f"{self.id}. {self.name}|No Owner"

class Owner(db.Model):
  __tablename__ = 'owners'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text)
  kitty_id = db.Column(db.Integer, db.ForeignKey('kitties.id'))

  def __init__(self, name, kitty_id):
    self.name = name
    self.kitty_id = kitty_id

#################################################################################################

# Creating routes
@app.route('/')
def index():
  return render_template('index.htm')

@app.route('/add', methods=['GET', 'POST'])
def add():
  form = addKitty()
  if form.validate_on_submit():
    name = form.name.data
    db.session.add(Kitty(name))
    db.session.commit()
    return redirect(url_for('kitty_list'))
  return render_template('add.htm', form=form)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
  form = delKitty()
  if form.validate_on_submit():
    id = form.kitty_id.data
    db.session.delete(Kitty.query.get(id))
    db.session.commit()
    return redirect(url_for('kitty_list'))
  return render_template('delete.htm', form=form)

@app.route('/owner', methods=['GET', 'POST'])
def owner():
  form = addOwner()
  if form.validate_on_submit():
    name = form.name.data
    kit_id = form.kitty_id.data
    db.session.add(Owner(name, kit_id))
    db.session.commit()
    return redirect(url_for('kitty_list'))
  return render_template('owner.htm', form=form)

@app.route('/kitty_list')
def kitty_list():
  kitties = Kitty.query.all()
  withOwner = Kitty.query.join(Owner, Kitty.id==Owner.kitty_id)
  withoutOwner = kitties
  return render_template('kitty_list.htm', kitties=kitties, withOwner=withOwner, withoutOwner=withoutOwner)
#################################################################################################

if __name__=="__main__":
  os.system('flask db migrate')
  os.system('flask db upgrade')
  app.run(debug=True)