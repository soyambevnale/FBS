# 1. Using Modules concept
# Create a class to store book details (bid, name, price and author).
# Write a menu driven program with following options:
# a. Add Book
# b. Delete book by id
# c. Display all books
# d. Search book by id
# Use dictionary to store all information.

from class_book import book

b=book()
ch=0
while True:
    print("1 : add")
    print("2 : Delete")
    print("3 : Display")
    print("4 : Search")
    print("5 : Exit")
    ch=input("Enter your choice :")
    
    if ch=="1":
        b.add()
    elif ch=="2":
        b.delete()
    elif ch=="3":
        b.display()
    elif ch=="4":
        b.search()
    elif ch=='5':
        print("Thank you")
        break
    else:
        print("Invalid choice")
        
    
        
        