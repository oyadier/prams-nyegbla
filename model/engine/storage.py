from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..user import Base, User
from ..professional import Professional


isSave = False
USER = 'root'
DATABASE = 'pramshigh'
DEFAULT_PORT = '3306'
HOST = 'localhost'
PASSWORD = 'Ro0551987'
mysql_connection = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{DEFAULT_PORT}/{DATABASE}'
engine = create_engine(mysql_connection)
Base.metadata.create_all(engine)

'''Creating a sessionmaker'''

Session = sessionmaker(bind=engine)
session = Session()
def instertUser(newUser:User):
    '''Create an engine for the db'''
    session.add(newUser)
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


def close():
    session.close()
    
def commit():
    try:
        session.commit()
        print("User added successfully.")
    except Exception as e:
        session.rollback()
        close()
        print(f"Failed to add user: {e}")

def insert_prof(prof: Professional):
    session.add(prof)
    commit()
    