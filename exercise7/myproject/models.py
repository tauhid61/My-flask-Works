from myproject import db
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