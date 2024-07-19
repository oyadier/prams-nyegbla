#!/usr/bin/env python3
''''A model for the staff professional qualifications '''
from sqlalchemy import DateTime, String, Integer, Column, Date, ForeignKey
from typing import List
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

       
class Professional(Base):
    '''Professional Qualification of staff'''
    __tablename__ = 'prof_qualification'
    pro_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    course = Column(String(200), nullable=False)
    institution = Column(String(200), nullable=False)
    from_date = Column(Date, nullable=False)
    to_date = Column(Date, nullable=False)
    cert_award_date = Column(Date, nullable=False)
    user_fk = Column(String(40), ForeignKey("user.user_id"), nullable=False)


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
