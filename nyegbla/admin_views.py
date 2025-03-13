from flask import Blueprint, redirect, render_template, session, url_for
from model.engine.storage import staff_profile

admin_views = Blueprint('admin_views',__name__)

@admin_views.route('/sign-in-staff')
def sign_in_post():
   '''An existing user sign in into his profile'''
   return render_template('departments/admin/sign_in.html')

@admin_views.route('/online-admission')
def online_admission():
   return render_template('departments/admin/online-admission.html')

@admin_views.route('/sign-up')
def sign_up_post():
   '''Sign Up a new staff by adding his/her staff id into the db'''
   return render_template('departments/admin/sign_up.html')
   

@admin_views.route('/departments/languages/in-perspective')
def languages():
   return render_template('departments/languages/general_overview.html')

@admin_views.route('/home-economics')
def homeecons():
   return render_template('departments/home_econs/why_learning_home_econs.html')

@admin_views.route('/staff/staff-profile')
def staff_profile():
   # A session from sign in page
    data = session.get('user')
    
    if data:
       return render_template('departments/admin/profile.html', data=data)

@admin_views.route('/profile-sign-in')
def profile_sign_in():
    return render_template('/departments/ict/students+projects.html')
 
@admin_views.route('/about_us')
def about_us():
    return render_template('/about_us.html')

