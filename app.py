# trashy by Tobias Karuth (for cs50 final project)

import os
from sqlite3 import dbapi2

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required
import json

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
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

# make sure that a secure password is chose
def secure_password(contra):
    numbers = sum(c.isdigit() for c in contra)
    letters = sum(c.isalpha() for c in contra)
    sola = len(contra) - numbers - letters
    if numbers < 2:
        return 0
    elif letters < 3:
        return 0
    elif sola < 1:
        return 0
    else:
        return 1

#  ---------------------------------    USERFORM PAGE    -----------------------------------

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
        extra_message = request.form.get("msg")

        # inserts the user in the db
        db.execute("INSERT INTO users ( first_name, last_name, email, city, state, zip, street, house_number, yellow_can, black_can, brown_can, blue_can, extra_message ) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? );"
        , first_name, last_name, email, city, state, zip, street, house_number,yellow_can, black_can, brown_can, blue_can, extra_message)

        return redirect("/") 

    else:
        return render_template("index.html")

#  ---------------------------------    WHAT WE DO PAGE    -----------------------------------

@app.route("/what_we_do")
def what_we_do():
    return render_template("what_we_do.html")

#  ---------------------------------    THE TEAM PAGE    -----------------------------------

@app.route("/where_we_are")
def where_we_are():
    return render_template("where_we_are.html")

#  ---------------------------------    IMPRINT PAGE    -----------------------------------

@app.route("/imprint")
def imprint():
    return render_template("imprint.html")

#  ---------------------------------    ADMIN PAGES    -----------------------------------

# to store admin username in global var for profilepicture (uncomment if the website is hosted and has http)
#if app.route("/admin/login"):
#    admin_username = request.form.get("username")

# comment this out if you are using http 
admin_username = "TK"

#  ---------------------------------    ADMIN PAGE    -----------------------------------

@app.route("/admin", methods=["GET", "POST"])
@login_required
def admin_pannel():

    # get the can amount to display for the graph
    yellow_can_amount_unformatted = db.execute("SELECT COUNT(yellow_can) FROM users WHERE yellow_can = yellow_can;")
    yellow_can_amount_dict = yellow_can_amount_unformatted[0]
    yellow_can_amount = yellow_can_amount_dict['COUNT(yellow_can)']

    black_can_amount_unformatted = db.execute("SELECT COUNT(black_can) FROM users WHERE black_can = black_can;")
    black_can_amount_dict = black_can_amount_unformatted[0]
    black_can_amount = black_can_amount_dict['COUNT(black_can)']

    brown_can_amount_unformatted = db.execute("SELECT COUNT(brown_can) FROM users WHERE brown_can = brown_can;")
    brown_can_amount_dict = brown_can_amount_unformatted[0]
    brown_can_amount = brown_can_amount_dict['COUNT(brown_can)']

    blue_can_amount_unformatted = db.execute("SELECT COUNT(blue_can) FROM users WHERE blue_can = blue_can;")
    blue_can_amount_dict = blue_can_amount_unformatted[0]
    blue_can_amount = blue_can_amount_dict['COUNT(blue_can)']

    differend_can_amounts = [yellow_can_amount, black_can_amount, brown_can_amount, blue_can_amount]
    sumed_can_amounts = yellow_can_amount + black_can_amount + brown_can_amount + blue_can_amount

    # get the data from db for the table on the admin pannel
    all_users = db.execute("SELECT * FROM users;")

    return render_template("admin_pannel.html", avatar=admin_username, users=all_users, sumed_can_amounts=sumed_can_amounts, differend_can_amounts=differend_can_amounts)

#  ---------------------------------    ADMIN LOGIN PAGE    -----------------------------------

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
# Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Query database for username
        rows = db.execute("SELECT * FROM admins WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("Invalid username and/or password", 400)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/admin", 302)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("admin_login.html")

#  ---------------------------------    ADMIN REGISTER PAGE    -----------------------------------        

@app.route("/admin/register", methods=["GET", "POST"])
def admin_register():
    """Register new admins"""
    if request.method == "POST":

        # Ensure username was selected
        if not request.form.get("username"):
            return apology("Must provide username", 400)

        # Ensure password was selected
        elif not request.form.get("password"):
            return apology("Must provide password", 400)

        # if username already exits return apology
        rows = db.execute("SELECT * FROM admins WHERE username = ?", request.form.get("username"))
        if len(rows) == 1:
            invalid = rows[0]["username"]
            return apology(f"The username {invalid} is not avalible", 400)

        # check that confirmation is equal to password
        if request.form.get("password") != request.form.get("confirm"):
            return apology("Password confirmation does not match password", 400)

        # check that the password has at least 8 characters
        if len(request.form.get("password")) < 8:
            return apology("Password must contain at least 8 chararcters", 400)

        # checking that the passwors has at least 2 numbers and one symbol
        if secure_password(request.form.get("password")) == 0:
            return apology("Password must contain at least 2 numbers, 1 symbol", 400)

        # here we save in the users database the information of the new user
        username = request.form.get("username")
        password = generate_password_hash(request.form.get("password"))
        admin_email = request.form.get("email")
        db.execute("INSERT INTO admins (username, hash, email) VALUES(?, ?, ?)", username, password, admin_email)
        valid = db.execute("SELECT * FROM admins WHERE username = ?", username)

        # Remember that new user has logged in
        session["user_id"] = valid[0]["id"]

        # Redirect user to home page
        flash("acount created successfully")
        return redirect("/admin", 302)

    # here we render the register page when a get method is pass
    else:
        return render_template("admin_register.html")

#  ---------------------------------    ADMIN LOGOUT    -----------------------------------

@app.route("/admin/logout")
def admin_logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/admin/login", 302)
