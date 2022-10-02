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
        db.execute("INSERT")

    else:
        return render_template("index.html")
