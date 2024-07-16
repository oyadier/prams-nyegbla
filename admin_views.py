from flask import Blueprint, jsonify, render_template
from .model.engine.storage import getUser

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
   return render_template('departments/admin/staff-profile.html')