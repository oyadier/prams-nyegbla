#!/usr/bin/env python3
from model.engine.storage import instertUser, insert_prof
from model.user import User
from model.util import get_to_timedate
from model.professional import Professional
import datetime
import sys

# def user():
new_user = User()
param = len(sys.argv)
if param < 9:
    print(f'Usage: firstname surname dob email mobile gender status type. <{param}>')
    exit(0)
new_user.staff_id = sys.argv[1]
new_user.firstName = sys.argv[2]
new_user.surname = sys.argv[3]
new_user.date_of_birth = sys.argv[4]
new_user.email = sys.argv[5]
new_user.mobile = sys.argv[6]
new_user.gender = sys.argv[7]
new_user.status = sys.argv[8]
new_user.employment_type = sys.argv[9]
new_user.credential_fk = sys.argv[10]
instertUser(newUser=new_user)
    
# param = len(sys.argv)
# if param < 5:
#     print(f'Usage: course institute from_date to-date cert fk')
#     exit(0)

# course = sys.argv[1]
# institute = sys.argv[2]
# from_date = sys.argv[3]
# to_date = sys.argv[4]
# cert_date = sys.argv[5]
# cert = sys.argv[6]
# fk = sys.argv[7]
# cre_date = get_to_timedate()
# prof = Professional(
#     course=course,
#     institution=institute,
#     from_date=from_date,
#     to_date=to_date,
#     cert_date=cert_date,
#     cert_award=cert, 
#     fk=fk)
# prof.created_at=cre_date
# insert_prof(prof)
    
    
# if __name__ == "__main__":
#     option = input("Enter opton\n 1. Add user\n2. Add Prof\n")
#     match option:
#         case 1:
#             user()
#         case 2:
#             prof()

