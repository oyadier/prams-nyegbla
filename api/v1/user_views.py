from typing import Dict
from flask import Blueprint, jsonify, request, url_for, flash, redirect, render_template, session
from ...model.engine.storage import getUser, all_staff, instertUser, auth, sign_up, credentials
from ...model.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from ...model.auth_credential import CredentialAuth



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
        user.surname = request.form['surname']
        user.email = request.form['email']
        user.gender = request.form['gender']
        user.mobile = request.form['mobile']
        user.reg_number = request.form['reg_number']
        user.ssf_no = request.form['ssf']
        user.bank = request.form['bank']
        user.staff_id = request.form.get('staff_id')
        user.date_of_birth = request.form.get('dob')
        user.employment_type = request.form.get('empl_type')
        user.status = request.form['status']

        instertUser(user)
    return render_template("/departments/admin/admission.html")

'''Make a querey and return the user with that staff id'''
# @crud_views.route('/auth/', methods=)
# def user_authentication():
#     if staff_id:
#         return jsonify(auth(staff_id=staff_id))
    
#     return {'None': 'No User like that'}


@crud_views.route('/authentication', methods=['GET', 'POST'])
def user_login():
    # user_auth = CredentialAuth()
    if request.method == 'POST':
        staff_id = request.form['staff_id']
        password = request.form['password']
        user =  credentials(staff_id=staff_id)
        check_pwd = check_password_hash(user.password, password=password)
        if not user or not check_pwd:
            flash('Please check your Staff Id or password correctly')
            return redirect(url_for('admin_views.sign_in_post'))
        session['user'] = user
        print(f'User data: {user}')
                # Because i am using session, i need not to pass argument to redirect
        return redirect(url_for('views.student_project_ict'))

 
@crud_views.route('/sign_up', methods=['GET','POST'])
def sign_up_post():
        '''Add new staff to the school database'''
        if request.method == 'POST':
            staff_id = request.form['staff_id']
            password = request.form['password']
            # check if password already exist on this line
            
            user =  auth(staff_id=staff_id)
            if user:
                flash('User already exits')
                return redirect(url_for('admin_views.sign_in'))
            user_auth = CredentialAuth()
            user_auth.staff_id = staff_id
            user_auth.password = generate_password_hash(password, method='sha256')
            sign_up(credential=user_auth)
            flash('New staff registered successufly')
            return redirect(url_for('admin_views.sign_in_post'))
        return redirect('admin_views.sign_up_post')
        