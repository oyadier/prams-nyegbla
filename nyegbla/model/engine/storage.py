#!/usr/bin/env python3
from typing import List
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..professional import Professional
from ..user import User
from ..base import Base
import os
from dotenv import load_dotenv

'''The database connection. It also create all tables need in the system'''
load_dotenv('.env')
DB_USER = os.environ.get('DB_USER')
DATABASE = os.environ.get('DATABASE_NAME')
DEFAULT_PORT = os.environ.get('DEFAULT_PORT')
HOST = os.environ.get('HOST')
PASSWORD = os.environ.get('DB_PASSWORD')
mysql_connection = f'mysql+pymysql://{DB_USER}:{PASSWORD}@{HOST}:{DEFAULT_PORT}/{DATABASE}'
print("pramshigh-edu.com is up running")
engine = create_engine(mysql_connection)
Base.metadata.create_all(engine)

'''Creating a sessionmaker'''

Session = sessionmaker(bind=engine)
session = Session()

    
def commit():
    try:
        session.commit()
        session.expire_on_commit(True)
        print("New user added successufly")
    except Exception as e:
        print(f"Failed to add user: {e}") 
    session.rollback()
    session.close()

def instertUser(newUser:User):
    '''Create an engine for the db'''
    session.add(newUser)
    commit()

def updateUser(newUser:User):
    '''Create an engine for the db'''
    print("User Data: ", newUser)
    session.query(User).filter(User.user_id == newUser['user_id']).update({'firstName':newUser['firstName'],
                                                                           'surname':newUser['surname'],
                                                                           'other_name':newUser['other_name'],
                                                                           'email':newUser['email'],
                                                                           'gender':newUser['gender'],
                                                                           'mobile':newUser['mobile'],
                                                                           'ssf_no':newUser['ssf_no'],
                                                                           'bank':newUser['bank'],
                                                                           'bank_branch':newUser['bank_branch'],
                                                                           'type':newUser['type'],
                                                                           'date_of_birth':newUser['date_of_birth']})                                                                  
    commit()
  

def getUser(staff_id=None):
    '''Get all users from the db'''
    staff=[]
    if staff_id:
        users = session.query(User).all()
        if int(staff_id) <= len(users):
            staff.append(users[int(staff_id)].__to_dict__())
            return staff
    return f'Your querry with this input {staff_id} might be None or Out of index-range. Thanks'
    

def all_staff():
    '''Return all the staff in the system'''
    staff = []
    users = session.query(User).order_by( User.firstName, User.created_at)
    for teacher in users:
        staff.append(teacher.__to_dict__())
    return staff
    
def user_bio_data(staff_id: str):
    '''Make a query for a staff with a particular staff id'''
    user = session.query(User).filter(
        User.staff_id==staff_id).first()
    if user:
        return user.__to_dict__()
    return {}

def userExists(staff_id: str):
    '''
    Make a query to into the User table to
    check if staff with a specific ID already exist.
        Arg:
            staff_id(String): Staff ID of a staff
        Return:
            Staff_ID: the staff id of an existed staff
    '''
    credent = session.query(User).filter(
        User.staff_id==staff_id).first()
    if credent:
        return credent.__to_dict__()
    return None


def sign_ups(user: User):
    session.add(user)
    commit()
    
    print('New user added successufly')
    

'''This section begins the promotion section'''

def insert_prof(prof: Professional):
    '''Inserting data into the professional qualification table'''
    session.add(prof)
    print('Add prof')
    commit()
    
    
def get_profs_qualificatons(prof: Professional)-> List['Professional']:
    profs = []
    all_prof = session.query(Professional).all()
    for prof in all_prof:
        profs.append(prof)
        
    return profs

def update_user(user: User):
    user = User()
    for key in user:
        if hasattr(user, key):
            setattr(user, key, user[key])
    session.commit()
        
    
