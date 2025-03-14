#!/usr/bin/env python3
import secrets
from flask import Flask

def create_app():
    '''entry point for flask app'''
    app = Flask(__name__)
    app.secret_key = secrets.token_hex(16)
    '''Remove strick slash forware'''
    app.url_map.strict_slashes = False
    
    from api.v1.user_views import crud_views
    from views import views
    from admin_views import admin_views
    from course import course
   
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(course, url_prefix="/courses")
    app.register_blueprint(admin_views, url_prefix="/admin")
    app.register_blueprint(crud_views, url_prefix="/v1/api")
    return app