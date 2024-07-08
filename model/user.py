#!/usr/bin/env python
'''Defining the base model for all users'''
from sqlalchemy import Column, Integer, String, UUID, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from time import time, strftime, localtime
import uuid

time_formatter = '%Y/%m/%d %H:%M:%S'
current_loccal_time = time()
Base = declarative_base()
def generate_uuid():
    return str(uuid.uuid4())

class User(Base):
    __tablename__ = 'user'
    '''Defining the user model and why is the Unique=True not working for staff_di?'''
    user_id = Column(String(40), primary_key=True, default=generate_uuid, nullable=False)
    staff_id = Column(String(30), nullable=False)
    firstName = Column(String(250), nullable=False)
    date_of_birth = Column(String(250), nullable=True)
    created_at = Column(String(50), default=strftime(time_formatter, localtime(current_loccal_time)))

    __table_args__ = (UniqueConstraint('staff_id'),)

    def __rep__(self):
        return f"<User(name='{self.firstName}', dob={self.date_of_birth})>"