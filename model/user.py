#!/usr/bin/env python
'''Defining the base model for all users'''
from sqlalchemy import  Integer, String, UniqueConstraint, Column, ForeignKey, Date
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from time import time, strftime, localtime
from typing_extensions import Annotated
from typing import List
import uuid




time_formatter = '%Y/%m/%d %H:%M:%S'
current_loccal_time = time()

str_40 = Annotated[str, mapped_column(String(40), nullable=False)]
str_200 = Annotated[str, mapped_column(String(200), nullable=False)]
def generate_uuid():
    return str(uuid.uuid4())

class Base(DeclarativeBase):
    pass


class User(Base):
    
    __tablename__ = 'user'
    '''Defining the user model and why is the Unique=True not working for staff_di?'''
    user_id: Mapped[str] = mapped_column(String(40), primary_key=True, default=generate_uuid, nullable=False)
    staff_id:Mapped[str_40]
    firstName : Mapped[str_200]
    date_of_birth : Mapped[str_40]
    created_at : Mapped[str] = mapped_column(String(30), default=strftime(time_formatter, localtime(current_loccal_time)))
    employment_type: Mapped[str] = mapped_column(String(200), name='type', nullable=False)
    profession: Mapped[List["Professional"]] = relationship('Professional', back_populates='user')
    __table_args__  = (UniqueConstraint('staff_id'),)

    def __rep__(self):
        return f"<User(name='{self.firstName}', dob={self.date_of_birth})>"
    
    def __to_dict__(self):
        '''Return a dictionary of the user object'''
        return {
            self.user_id: {
                'user_id': self.user_id,
                'staff_id': self.staff_id,
                'firstName': self.firstName,
                'date_of_birth': self.date_of_birth,
                'type': self.employment_type,
                'created_at': self.created_at
            }
        }
        
        
class Professional(Base):
    '''Professional Qualification of staff'''
    __tablename__ = 'prof_qualification'
    pro_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    course = Column(String(200), nullable=False)
    institution = Column(String(200), nullable=False)
    from_date = Column(Date, nullable=False)
    to_date = Column(Date, nullable=False)
    cert_award_date = Column(Date, nullable=False)
    user_fk = Column(String(40), ForeignKey("user.user_id"))
    user = relationship('User')

    def __init__(self, course, institution, from_date, to_date, cert_award_date):
        self.course = course
        self.institution = institution
        self.from_date = from_date
        self.to_date = to_date
        self.cert_award_date = cert_award_date

    def __repr__(self):
        return "<Professional(course='{}', institution='{}', from_date='{}', to_date='{}', cert_award_date='{}')>".format(
            self.course, self.institution, self.from_date, self.to_date, self.cert_award_date
        )

    def to_dict(self):
        return {
            'pro_id': self.pro_id,
            'course': self.course,
            'institution': self.institution,
            'from_date': self.from_date,
            'to_date': self.to_date,
            'cert_award_date': self.cert_award_date
        }
        