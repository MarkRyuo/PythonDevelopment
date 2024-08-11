# imports 
from flask import Flask  # Import Flask 
# from flask_scss import Scss  # importing Flask Sass
# from flask_sqlalchemy import SQLAlchemy # Import flask-sqlalchemy 

# My app 
app = Flask(__name__) 


@app.route("/")
def index() :
    return "Hello World"

if __name__ == '__main__' :
    app.run(debug=True)