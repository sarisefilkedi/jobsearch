from flask import Blueprint, render_template, request, redirect, url_for

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/')
@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if (username == 'user1' and password == '1') or \
           (username == 'user2' and password == '2'):
            return redirect(url_for('search.search_jobs'))
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)

@login_blueprint.route('/home')
def home():
    return 'Logged in successfully.'

