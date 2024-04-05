import Managment
from Library import books
from Account import *

def auth(name):
  Id[name] = input("Enter your Password : ")
  f = open("Account.py","w")
  issued_books[name] = []
  f.write(f"Id = {Id}\nissued_books = {issued_books}")
  f.close()

def User():
  name = input("Enter your user name : ")
  if name == "":
    print("enter name or Quit --> Q")
    User()
  if name == "Q":
    return 0
  if name not in set(Id):    
    auth(name)
    return name
  else:
    password = input("Verify your password : ")
    return name if password == Id[name] else User()
  
user = User()




while user:
  if user == "Admin":
    print("1. Display all books")
    print("2. Add a book")
    print("3. Delete a book")
    print("7. Exit")
  else : 
    print("1. Display all books")
    print("4. Issue a book")
    print("5. Return a book")
    print("6. My book")
    print("7. Exit")

  value = int(input("Enter your choice: "))
  print()

  if value == 1:
    Managment.display(books)

  elif value == 2 and user == "Admin":
    Managment.addBook()

  elif value == 3 and user == "Admin":
    Managment.deleteBook()

  elif value == 4:
    Managment.issueBook(user)

  elif value == 5:
    Managment.returnBook(user)

  elif value == 6:
    Managment.myBook(user)
    
  elif value == 7:
    print("Thanks for using our software...")
    break
  else:
    print("Invalid Input. Please Try Again!")

  print("=" * 20 + " RESTART " + "=" * 20)
