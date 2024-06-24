from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson import ObjectId

app = Flask(_name_)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

# Insert a new book record
@app.route('/books', methods=['POST'])
def add_book():
    title = request.json['title']
    author = request.json['author']
    published_date = request.json['published_date']
    book_id = mongo.db.books.insert({'title': title, 'author': author, 'published_date': published_date})
    new_book = mongo.db.books.find_one({'_id': book_id})
    return jsonify({'result': new_book})

# Retrieve and return all book records
@app.route('/books', methods=['GET'])
def get_books():
    books = mongo.db.books.find()
    output = []
    for book in books:
        output.append({'title': book['title'], 'author': book['author'], 'published_date': book['published_date']})
    return jsonify({'result': output})

# Update a book record
@app.route('/books/<id>', methods=['PUT'])
def update_book(id):
    title = request.json['title']
    author = request.json['author']
    published_date = request.json['published_date']
    mongo.db.books.update_one({'_id': ObjectId(id)}, {'$set': {'title': title, 'author': author, 'published_date': published_date}})
    updated_book = mongo.db.books.find_one({'_id': ObjectId(id)})
    return jsonify({'result': updated_book})

# Delete a book record
@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    mongo.db.books.delete_one({'_id': ObjectId(id)})
    return jsonify({'result': 'Book deleted successfully'})

if _name_ == '_main_':
    app.run(debug=True)