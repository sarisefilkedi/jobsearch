from flask import Blueprint, render_template, request, redirect, url_for

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if (username == 'user1' and password == 'password1') or \
           (username == 'user2' and password == 'password2'):
            return redirect(url_for('main.home'))  # Assuming 'home' function is in the main module
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)
