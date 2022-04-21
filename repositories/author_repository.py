from db.run_sql import run_sql

from models.author import Author

def save(author):
    sql = """
    INSERT INTO authors (first_name, last_name)
    VALUES (%s, %s)
    RETURNING id
    """
    values = [
        author.first_name,
        author.last_name
        ]
    insertion = run_sql(sql, values)
    author.id = insertion[0]['id']
    return author

def select_all():
    sql = "SELECT * FROM authors"
    selection = run_sql(sql)
    return [Author(
        author['first_name'],
        author['last_name'],
        author['id']
        ) for author in selection]

def select(id):
    sql = "SELECT * FROM authors WHERE id = %s"
    values = [id]
    selection = run_sql(sql, values)[0]
    if selection is not None:
        return Author(
            selection['first_name'],
            selection['last_name'],
            selection['id']
        )

def delete_all():
    sql = "DELETE FROM authors"
    run_sql(sql)
