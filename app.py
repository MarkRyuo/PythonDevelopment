# imports 
from flask import Flask  # Import Flask 
from flask_scss import Scss  # importing Flask Sass
from flask_sqlalchemy import SQLAlchemy # Import flask-sqlalchemy 

# My app 
app = Flask(__name__) 


@app.route("/")
def index() :
    return "testing 123"

