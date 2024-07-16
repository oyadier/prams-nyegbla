from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..user import Base, User
from ..professional import Professional
from ..auth_credential import CredentialAuth

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
    print('User added successfully')
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



def insert_prof(prof: Professional):
    session.add(prof)
    commit()
    
    
def auth(staff_id: str):
    user = session.query(User).filter(User.staff_id==staff_id).first()
    if user is None:
        return {'None': 'Not user in the database'}
    return user.__to_dict__()

def credentials(staff_id: str):
    credent = session.query(CredentialAuth).filter(CredentialAuth.staff_id==staff_id).first()
    if credent is None:
        return None
    return credent.__to_dict__()

def sign_up(credential: CredentialAuth):
    session.add(credential)
    session.commit()
    print('Credential added successufly')
    session.rollback()
    session.close()
   
    
def commit():
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Failed to add user: {e}")
        session.close()