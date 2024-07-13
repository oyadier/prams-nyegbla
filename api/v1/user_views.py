from flask import Blueprint, jsonify
from ...model.engine.storage import getUser, all_staff, instertUser
from ...model.user import User


crud_views = Blueprint('crud_views',__name__)

@crud_views.route('/a-staff/<staff_id>')
def a_staff(staff_id=None):
    '''Query db for a staff using index
        Arg:
            staff_id(integer): the index of the dictionary
        Return:
            A staff at the index
    '''
    if staff_id:
        staff = getUser(staff_id)
    return jsonify(staff)

@crud_views.route('/all-staff', strict_slashes=False)
def get_all_staff():
    '''Query db for all staff'''
    staff = all_staff()
    return jsonify(staff)

@crud_views.route('/add_user', methods=['POST'])
def add_user():
    first_name = requests.form()
    user = User()
    
    