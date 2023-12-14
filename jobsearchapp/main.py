from flask import Flask
from login import login_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(login_blueprint)
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
