#!/usr/bin/env python
'''Defining the base model for all users'''
from sqlalchemy import  Integer, String, UniqueConstraint, Column, ForeignKey, Date
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from time import time, strftime, localtime
from typing_extensions import Annotated
from typing import List
from .base import Base
import uuid


time_formatter = '%Y/%m/%d %H:%M:%S'
current_loccal_time = time()

str_40 = Annotated[str, mapped_column(String(40), nullable=False)]
str_200 = Annotated[str, mapped_column(String(200), nullable=False)]
def generate_uuid():
    return str(uuid.uuid4())


class User(Base):
    
    __tablename__ = 'user'
    '''Defining the user model and why is the Unique=True not working for staff_di?'''
    user_id: Mapped[str] = mapped_column(String(40), primary_key=True, default=generate_uuid, nullable=False)
    staff_id:Mapped[str_40]
    firstName : Mapped[str_200]
    surname: Mapped[str_200]
    other_name: Mapped[str] =  mapped_column(String(200), nullable=True)
    date_of_birth : Mapped[str_40]
    email: Mapped[str_40]
    mobile: Mapped[str_40]
    gender:Mapped[str_40]
    reg_number:Mapped[str] = mapped_column(String(40), nullable=True)
    ssf_no : Mapped[str] = mapped_column(String(50), nullable=True)
    bank :Mapped[str] = mapped_column(String(200), nullable=True)
    bank_branch: Mapped[str] = mapped_column(String(200), nullable=True)
    status = Mapped[str_40]
    created_at : Mapped[str] = mapped_column(String(30), default=strftime(time_formatter, localtime(current_loccal_time)))
    employment_type: Mapped[str] = mapped_column(String(200), name='type', nullable=False)
    credential_fk:Mapped[str] = mapped_column(ForeignKey('user.staff_id'), nullable=False)
    __table_args__  = (UniqueConstraint('staff_id'),)

    def __rep__(self):
        return f"<User(name='{self.firstName}', dob={self.date_of_birth})>"
    
    def __to_dict__(self):
        '''Return a dictionary of the user object'''
        return {
                'user_id': self.user_id,
                'staff_id': self.staff_id,
                'firstName': self.firstName,
                'surname': self.surname,
                'gender': self.gender,
                'email': self.email,
                'bank': self.bank,
                'bank_branch': self.bank_branch,
                'ssf_no': self.ssf_no,
                'mobile': self.mobile,
                'date_of_birth': self.date_of_birth,
                'type': self.employment_type,
                'created_at': self.created_at,
                'reg_number': self.ssf_no
            }

 