from flask import Blueprint, render_template, redirect, request

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository
from models.book import Book

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def books():
    return render_template(
        "books/index.html",
        books = book_repository.select_all()
        )

@books_blueprint.route("/books/add", methods=['GET'])
def add_book():
    return render_template(
        "books/add.html",
        authors = author_repository.select_all()
        )

@books_blueprint.route("/books", methods=['POST'])
def construct_book():
    title = request.form['title']
    author = author_repository.select(request.form['author_id'])
    book = Book(title, author)
    book_repository.save(book)
    return redirect("/books")

@books_blueprint.route("/books/<id>", methods=['GET'])
def book_details(id):
    return render_template(
        "books/detail.html",
        book = book_repository.select(id)
        )

@books_blueprint.route("/books/<id>/edit", methods=['GET'])
def edit_book(id):
    return render_template(
        "books/edit.html",
        book = book_repository.select(id),
        authors = author_repository.select_all()
        )

@books_blueprint.route("/books/<id>", methods=['POST'])
def update_book(id):
    title = request.form['title']
    author = author_repository.select(request.form['author_id'])
    book = Book(title, author)
    book_repository.update(book)
    return redirect("/books")

@books_blueprint.route("/books/<id>/delete", methods=['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect("/books")
