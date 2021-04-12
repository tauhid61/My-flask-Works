from flask import Blueprint, render_template, redirect, url_for
from myproject import db
from myproject.models import Owner
from myproject.owners.forms import addOwner

owners_blueprint = Blueprint('owners', __name__, template_folder='templates/owners')
@owners_blueprint.route('/owner', methods=['GET', 'POST'])
def owner():
  form = addOwner()
  if form.validate_on_submit():
    name = form.name.data
    kit_id = form.kitty_id.data
    db.session.add(Owner(name, kit_id))
    db.session.commit()
    return redirect(url_for('kitties.kitty_list'))
  return render_template('owner.htm', form=form)

