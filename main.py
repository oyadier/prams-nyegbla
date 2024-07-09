#!/usr/bin/env python3
from model.engine.storage import instertUser
from model.user import User
from model.engine.storage import isSave
import sys

user = User()
if len(sys.argv) < 3:
    print('Usage: firstname dof')
    exit
user.staff_id = sys.argv[1]
user.firstName = sys.argv[2]
user.date_of_birth = sys.argv[3]
user.employment_type = sys.argv[4]

instertUser(newUser=user)
if isSave:
    print('User added successfully')

