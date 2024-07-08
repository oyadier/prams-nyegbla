from . import create_app
'''A main module for app execution'''

app = create_app()

# Running the flask app

if __name__== "__main__":
    app.run(host='127.0.0.1',port=5000, debug=True)
