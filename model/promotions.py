#!/usr/bin/env python3
'''A model for the staff professional qualifications.'''
from sqlalchemy import String, Integer, Column, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Promotion(Base):
    '''Staff Promotion model for keeping promotion records'''
    
    promotion_id = Column(Integer, primary_key=True)
    effective_date = Column(Date, nullable=False)
    salary_scale = Column(String(20), nullable=False)
    entry_point = Column(String(20), nullable=True)
    
    def __to_dict__(self):
        '''Serialiazing the Promotion to dictionay format'''
        return {
            'promoton_id': self.promotion_id,
            'effective_date': self.effective_date,
            'salary_scale':self.salary_scale,
            'entry_point': self.entry_point
        }
        
    def __rep__(self):
        '''Return a string representation of the class'''
        return "<Promotion(id={}, effective_date={}, salary_scale={}, entry_point={})".format(
            self.promotion_id, self.effective_date, self.salary_scale, self.entry_point   
        )