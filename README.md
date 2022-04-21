# What's this then?
It's a practice exercise to get used to setting up a Python web application that accesses data from an SQL database. It was assigned as part of a software development course.
This one was worked through as a paired exercise, so a lot of it was written by [AbiJays](https://github.com/AbiJays), who has her own fork that she'll presumably mess around with on her own (as I'll do with this one).

# What does it do?
Very little! It's just a practically nonexistent home page, a page that contains a list of books (which have authors assigned to them as attributes), and pages for each book.
Books can be added, edited, and deleted from the database via the web interface.

A major limitation of this right now is that you can only add books by authors that are already in the database in the first place, mostly because I couldn't identify an elegant way of doing that with the tools I had in the moment (I know it can be done the way I want in Javascript, but this is purely Python, HTML, PostgreSQL, and some CSS). It's dumb. I know. I might fiddle with it once I learn something that would enable it to be done how I'd like. Probably not.

I also haven't yet written any CSS for it whatsoever so have some eye bleach at the ready.

This heavily relies upon the [Flask](https://palletsprojects.com/p/flask/) web framework and [jinja2](https://palletsprojects.com/p/jinja/) HTML templating. It uses [Psycopg](https://www.psycopg.org/) to allow [PostgreSQL](https://www.postgresql.org/) database syntax to be accessible to a [Python](https://www.python.org/) front end.
