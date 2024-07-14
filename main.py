#!/usr/bin/env python3
from model.engine.storage import instertUser
from model.user import User
from model.engine.storage import isSave
import requests
import sys

data = User()
if len(sys.argv) < 5:
    print('Usage: staff_Id firstname dof type')
    exit(0)
data.staff_id = sys.argv[1]
data.firstName = sys.argv[2]
data.date_of_birth = sys.argv[3]
data.employment_type = sys.argv[4]

if isSave:
    print('User added successfully')

