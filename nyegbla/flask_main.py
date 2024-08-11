import secrets
from flask import Flask
from  creator import create_app
'''A main module for app execution'''


# Running the flask app

if __name__== "__main__":
    app = create_app()
    app.run(host='127.0.0.1',port=5000)
else:
    gunapp = create_app()