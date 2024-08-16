# imports 
from flask import Flask, render_template  # Import Flask 
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy  # importing Flask Sass
# from flask_sqlalchemy import SQLAlchemy # Import flask-sqlalchemy 

# My app 
app = Flask(__name__) 
Scss(app) # * for importing the Scss

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

# * Data class - row of data
class MyTask(db.Model) :
    id
    content 





@app.route("/") # always add / for route 
def index() :
    return render_template("index.html")

@app.route("/homepage") 
def homepage():
    return render_template("Homepage.html")

if __name__ == '__main__' :
    app.run(debug=True)