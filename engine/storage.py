from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.user import Base, User

isSave = False

def instertUser(newUser:User):
    '''Create an engine for the db'''
    mysql_connection = f'mysql+pymysql://root:Ro0551987@localhost:3306/pramshigh'
    engine = create_engine(mysql_connection)
    Base.metadata.create_all(engine)

    '''Creating a sessionmaker'''

    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(newUser)
    try:
        session.commit()
        print("User added successfully.")
    except Exception as e:
        session.rollback()
        print(f"Failed to add user: {e}")
    finally:
        session.close()
