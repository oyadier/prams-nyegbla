from typing import Dict
from flask import Blueprint, jsonify, request, url_for, flash, redirect, session

from ...model.engine.storage import getUser, all_staff, instertUser, user_bio_data, sign_up, credentials
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
        staff = user_bio_data(staff_id)
    return jsonify(staff)

@crud_views.route('/all-staff', strict_slashes=False)
def get_all_staff():
    '''Query db for all staff'''
    staff = all_staff()
    return jsonify(staff)

@crud_views.route('/add_user', methods=['GET', 'POST'])
def add_user():
    '''Add new user's bio data to school database'''
    if request.method == 'POST':     
        data = User()
        staffId = session.get('user')
        if staffId:
            staff_id = staffId['staff_id']
            data.staff_id = staff_id
            print(staff_id)
            data.credential_fk = staff_id
        else:
            data.staff_id = request.form.get('staff_idd')
            data.credential_fk = request.form.get('staff_id')

        data.firstName = request.form.get('first_name')
        data.surname = request.form['surname']
        data.email = request.form['email']
        data.gender = request.form['gender']
        data.mobile = request.form['mobile']
        data.reg_number = request.form['reg_number']
        data.ssf_no = request.form['ssf']
        data.bank = request.form['bank']
        data.date_of_birth = request.form.get('dob')
        data.employment_type = request.form.get('empl_type')
        data.status = request.form['status']
        instertUser(data)
        flash('Profile updated', 'info')
    return redirect(url_for('admin_views.staff_profile'))


@crud_views.route('/authentication', methods=['POST'])
def user_login():
    # user_auth = CredentialAuth()
    if request.method == 'POST':
        staff_id = request.form['staff_id']
        password = request.form['password']
        user =  credentials(staff_id=staff_id)
        if not user:
            flash("User does not exit", category='error')
            return redirect(url_for('admin_views.sign_in_post'))

        check_pwd = check_password_hash(pwhash=user['password'], password=password)
        if not check_pwd:
            flash('Please check your password again', category='error')
            return redirect(url_for('admin_views.sign_in_post'))
        session['data'] = user_bio_data(staff_id=staff_id)
        return redirect(url_for('admin_views.staff_profile'))

 
@crud_views.route('/sign_up', methods=['GET','POST'])
def sign_up_post():
        '''Add new staff to the school database'''
        if request.method == 'POST':
            staff_id = request.form['staff_id']
            password = request.form['password']
            # check if password already exist on this line
            
            user =  credentials(staff_id=staff_id)
            if user:
                flash('User already exits', category='warning')
                return redirect(url_for('admin_views.sign_in_post'))
            user_auth = CredentialAuth()
            user_auth.staff_id = staff_id
            user_auth.password = generate_password_hash(password, method='sha256')
            sign_up(credential=user_auth)
            flash('New staff registered successufly', category='info')
            return redirect(url_for('admin_views.sign_in_post'))
        return redirect('admin_views.sign_up_post')

