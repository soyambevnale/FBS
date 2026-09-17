class mechanical:
    def display(self):
        print("I am from mechanical ")
        
class electric:
    def display(self):
        print("I am from electronics ")
        
# class mecatronix(mechanical,electric):
#     def display(self):
#         print("I am from mecatronix ")
        
class mecatronix(mechanical,electric):
    def abc(self):
        print("I am from mecatronix ")
        
c1=mecatronix()
c1.display()