Flask Environment 
 
# Creating Environment 
 
### Creating env folder: 
 $ python3 -m venv env

### Active the environment:
 $ source env/bin/activate

### Deactive the environment: 
 $ deactivate

### Pip list
 $ pip list

### Importing  a bunch of staff: 
 $ pip3 install Flask or 
 $ pip3 install Flask Flask-Scss Flask-SQLAlchemy 


Make a requirements text file, these are the dependencies and packages that anyone who works with this project is going to need. 

 $ pip freeze > requirements.txt 
 
Create a folder name: static 
 - static folder is use for bunch of file like css, js files.
 
Create a folder name: templates
 - templates for html pages etc. 
 - importing in app.py use this command
   - from flask import Flask, render_template  # Import Flask using template 
   - ex. code
   @app.route("/")
	def index() :
    		return render_template("index.html") # Use render template("example.html")
