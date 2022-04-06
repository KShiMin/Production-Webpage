from cgitb import text
from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

# methods = a list of request that can be gotten
@auth.route('/login', methods=['GET','POST'])
def login():
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return render_template("home.html")


@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        fname = request.form.get('fname')
        password = request.form.get('pass')
        confirmpass = request.form.get('confirmpass')
        
        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(fname) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password != confirmpass:
            flash('Password don\'t match.', category='error')
        elif len(password) < 8:
            flash('Password must be at least 8 characters', category='error')
        else:
            # add user to database
            flash('Account created!', category='success')
    
    return render_template("sign_up.html")
