from flask import Flask
from models import db
from login import login_blueprint, create_admin_account
from book_routes import book_blueprint  # Import the book routes
# Assuming you have a blueprint for search functionality
from search import search_blueprint

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()  # Create database tables
        create_admin_account()  # Create the admin account

    app.register_blueprint(login_blueprint, url_prefix='/')
    app.register_blueprint(book_blueprint, url_prefix='/books')  # Register book routes
    app.register_blueprint(search_blueprint, url_prefix='/search')  # Register search routes

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)



