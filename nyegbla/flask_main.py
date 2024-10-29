import secrets
from flask import Flask
from  creator import create_app
from dotenv import load_dotenv
'''A main module for app execution'''


# Running the flask app
# load_dotenv('.env')# Loading all the virtual environment set
if __name__== "__main__":
    
    app = create_app()
else:
    gunapp = create_app()