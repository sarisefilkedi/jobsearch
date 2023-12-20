from flask import Flask, jsonify, json, request

with open('all_books.json') as f:
    all_books = json.load(f)

app = Flask(__name__)

@app.route("/")
def hello():
	return "<h1>Hello, welcome to the Can I Borrow World full of Books in all languages (work in progress)!</h1>"

@app.route('/books/', methods=['GET'])
def get_books():
	return jsonify(all_books)

@app.route('/books/languages/', methods=['GET'])
def get_language():
	response = [item["language"] for item in all_books]
	return jsonify(response)

@app.route('/books/literatures/', methods=['GET'])
def get_literature():
	response = [item["literature"] for item in all_books]
	return jsonify(response)

@app.route('/books/by_literature/<literature>/', methods=['GET'])
def get_books_by_literature(literature):
        books = [lite['books'] for lite in all_books if lite['literature'] == literature]
        if len(books)==0:
                return jsonify({'error':'literature not found!'}), 404
        else:
                response = [book['name'] for book in books[0]]
                return jsonify(response), 200

@app.route('/books/by_language/<language>/', methods=['GET'])
def get_books_by_language(language):
        books = [lang['books'] for lang in all_books if lang['language'] == language]
        if len(books)==0:
                return jsonify({'error':'language not found!'}), 404
        else:
                response = [book['name'] for book in books[0]]
                return jsonify(response), 200

@app.route('/books_by_literature/<literature>/<bookname>', methods=['GET','DELETE'])
def get_desc_by_lite_and_name(literature, bookname):
	books = [lite['books'] for lite in all_books if lite['literature'] == literature]
	if len(books)==0:
		return jsonify({'error':'literature not found!'}), 404
	else:
		desc = [book['description'] for book in books[0] if book['name'] == bookname]
	if len(desc)==0:
		return jsonify({'error':'book not found!'}), 404
	else:
		return jsonify(desc[0]), 200

@app.route('/books_by_language/<language>/<bookname>', methods=['GET'])
def get_desc_by_lang_and_name(language, bookname):
        books = [lang['books'] for lang in all_books if lang['language'] == language]
        if len(books)==0:
                return jsonify({'error':'language not found!'}), 404
        else:
                desc = [book['description'] for book in books[0] if book['name'] == bookname]
        if len(desc)==0:
                return jsonify({'error':'book not found!'}), 404
        else:
                return jsonify(desc[0]), 200

@app.route('/genres_by_literature/<literature>/', methods=['GET'])
def get_genre_by_lite(literature):
        books = [gen['books'] for gen in all_books if gen['literature'] == literature]
        if len(books)==0:
                return jsonify({'error':'literature not found!'}), 404
        else:
                response = [(book['name'],book['genre']) for book in books[0]]
                return jsonify(response), 200

@app.route('/writers_by_literature/<literature>', methods=['GET'])
def get_writers_by_literature(literature):
        books = [wr['books'] for wr in all_books if wr['literature'] == literature]
        if len(books)==0:
                return jsonify({'error':'literature not found!'}), 404
        else:
                response = [(book['writer'],book['name']) for book in books[0]]
                return jsonify(response), 200

@app.route("/books", methods=["POST"])
def create_a_literature():
	if not request.json or not "literature" in request.json:
		return jsonify({"error":"the new literature needs to have literature and language info"}), 400
	new_literature = {
		"literature": request.json["literature"],
		"language": request.json["language"],
		"books": request.json.get("books","")
	}
	all_books.append(new_literature)
	return jsonify({"message":"new literature created:/books/{}".format(new_literature["literature","language"])}), 201

@app.route("/books/literature/<literature>/", methods=["POST"])
def create_a_book(literature):
	if not request.json or not "language" in request.json:
		return jsonify({"error":"the new record needs to have language info"}), 400
	new_book = {
		"language": request.json["language"],
		"books": request.json.get("books", "")
	}
	all_books.append(new_book)
	return jsonify({"message":"new book created: /books/literature{}".format(new_book["language"])}), 201

@app.route('/books/<literature>', methods=['DELETE'])
def delete_a_literature(literature):
	matching_literature = [lite for lite in all_books if lite['literature'] == literature]
	if len(matching_literature)==0:
		return jsonify({'error':'literature not found!'}), 404
	all_books.remove(matching_literature[0])
	return jsonify({'success': True})

@app.route('/books_by_literature/<literature>/<bookname>', methods=['DELETE'])
def delete_a_book(literature, bookname):
	if [lite for lite in all_books if lite['literature'] == literature]:
		matching_book = [book['name'] for book in books[0] if book['name'] == bookname]
	if len(matching_book)==0:
		return jsonify({'error':'book not found!'}), 404
	all_books.remove(matching_book[0])
	return jsonify({'success': True})

@app.route('/books_by_name/<literature>/<bookname>', methods=['DELETE'])
def delete_the_book(literature, bookname):
	matching_literature = [lite for lite in all_books if lite['literature'] == literature]
	if len(matching_literature)==0:
		return jsonify({'error':'literature not found!'}), 404
	else:
		name = [book['name'] for book in books[0] if book['name'] == bookname]
		if len(name)==0:
			return jsonify({'error':'bookname not found!'}), 404
		else:
			all_books.remove(matching_book[0])
			return jsonify({'success': True})

@app.route('/book_search/<literature>/<bookname>', methods=['GET'])
def search_a_book_by_literature(literature, bookname):
	books = [lite['books'] for lite in all_books if lite['literature'] == literature]
	if len(books)==0:
		return jsonify({'error':'literature not found!'}), 404
	else:
		name = [book['name'] for book in books[0] if book['name'] == bookname]
		if len(name)==0:
			return jsonify({'error':'bookname not found!'}), 404
		else:
			return jsonify(name[0]), 200
