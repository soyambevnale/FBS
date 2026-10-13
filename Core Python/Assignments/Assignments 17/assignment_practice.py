# 1. Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook
# d. Add static variable count and also maintain count of objects created.\
    
class book:
    count=0
    def __init__(self,bid,bname,price,author):
        self.bid=bid
        self.bname=bname
        self.price=price
        self.author=author
        book.count+=1
    
    def getid(self):
        return self.bid
    def set_id(self,newid):
        self.bid=newid
        
    def getname(self):
        return self.bname
    def setname(self,newname):
        self.bname=newname
        
    def getprice(self):
        return self.price
    def setprice(self,newprice):
        self.price=newprice
        
    def getauthor(self):
        return self.author
    def setauthor(self,newauthor):
        self.author=newauthor
        
    def __str__(self):
        return f" Id : {self.bid} Name :{self.bname}  Price :{self.price}  Author:{self.author}count:{book.count}"
    
    def showbook(self):
        print(f" Id : {self.bid}  Name : {self.bname}  Price : {self.price}  Author : {self.author}")
        print("Count : ",book.count)
        
    # def __del__(self):
    #     print("Object destroyed")
        
b=book(1,"Abc",400,"soyam")
b1=book(2,"XYZ",500,"Soham")
print(b)
print(b1)
        