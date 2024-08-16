# imports 
from email.policy import default
from flask import Flask, render_template  # Import Flask 
from flask_scss import Scss # importing Flask Sass
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Nullable  
from datetime import datetime
# from flask_sqlalchemy import SQLAlchemy # Import flask-sqlalchemy 

# My app 
app = Flask(__name__) 
Scss(app) # * for importing the Scss

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

# * Data class - row of data
class MyTask(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), Nullable=False)
    complete = db.Column(db.Integer)
    created = db.Column(db.DateTime, default=datetime)







@app.route("/") # always add / for route 
def index() :
    return render_template("index.html")

@app.route("/homepage") 
def homepage():
    return render_template("Homepage.html")

if __name__ == '__main__' :
    app.run(debug=True)