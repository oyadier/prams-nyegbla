from flask import Blueprint, redirect, render_template, session, url_for
from .model.engine.storage import user_bio_data

admin_views = Blueprint('admin_views',__name__)

@admin_views.route('/sign_in_staff')
def sign_in_post():
   '''An existing user sign in into his profile'''
   return render_template('departments/admin/sign_in.html')
   
@admin_views.route('/sign_up')
def sign_up_post():
   '''Sign Up a new staff by adding his/her staff id into the db'''
   return render_template('departments/admin/sign_up.html')
   

@admin_views.route('/languages')
def languages():
   return render_template('departments/languages/why+study+language.html')

@admin_views.route('/home+economics')
def homeecons():
   return render_template('departments/home_econs/why_learning_home_econs.html')

@admin_views.route('/staff/staff-profile')
def staff_profile():
   # A session from sign in page
    data = session.get('data')
    if not data:
       return redirect(url_for('admin_views.sign_in_post'))
    data = user_bio_data(staff_id=data['staff_id'])
    
    return render_template('departments/admin/user.html', data=data)

@admin_views.route('/profile_sign_in')
def profile_sign_in():
    return render_template('/departments/ict/students+projects.html')