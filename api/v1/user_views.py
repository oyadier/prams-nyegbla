from flask import Blueprint, jsonify, request, url_for, flash, redirect, render_template
from ...model.engine.storage import getUser, all_staff, instertUser
from ...model.user import User
import requests


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

@crud_views.route('/add_user', methods=['GET', 'POST'])
def add_user():
    
    if request.method == 'POST':
        user = User()
        user.firstName = request.form.get('first_name')
        user.staff_id = request.form.get('staff_id')
        user.date_of_birth = request.form.get('dob')
        user.employment_type = request.form.get('staff_type')
        instertUser(user)
    return render_template("/departments/ict/students+projects.html")
        
    
    