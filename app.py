# trashy by Tobias Karuth (for cs50 final project)

import os
from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
#from werkzeug.security import check_password_hash, generate_password_hash

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///trashy_user.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response
# TODO different routs to add 

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form.get("first_name") 
        last_name = request.form.get("last_name") 
        email = request.form.get("email") 
        city = request.form.get("city") 
        state = request.form.get("state") 
        zip = request.form.get("zip") 
        street = request.form.get("street") 
        house_number = request.form.get("house_number") 
        yellow_can = request.form.get("yellow_can") 
        black_can = request.form.get("black_can") 
        brown_can = request.form.get("brown_can") 
        blue_can = request.form.get("blue_can")

        # inserts the user in the db 
        db.execute("INSERT INTO users ( first_name, last_name, email, city, state, zip, street, house_number, yellow_can, black_can, brown_can, blue_can ) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? );"
        , first_name, last_name, email, city, state, zip, street, house_number,yellow_can, black_can, brown_can, blue_can)

        # TODO add an alert to say that succesfully got submited

        return redirect("/") 

    else:
        return redirect("index.html")

@app.route("/what_we_do")
def what_we_do():
    return render_template("what_we_do.html")

@app.route("/where_we_are")
def where_we_are():
    return render_template("where_we_are.html")

@app.route("/imprint")
def imprint():
    return render_template("imprint.html")