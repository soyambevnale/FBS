class emp:
    def __init__(self,nm):
        self.nm=nm
    def display(self):
        print("Display")
        
class hr(emp):
    def display(self):
        print("HR display")
        
h1=hr("Rohit")
h1.display()
s1=emp("Sachin")
s1.display()