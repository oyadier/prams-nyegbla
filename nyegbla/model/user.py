#!/usr/bin/env python
'''Defining the base model for all users'''
from sqlalchemy import String, UniqueConstraint
from sqlalchemy.orm import mapped_column, Mapped
from time import time, strftime, localtime
from typing_extensions import Annotated
from typing import List
from .base import Base
import uuid


time_formatter = '%Y/%m/%d %H:%M:%S'
current_loccal_time = time()

str_40 = Annotated[str, mapped_column(String(40), nullable=False)]
str_100 = Annotated[str, mapped_column(String(100), nullable=True)]
def generate_uuid():
    return str(uuid.uuid4())


class User(Base):
    
    __tablename__ = 'user'
    '''Defining the user model and why is the Unique=True not working for staff_di?'''
    user_id: Mapped[str] = mapped_column(String(40), primary_key=True, default=generate_uuid, nullable=False)
    staff_id:Mapped[str_40]
    password:Mapped[str_40]
    firstName : Mapped[str_40]
    surname: Mapped[str_40]
    other_name: Mapped[str_100]
    date_of_birth : Mapped[str_100]
    email: Mapped[str_100]
    mobile: Mapped[str_100]
    gender:Mapped[str_100]
    reg_number:Mapped[str_100]
    ssf_no : Mapped[str_100]
    bank :Mapped[str_100]
    bank_branch: Mapped[str_100]
    status = Mapped[str_100]
    created_at : Mapped[str] = mapped_column(String(30), default=strftime(time_formatter, localtime(current_loccal_time)))
    category: Mapped[str_100]
    __table_args__  = (UniqueConstraint('staff_id'))

    def __rep__(self):
        return f"<User(name='{self.firstName}', dob={self.date_of_birth})>"
    
    def __to_dict__(self):
        '''Return a dictionary of the user object'''
        return {
                'user_id': self.user_id,
                'staff_id': self.staff_id,
                'firstName': self.firstName,
                'surname': self.surname,
                'other_name': self.other_name,
                'gender': self.gender,
                'email': self.email,
                'bank': self.bank,
                'bank_branch': self.bank_branch,
                'ssf_no': self.ssf_no,
                'mobile': self.mobile,
                'date_of_birth': self.date_of_birth,
                'category': self.category,
                'created_at': self.created_at,
                'reg_number': self.ssf_no,
                'status': self.status
            }

 