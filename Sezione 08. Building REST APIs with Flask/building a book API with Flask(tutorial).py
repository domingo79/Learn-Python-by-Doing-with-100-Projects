from flask import Flask
from pathlib import Path
import json
BASE_DIR = Path(__file__).resolve().parent
JSON_BOOK = BASE_DIR / "books.json"

app = Flask(__name__)

with open(JSON_BOOK, "r") as file:
    books = json.load(file)


@app.route("/")
def index():
    return "<h1>Home Page</h1>"


@app.route('/books/<book_id>')
def get_book(book_id):
    book = books.get(book_id)
    if book:
        return book
    else:
        return {'message': "Book not found"}, 404


app.run(debug=True)
