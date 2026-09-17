class emp:
    def __init__(self,nm):
        self.nm=nm
    def display(self):
        print("Display")
        
# emp ends here ...........................

class dev(emp):
    def display(self):
        print("A am from developer")
        
# dev ends here .............
        
class hr(emp):
    def display(self):
        print("HR display")


# hr ends here .............................

class juniorHr(hr):
    def display(self):
        print("A am from junior hr ...")

# junior hr ends here ................

class seniorHr(hr):
    def display(self):
        print("I am from senior hr ")
        
# senior hr ends here .....................

class juniorDev(dev):
    def display(self):
        print("I am from junior developer ")
        
# junior developer ends ere .................    

h1=hr("Rohit")
h1.display()
s1=emp("Sachin")
s1.display()
jr=juniorHr("Smriti")
jr.display()
jdev=juniorDev("Suryansh")
jdev.display()
