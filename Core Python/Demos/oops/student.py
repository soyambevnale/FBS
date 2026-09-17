class student:
    inName="FBS"
    stdCount=0
    @staticmethod
    def getInName():
        return student.inName
    @staticmethod
    def setInName(nm):
        student.inName=nm
    def __init__(self,rollno,name,batch):
        self.rollno=rollno
        self.name=name
        self.batch=batch
        student.stdCount+=1
        
    def display(self):
        print(f"Roll No : {self.rollno}  ,  Name : {self.name}  ,  batch  :{self.batch}  , Institute name :{self.inName}")
        
s1=student(12,"Suraj","JulyPython")
s2=student(13,"Swaraj","JulyPython")
s3=student(1,"Suhan","JulyPython")
s1.display()
s2.display()
# s1.inName="firstbit"
# student.inName="FirstBit"
s3.display()
print(student.stdCount)

# Name
# frn

        