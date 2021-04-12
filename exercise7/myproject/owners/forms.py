from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired
    
class addOwner(FlaskForm):
  name = StringField("Enter the Owner name", validators=[DataRequired()])
  kitty_id = IntegerField("Enter Kitty Id", validators=[DataRequired()])
  submit = SubmitField()