class placed_student:
    inName="FBS"
    stdCount=0
    @staticmethod
    def getInName():
        return placed_student.inName
    @staticmethod
    def setInName(nm):
        placed_student.inName=nm
    def __init__(self,FRN,name,batch):
        self.frn=FRN
        self.name=name
        self.batch=batch
        placed_student.stdCount+=1
        
    def display(self):
        print(f"Roll No : {self.frn}  ,  Name : {self.name}  ,  batch  :{self.batch}  , Institute name :{self.inName}")
        
s1=placed_student(12,"Suraj","JulyPython")
s2=placed_student(13,"Swaraj","JulyPython")
s3=placed_student(1,"Suhan","JulyPython")
s1.display()
s2.display()
# s1.inName="firstbit"
# placed_student.inName="FirstBit"
s3.display()
print(placed_student.stdCount)

# Name
# frn

        