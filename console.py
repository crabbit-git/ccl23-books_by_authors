from models.author import Author
from models.book import Book
import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

author_repository.delete_all()
book_repository.delete_all()

author1 = Author("Patrick", "Rothfuss")
author_repository.save(author1)
print(f"{author1.first_name} {author1.last_name} has an id of {author1.id}")

author2 = Author("N.K.", "Jemisin")
author_repository.save(author2)
print(f"{author2.first_name} {author2.last_name} has an id of {author2.id}")

authors = author_repository.select_all()

book1 = Book("The Name of the Wind", author1)
book_repository.save(book1)
print(f"{book1.title} has an id of {book1.id}")

book2 = Book("The Fifth Season", author2)
book_repository.save(book2)
print(f"{book2.title} has an id of {book2.id}")

breakpoint()