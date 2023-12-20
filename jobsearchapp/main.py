from flask import Flask
from models import db, User

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    with app.app_context():
        db.create_all()  # Create database tables

    # Import blueprints AFTER initializing db to avoid circular imports
    from login import login_blueprint
    from search import search_blueprint

    # Register the search blueprint with '/search' prefix
    app.register_blueprint(search_blueprint, url_prefix='/search')
    
    # Register the login blueprint with '/' prefix
    app.register_blueprint(login_blueprint, url_prefix='/')

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)



