from flask import Blueprint, render_template, jsonify, request
from models import db, Book
import json
import requests
import requests_cache

requests_cache.install_cache('book_api_cache', backend='sqlite', expire_after=36000)
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
    return render_template('books_list.html', books=books, category=literature), 200

@book_blueprint.route('/language/<language>/')
def books_by_language(language):
    books = next((item["books"] for item in all_books if item["language"] == language), [])
    return render_template('books_list.html', books=books, category=language), 200

@book_blueprint.route('/book/<literature>/<bookname>/')
def book_detail(literature, bookname):
    book = next((book for item in all_books if item["literature"] == literature for book in item["books"] if book["name"] == bookname), None)
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    return render_template('book_detail.html', book=book), 200

@book_blueprint.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        data = request.json
        new_book = Book(
            name=data['name'],
            writer=data['writer'],
            genre=data['genre'],
            description=data['description'],
            literature=data['literature'],
            language=data['language']
        )
        db.session.add(new_book)
        db.session.commit()
        return jsonify({'message': 'Book added successfully'}), 201
    return render_template('add_book.html')

@book_blueprint.route('/booksummary/<bookname>', methods=['GET'])
def get_booksummary(bookname):
    wiki_url_template = 'https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles={book_name}'
    book_url = wiki_url_template.format(book_name=bookname)
    resp = requests.get(book_url)
    if resp.ok:
        return jsonify(resp.json())
    else:
        return jsonify({'error': resp.reason}), resp.status_code




