from flask import Blueprint, render_template
'''This is a module that '''

course = Blueprint('course',__name__)


@course.route('/vitual-art-option-one')
def vitualArtOne():
    return render_template('courses/vitual-art-one.html')

@course.route('/vitual-art-option-two')
def vitualArtTwo():
    return render_template('courses/vitual-art-two.html')

@course.route('/government')
def government():
    gov_course = ['Core Math', 'Core English Language', 'Core Science']
    return render_template('courses/government.html', course_cmb= gov_course)

@course.route('/christian-religious-study')
def crs():
    return render_template('courses/christian-religious-studies.html')


@course.route('/couses/home-econs-two')
def homeEconsTwo():
    return render_template('courses/home-economics-option-two.html')

@course.route('/home-econs-one')
def homeEconsOne():
    return render_template('courses/home-economics-option-one.html')

@course.route('/business')
def business():
    return render_template('courses/business.html')
@course.route('/general-science')
def  generalScience():
    return render_template('courses/general-science.html')