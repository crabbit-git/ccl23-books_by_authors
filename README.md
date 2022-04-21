# What's this then?
It's a practice exercise to get used to setting up a Python web application that accesses data from an SQL database. It was assigned as part of a software development course.
This one was worked through as a paired exercise, so a lot of it was written by [AbiJays](https://github.com/AbiJays), who has her own fork that she'll presumably mess around with on her own (as I'll do with this one).

# What does it do?
Very little! It's just a practically nonexistent home page, a page that contains a list of books (which have authors assigned to them as attributes), and pages for each book.
Books can be added, edited, and deleted from the database via the web interface.

This heavily relies upon [the Flask](https://palletsprojects.com/p/flask/) web framework and [jinja2](https://palletsprojects.com/p/jinja/) HTML templating. It uses [Psycopg](https://www.psycopg.org/) to allow [PostgreSQL](https://www.postgresql.org/) database syntax to be accessible to a [Python](https://www.python.org/) front end.
