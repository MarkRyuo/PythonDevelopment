# imports 
from flask import Flask, render_template  # * Import Flask and render_template for html
from flask_scss import Scss # * importing Flask Sass
from flask_sqlalchemy import SQLAlchemy # * Import flask-sqlalchemy
from datetime import datetime 

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
    complete = db.Column(db.Integer, default=0)
    created = db.Column(db.DateTime, default=datetime)

    def __repr__(self) -> str:
        return f"Task {self.id}"







@app.route("/") # always add / for route 
def index() :
    return render_template("index.html")

@app.route("/homepage") 
def homepage():
    return render_template("Homepage.html")

if __name__ == '__main__' :
    app.run(debug=True)