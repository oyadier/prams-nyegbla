from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from .views import views
    from .admin_views import admin_views
    from .course import course
    
    app.register_blueprint(views, url_prefix="/v1/pramshigh")
    app.register_blueprint(course, url_prefix="/v1/pramshigh/courses")
    app.register_blueprint(admin_views, url_prefix="/v1/pramshigh/admin")
    return app