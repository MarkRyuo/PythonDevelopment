# imports 
from flask import Flask, render_template  # Import Flask 
from flask_scss import Scss  # importing Flask Sass
# from flask_sqlalchemy import SQLAlchemy # Import flask-sqlalchemy 

# My app 
app = Flask(__name__) 
Scss(app) # * for importing the Scss

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

@app.route("/") # always add / for route 
def index() :
    return render_template("index.html")

@app.route("/homepage") 
def homepage():
    return render_template("Homepage.html")

if __name__ == '__main__' :
    app.run(debug=True)