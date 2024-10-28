#!/usr/bin/env python3
'''Defining the base model for user authentication'''
from sqlalchemy import  Integer, String
from sqlalchemy.orm import mapped_column, Mapped, relationship
from time import time, strftime, localtime
from typing_extensions import Annotated

from .base import Base


time_formatter = '%Y/%m/%d %H:%M:%S'
current_loccal_time = time()

class User(Base):
    __tablename__= 'credentials'
    auth_id:Mapped[int] = mapped_column(Integer, primary_key=True, unique=True, autoincrement=True)
    staff_id:Mapped[str] = mapped_column(String(200), nullable=False, unique=True)
    password:Mapped[str] = mapped_column(String(1000), nullable=False)
    created_at : Mapped[str] = mapped_column(String(30), default=strftime(time_formatter, localtime(current_loccal_time)))
    

    def __to_dict__(self):
        return {
            'auth_id': self.auth_id,
            'created_at': self.auth_id,
            'staff_id': self.staff_id,
            'password': self.password
        }
