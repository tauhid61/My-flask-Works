from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from forms import addForm, delForm

base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'key1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(base_dir, 'adoptBase.db')
db = SQLAlchemy(app)
Migrate(app, db)

class puppy(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text)

  def __init__(self, name):
    self.name = name


@app.route('/')
def index():
  return render_template('home.htm')
  
@app.route('/database')
def database():
  puppy_db = puppy.query.all()

  return render_template('database.htm', puppy_db=puppy_db)

@app.route('/add', methods=['GET', 'POST'])
def add():
  form = addForm()
  if form.validate_on_submit():
    name = form.name.data
    db.session.add(puppy(name))
    db.session.commit()
    return redirect(url_for('database'))
  return render_template('add.htm', form=form)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
  form = delForm()
  if form.validate_on_submit():
    id = form.puppy_id.data
    db.session.delete(puppy.query.get(id))
    db.session.commit()
    return redirect (url_for('database'))
  return render_template('delete.htm', form=form)

if __name__=='__main__':
  os.system('flask db migrate')
  os.system('flask db upgrade')
  app.run(debug=True)