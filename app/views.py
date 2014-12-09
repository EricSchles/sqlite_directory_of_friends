from app import app
from flask import render_template,redirect, request, flash,g,session,url_for
from models import *

@app.route("/",methods=["GET","POST"])
@app.route("/index",methods=["GET","POST"])
def index():
    return render_template("index.html")


@app.route("/signup", methods=["GET","POST"])
def signup():
    return render_template("signup.html")

@app.route("/signedup", methods=["GET","POST"])
def signedup():
    
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    phone = request.form.get('phone')

    if not session.get("logged_in"):
        insert_account_holder(email,username,phone,password)
    return render_template("homepage.html",username=username) 

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/directory/<username>")
def directory(username):
    contacts = models.Contact.query.all()
    return render_template("directory.html",username=username,contacts=contacts)

@app.route("/info/<username>/<person>")
def info(username,person):
    return render_template("info.html",username=username,person=person)

@app.route("/home/<username>")
def homepage(username):
    return render_template("homepage.html",username=username)

@app.route("/add_contact/<username>")
def add_contact(username):    
    return render_template("add_contact.html",username=username)

@app.route("/adding/<username>", methods=["GET","POST"])
def adding(username):
        
    if request.form.get('name') == None:
        flash("Please give us a name, at least")
    else:
        name = request.form['name']
        
    phone = request.form.get('phone')
    email = request.form.get('email')
    picture = request.form.get('picture')
    return redirect("/home",username=username) # add a route to the signed in homepage
