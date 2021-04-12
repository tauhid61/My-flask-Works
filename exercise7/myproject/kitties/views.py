from flask import render_template, redirect, url_for, Blueprint
from myproject import db
from myproject.models import Kitty, Owner
from myproject.kitties.forms import delKitty, addKitty
 
kitties_blueprint = Blueprint('kitties', __name__, template_folder='templates/kitties')

@kitties_blueprint.route('/add', methods=['GET', 'POST'])
def add():
  form = addKitty()
  if form.validate_on_submit():
    name = form.name.data
    db.session.add(Kitty(name))
    db.session.commit()
    return redirect(url_for('kitties.kitty_list'))
  return render_template('add.htm', form=form)


@kitties_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():
  form = delKitty()
  if form.validate_on_submit():
    id = form.kitty_id.data
    db.session.delete(Kitty.query.get(id))
    db.session.commit()
    return redirect(url_for('kitties.kitty_list'))
  return render_template('delete.htm', form=form)

@kitties_blueprint.route('/kitty_list')
def kitty_list():
  kitties = Kitty.query.all()
  withOwner = Kitty.query.join(Owner, Kitty.id==Owner.kitty_id)
  withoutOwner = kitties
  return render_template('kitty_list.htm', kitties=kitties, withOwner=withOwner, withoutOwner=withoutOwner)
