from Library import books
from Account import *
from Library import books

def display(books):
  count = 1
  for book in books:
    print(f"{count}. {book}")
    count += 1

# ========== Add a book


def addBook():
  book = input("Enter the name of the book: ")
  books.append(book)
  f = open("Library.py","w")
  f.write(f"books = {books}")
  f.close()
  print(book , "book has been added in the Library successfully!")


# ========= Delete a book


def deleteBook():
  display(books)

  n = int(input("Enter the id of the book: "))
  book = books.pop(n - 1)
  f = open("Library.py","w")
  f.write(f"books = {books}")
  f.close()
  print(book , "book has been deleted successfully!")


# ========= Issue a book


def issueBook(user):
  display(books)
  
  book_id = int(input("Enter the id of the book: "))
  issued_books[user] += [books[book_id-1]]
  f = open("Account.py","w")
  f.write(f"Id = {Id}\nissued_books = {issued_books}")
  f.close()
  
  # -------------- removing book from library --------------
  
  books.remove(books[book_id-1])
  f = open("Library.py","w")
  f.write(f"books = {books}")
  f.close()

  print("The book has been issued successfully!")


# ========= Return a book


def returnBook(user):
  print(issued_books)
  display(issued_books[user])
  book_id = int(input("Enter the id of the book: "))

  returnedBook = issued_books[user].pop(book_id-1)
  f = open("Account.py","w")
  f.write(f"Id = {Id}\nissued_books = {issued_books}")
  f.close()

  books.append(returnedBook)
  f = open("Library.py","w")
  f.write(f"books = {books}")
  f.close()
  print(returnedBook,"book has been returned successfully!")
