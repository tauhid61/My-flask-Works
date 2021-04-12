from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ex7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(base_dir, 'kittybase2.db')
db = SQLAlchemy(app)
Migrate(app, db)

from myproject.kitties.views import kitties_blueprint
from myproject.owners.views import owners_blueprint

app.register_blueprint(kitties_blueprint, url_prefix='/kitties')
app.register_blueprint(owners_blueprint, url_prefix='/owners')