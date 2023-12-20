from flask import Blueprint, render_template, jsonify, request
import json

book_blueprint = Blueprint('books', __name__)

with open('all_books.json') as f:
    all_books = json.load(f)

@book_blueprint.route('/')
def book_home():
    return render_template('book_home.html'), 200

@book_blueprint.route('/languages/')
def get_language():
    languages = list(set(item["language"] for item in all_books))
    return render_template('languages.html', languages=languages), 200

@book_blueprint.route('/literatures/')
def get_literature():
    literatures = list(set(item["literature"] for item in all_books))
    return render_template('literatures.html', literatures=literatures), 200

@book_blueprint.route('/literature/<literature>/')
def books_by_literature(literature):
    books = next((item["books"] for item in all_books if item["literature"] == literature), [])
    if not books:
        return jsonify({'error': 'Literature not found'}), 404
    return render_template('books_list.html', books=books, category=literature), 200

@book_blueprint.route('/language/<language>/')
def books_by_language(language):
    books = next((item["books"] for item in all_books if item["language"] == language), [])
    if not books:
        return jsonify({'error': 'Language not found'}), 404
    return render_template('books_list.html', books=books, category=language), 200

@book_blueprint.route('/book/<literature>/<bookname>/')
def book_detail(literature, bookname):
    book = next((book for item in all_books if item["literature"] == literature for book in item["books"] if book["name"] == bookname), None)
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    return render_template('book_detail.html', book=book), 200



