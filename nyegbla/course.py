from flask import Blueprint, render_template
'''This is a module that '''

course = Blueprint('course',__name__)


@course.route('/vitual-art-graphic-course-overview')
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


@course.route('/couses/home-econs-two-clothing')
def homeEconsTwo():
    return render_template('courses/home-economics-option-two.html')

@course.route('/home-econs-option-one-food')
def homeEconsOne():
    return render_template('courses/home-economics-option-one.html')

@course.route('/business')
def business():
    return render_template('courses/business.html')

@course.route("/subject/general_science")
def general_science():
    tb_content = {'description':'Course Description.', 
                  'whatYou': 'What You Will Learn.',
                  'skills': 'Key Skills You Will Develop',
                  'why':'Why Take This Course',
                  'career':'Career Opportunities in Science',
                  'combination': 'Subject Combination',
                  'conclusion':'Conclusion'}
    return render_template("/courses/general-science.html", tb_content=tb_content)
@course.route('/general-science')
def  generalScience():
    return render_template('courses/general-science.html')