from flask import Blueprint, jsonify
from ...model.engine.storage import getUser, all_staff

crud_views = Blueprint('crud_views',__name__)

@crud_views.route('/testing')
def profile():
    return 'Hello this is the staff of pramshigh'

@crud_views.route('/a-staff/<staff_id>')
def a_staff(staff_id=None):
    if staff_id:
        staff = getUser(staff_id)
    return jsonify(staff)

@crud_views.route('/all-staff', strict_slashes=False)
def get_all_staff():
    staff = all_staff()
    return jsonify(staff)
