# 1. Create a class Book with members as bid,bname,price and author.Add following methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook

class book:
    def __init__(self,bid=1,bname="life_not_easy",price=100,author="soyamm"):
        self.id=bid
        self.name=bname
        self.price=price
        self.author=author
        
    def __del__(self):
        print("Object id destroyed ")
        
    def showbook(self):
        print("Book Id : ",self.id)
        print("Book Name : ",self.name)
        print("Book Price : ",self.price)
        print("Book Author : ",self.author)
        
print("Without parameter ")
obj1=book()
obj1.showbook()

print("++++++++++++++++++++++++++++++++++++")
print("With parameter")
obj2=book(2,"alone",200,"soyam")
obj2.showbook()
    