from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    writer = db.Column(db.String(200), nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    literature = db.Column(db.String(100), nullable=False)
    language = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Book {self.name}>'

