from db.run_sql import run_sql

from models.book import Book
import repositories.author_repository as author_repository

def save(book):
    sql = """
    INSERT INTO books (title, author_id)
    VALUES (%s, %s)
    RETURNING id
    """
    values = [book.title, book.author.id]
    insertion = run_sql(sql, values)
    book.id = insertion[0]['id']
    return book

def select_all():
    sql = "SELECT * FROM books"
    selection = run_sql(sql)
    return [Book(
        book['title'],
        author_repository.select(book['author_id']),
        book['id']
        ) for book in selection]

def select(id):
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    selection = run_sql(sql, values)[0]

    if selection is not None:
        return Book(
            selection['title'],
            author_repository.select(selection['author_id']),
            selection['id']
            )
    else:
        return None

def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)

def update(book):
    sql = """
    UPDATE books
    SET (title, author_id) = (%s, %s)
    WHERE id = %s
    """
    values = [book.title, book.author.id, book.id]
    run_sql(sql, values)
