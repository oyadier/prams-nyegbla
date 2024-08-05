from flask import Blueprint, render_template, request, session

views = Blueprint('views', __name__)


@views.route("/home/")
def homepage():
    core = ['The capacity to recover quickly from difficulties or setbacks',
            'The ability to achieve maximum productivity with minimum wasted effort or resources.',
            'Self-discipline is the ability to control your own actions and impulses to achieve your goals.',
            'Patience is the capacity to endure waiting, difficulties, or setbacks without getting frustrated.',
            'Excellence is the relentless pursuit of the highest standards.',
            'Confidence is the belief in oneself, abilities, and judgment.',
            'Teamwork is the collaborative effort of individuals working together harmoniously towards a common goal.']
    return render_template('index.html', core=core)

@views.route('/base/')
def base():
    return render_template('base.html')

@views.route("/departments/ict/why_learning_ict")
def ict():
    
    
    tb_content = {'introduction':'Introduction', 
                  'whatIs': 'What is ICT?',
                  'importance': 'Importance of ICT',
                  'career':'Career in ICT',
                  'conclusion':'Conclusion'}
    return render_template("/departments/ict/why_learning_ict.html", tb_content=tb_content)
    
# Launch students personal projects in all possible years
@views.route('/department/ict/student+projects/')
def student_project_ict():
    user = session.get('user')
    if not user:
        return "No data found in session", 400

    return render_template('/departments/ict/students+projects.html', user=user)


@views.route('/events/induction')
def prefect_induction():
    
    return render_template("/events/induction.html")