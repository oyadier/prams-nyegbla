from flask import Blueprint, render_template

admin_views = Blueprint('admin_views',__name__)

@admin_views.route('/admission')
def administration():
   return render_template('departments/admin/admission.html')


@admin_views.route('/languages')
def languages():
   return render_template('departments/languages/why+study+language.html')

@admin_views.route('/home+economics')
def homeecons():
   return render_template('departments/home_econs/why_learning_home_econs.html')

