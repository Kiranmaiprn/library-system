# app.py
from flask import Flask, request, jsonify
from models import Book, EBook, Library

app = Flask(__name__)
library = Library()

@app.route('/add_book', methods=['POST'])
def add_book():
    data = request.json
    try:
        title = data['title']
        author = data['author']
        isbn = data['isbn']
        file_format = data.get('file_format')

        if not isbn or not isbn.isdigit():
            raise ValueError('ISBN must be a valid number.')

        if file_format:
            new_book = EBook(title, author, isbn, file_format)
        else:
            new_book = Book(title, author, isbn)

        library.add_book(new_book)
        return jsonify({'message': 'Book added successfully.'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/list_books', methods=['GET'])
def list_books():
    return jsonify({'books': library.list_books()})

@app.route('/search_book', methods=['GET'])
def search_book():
    title = request.args.get('title')
    result = library.search_book(title)
    return jsonify({'result': result})

@app.route('/delete_book', methods=['DELETE'])
def delete_book():
    data = request.json
    try:
        isbn = data['isbn']
        if not isbn or not isbn.isdigit():
            raise ValueError('ISBN must be a valid number.')

        library.delete_book(isbn)
        return jsonify({'message': 'Book deleted successfully.'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True, port=3000)
