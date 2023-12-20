from flask import Blueprint, render_template, request, jsonify
import json

book_blueprint = Blueprint('books', __name__)

with open('all_books.json') as f:
    all_books = json.load(f)

# Route for languages
@book_blueprint.route('/languages/')
def get_language():
    languages = list(set([item["language"] for item in all_books]))
    return render_template('languages.html', languages=languages)

# Route for literatures
@book_blueprint.route('/literatures/')
def get_literature():
    literatures = list(set([item["literature"] for item in all_books]))
    return render_template('literatures.html', literatures=literatures)

# Route to view books by literature
@book_blueprint.route('/by_literature/<literature>/')
def get_books_by_literature(literature):
    books = [lite['books'] for lite in all_books if lite['literature'] == literature]
    if len(books) == 0:
        return 'Literature not found', 404
    return render_template('books_by_literature.html', books=books[0], literature=literature)

# Route to view books by language
@book_blueprint.route('/by_language/<language>/')
def get_books_by_language(language):
    books = [lang['books'] for lang in all_books if lang['language'] == language]
    if len(books) == 0:
        return 'Language not found', 404
    return render_template('books_by_language.html', books=books[0], language=language)

# Route to get book description by literature and name
@book_blueprint.route('/description/literature/<literature>/<bookname>/')
def get_desc_by_lite_and_name(literature, bookname):
    books = [lite['books'] for lite in all_books if lite['literature'] == literature]
    if len(books) == 0:
        return 'Literature not found', 404
    book = next((book for book in books[0] if book['name'] == bookname), None)
    if not book:
        return 'Book not found', 404
    return render_template('book_description.html', book=book, literature=literature)

# Route to get book description by language and name
@book_blueprint.route('/description/language/<language>/<bookname>/')
def get_desc_by_lang_and_name(language, bookname):
    books = [lang['books'] for lang in all_books if lang['language'] == language]
    if len(books) == 0:
        return 'Language not found', 404
    book = next((book for book in books[0] if book['name'] == bookname), None)
    if not book:
        return 'Book not found', 404
    return render_template('book_description.html', book=book, language=language)


