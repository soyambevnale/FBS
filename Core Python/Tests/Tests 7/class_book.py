
class book:
    bookDetail={}
    def add(self):
        book_id=int(input("Enter book id = "))
        if book_id in book.bookDetail:
            print("Book id already exists .")
        else:
            book_name=input("Enter Name of Book = ")
            book_price=float(input("Enter the price = "))
            book_author=input("Enter author : ")
            
            book.bookDetail[book_id]={
                "Book_name" : book_name ,
                "Book_price" : book_price ,
                "Book_Author" : book_author
            }
            print("book added ")
    
    def delete(self):
        id=int(input("Enter id :"))
        if id in book.bookDetail:
            del book.bookDetail[id]
            print("Book deleted successfully .")
        else:
            print("Book is not available .")
            
    def display(self):
        if len(book.bookDetail)==0:
            print("There is no data  .")
        else:
            for i in book.bookDetail.values():
                print(i)
        
    def search(self):
        print("Search by id .")
        id=int(input("Enter id ="))
        if id in book.bookDetail:
            bk=book.bookDetail[id]
            print(bk)
        else:
            print("Book not found ")
