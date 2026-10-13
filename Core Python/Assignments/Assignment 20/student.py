# 3. Create object of student class (Outside SY & TY package) having roll
# number, name, SYMakrs and TYMarks. Add the marksof SY and TY
# Computer subjects and calculate grade ("A" for >=70, "B" for >=60,
# "C" for >=50, “Pass Class” for >=40 else “Fail”) and display the result
# of the student in proper format.
from SY.sy import sy_marks
from TY.ty import ty_marks
class student:
    def __init__(self,roll_no,name,SYmarks,TYmarks):
        self.roll_no=roll_no
        self.name=name
        self.SYmarks=SYmarks
        self.TYmarks=TYmarks
        
    def display(self):
        total=0
        total=sy.computer+ty.theory
        # total = self.SYmarks.computer+self.TYmarks.theory
        
        print("Roll no : ",self.roll_no)
        print("Name : ",self.name)
        print("SY computer : ",sy.computer)
        print("TY compurt thoery : ",ty.theory)
        print("total marks : ",total)
        
        if total>=70:
            print("Grade : A")
        elif total>=60:
            print("Grade : B")
        elif total>=50:
            print("Grade : C")
        elif total>=40:
            print("Pass")
        else:
            print("Fail")
            


sy=sy_marks(50,50,50)
ty=ty_marks(30,30)
s=student(1,"Soyam",sy,ty)
s.display()

