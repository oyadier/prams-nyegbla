#!/usr/bin/env python3
from model.engine.storage import instertUser
from model.user import User
import sys

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
    

