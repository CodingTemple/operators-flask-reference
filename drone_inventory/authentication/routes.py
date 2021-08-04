from flask import Blueprint, render_template, request, redirect, url_for, flash
from drone_inventory.forms import UserLoginForm
from drone_inventory.models import User, db


auth = Blueprint('auth', __name__, template_folder='auth_templates')


@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print(email, password)

        #Creating a new user instance and adding that user to the User Table
        user = User(email, password)
        db.session.add(user)
        db.session.commit()

        # Flashed message for successful sign up
        flash(f'You have successfully created a user account {email}', 'user-created')
        #Redirecting to home page
        return redirect(url_for('site.home'))

    return render_template('signup.html', form = form)

@auth.route('/signin', methods = ['GET', 'POST'])
def signin():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print(email, password)
    
    return render_template('signin.html', form = form)
