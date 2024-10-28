from typing import List
from flask import Blueprint, jsonify, render_template, request, url_for, flash, redirect, session

from model.engine.storage import insert_prof, all_staff, instertUser,user_bio_data, get_profs_qualificatons, sign_ups, userExists
from model.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from model.professional import Professional


crud_views = Blueprint('crud_views',__name__)
global user_fk

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
    return jsonify(staff), 200

@crud_views.route('/all-staff', strict_slashes=False)
def get_all_staff():
    '''Query db for all staff'''
    staff = all_staff()
    return jsonify(staff), 202

# @crud_views.route('/add_user', methods=['POST'])
# def add_user():
    
#     '''Add new user's bio data to school database'''
#     user = session.get('user')

#     if user:
#         user['firstName'] = request.form.get('first_name')
#         user['surname'] = request.form.get('surname')
#         user['other_name'] = request.form['other_name']
#         user['email'] = request.form['email']
#         user['gender'] = request.form['gender']
#         user['mobile'] = request.form['mobile']
#         user['ssf_no'] = request.form['ssf']
#         user['bank'] = request.form['bank']
#         user['bank_branch']= request.form['bank_branch']
#         user['date_of_birth'] = request.form.get('dob')
#         user['staff_type'] = request.form.get('staff_type')
#         print(f"New Update data: {user}")
#     if request.method == 'POST':
#             try:
#                 instertUser(user)
#                 flash('Profile updated', category='info')
#                 return redirect (url_for('admin_views.staff_profile'))
#             except Exception as e:
#                 flash(f"Failed to update: {str(e)}", category='error')
                
#     return redirect(url_for('admin_views.staff_profile'))


# '''TODO: WORKING ON UPDATE OF STAFF PROFILE'''
# @crud_views.route('user/update-profile', methods=['PUT'])      
# def update_profile():
    
#     '''Add new user's bio data to school database'''
#     data = User()
#     staff_id = session.get('user')
#     print(staff_id)
#     if staff_id:
              
#         data.staff_id = staff_id
#         data.credential_fk = staff_id
#     else:
#         data.staff_id = request.form.get('staff_id')
#         data.credential_fk = request.form.get('staff_id')   
#     data.firstName = request.form.get('+first_name')
#     data.surname = request.form['surname']
#     data.other_name = request.form['other_name']            
#     data.email = request.form['email']
#     data.gender = request.form['gender']
#     data.mobile = request.form['mobile']
#     data.reg_number = request.form['reg_number']
#     data.ssf_no = request.form['ssf']
#     data.bank = request.form['bank']
#     data.bank_branch = request.form['bank_branch']
#     data.date_of_birth = request.form.get('dob')
#     data.employment_type = request.form.get('empl_type')
#     data.status = request.form['status']
#     if request.method == 'PUT':
#         try:
#             updateUser(data)
#             flash('Profile updated', category='info')
#         except:
#             raise flash('Profile not updated', category='info')
#     return redirect(url_for('admin_views.staff_profile'))

      


@crud_views.route('/auth/login', methods=['POST'])
def user_login():

    # User authentication
    if request.method == 'POST':
        staff_id = request.form['staff_id']
        password = request.form['password']
        user_credentials =  userExists(staff_id=staff_id)
        if not user_credentials or user_credentials is None:
            flash('User does not exists', category='info')
            return redirect(url_for('admin_views.sign_in_post'))
        check_pwd = check_password_hash(pwhash=user_credentials['password'], password=password)
        if not check_pwd:
            flash('Please check your password again', category='info')
            return redirect(url_for('admin_views.sign_in_post'))
        session['user'] = user_bio_data(staff_id=staff_id)
        session['staff_id'] = staff_id

        return redirect(url_for('admin_views.staff_profile'))

 
@crud_views.route('/sign_up', methods=['GET','POST'])
def sign_up_post():
    
    '''Add new staff to the school database'''
    if request.method == 'POST':
        first_name = request.form['first_name']
        others = request.form['surname']
        staff_id = request.form['staff_id']
        password = request.form['password']
        conf_password = request.form['confirm_password']
        
        # if password != conf_password:
        #     flash("Password not match", category='info')
        #     return redirect('admin_views.sign_up_post')
        # check if password already exist on this line
    
        user =  userExists(staff_id=staff_id)
        if user:
            flash('User already exits', category='warning')
            return redirect(url_for('admin_views.sign_in_post'))
        user = User()
        user.staff_id = staff_id
        password = generate_password_hash(password, method='pbkdf2:sha256')[10:30]
        user.password = password
        
        sign_ups(user=user)
        flash('New staff registered successufly', category='info')
        return redirect(url_for('admin_views.sign_in_post'))
    return redirect('admin_views.sign_up_post')


'''Professional Qualification Views'''
@crud_views.route('/professional-qualification', methods=['GET','POST'])
def professional_qualification()-> List:
    '''Staff professional qualification'''
    
    if request.method == 'POST':
       
       from_date = request.form['from_date']
       course = request.form['course']
       institution = request.form['institution']
       to_date = request.form['to_date']
       cert_award = request.form['award']
       cert_date = request.form['cert_date']
       prof= Professional(course=course,
                          institution=institution,
                          from_date=from_date,
                          to_date=to_date,
                          cert_date=cert_date,
                          cert_award=cert_award,
                          fk=session.get('data')['staff_id']
                          )
       
       insert_prof(prof=prof)
       flash('Professional qualification updated successfuly',
             category='info')
       return redirect(url_for('admin_views.staff_profile'))

@crud_views.route('/get_prof_qualification')
def get_prof_qualification():
    '''Retrieve all professional qualification of a staff'''
    profs = get_profs_qualificatons()
    for prof in profs:
        session['prof'] = prof
        return render_template('Link to the professional form', prof=prof)
    
@crud_views.route('/sign_out')
def user_sign_out():
    session.clear()
    flash('User signed out', category='info')
    return redirect(url_for('admin_views.sign_in_post'))
