from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import User, db

login_blueprint = Blueprint('login', __name__)

def create_admin_account():
    admin_username = 'admin'
    admin_password = 'Cloud1@'
    admin_user = User.query.filter_by(username=admin_username).first()
    if not admin_user:
        hashed_password = generate_password_hash(admin_password)
        new_admin = User(username=admin_username, password=hashed_password)
        db.session.add(new_admin)
        db.session.commit()
        print("Admin account created with username 'admin' and password 'Cloud1@'")
    else:
        print("Admin account already exists.")

@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['username'] = user.username  # Set the username in the session
            return redirect(url_for('books.book_home'))
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)

@login_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login.login'))
    return render_template('register.html')






