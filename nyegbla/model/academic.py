#!/usr/bin/env python3
'''This model in an academic qualification model.
    It contain attributes of the academic qualification attained
    by the staff
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Academics(Base):
    '''Table attributes of the academic qualification'''
    __tablename__ = 'academic_qualification'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    level = Column(String(20), nullable=False)
    subject_passed = Column(String(200), nullable=False)
    year = Column(String(20), nullable=False)
    
    def __to_dict__(self):
        '''Serialized the Academy class to be jsonify'''
        return {
            'id': self.id,
            'level':self.level,
            'subject_passed': self.subject_passed,
            'year': self.year
        }
        
    def __rep__(self):
        '''Change the attributes to string'''
        return f'<{self.__class__}={
            "id": {self.id}
            "level": {self.level}
            "subject_passed": {self.subject_passed}
            "year": {self.year}
            }'
