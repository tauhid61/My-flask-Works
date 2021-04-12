from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired
class addForm(FlaskForm):
  name = StringField('Enter Puppy Name', validators=[DataRequired()])
  submit = SubmitField('Submit')

class delForm(FlaskForm):
  puppy_id = IntegerField('Enter Puppy Id', validators=[DataRequired()])
  submit = SubmitField('Submit')
