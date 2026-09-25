from hr import Hr
from dev import Dev
from emp import Employee

class empManage:
    empDetail={}
    def addEmp(self):
        emp_id=int(input("Enter employee id = "))
        if emp_id in empManage.empDetail:
            print("Employee id already exists .")
        else:
            emp_name=input("Enter Name of Employee = ")
            emp_sal=float(input("Enter the salary = "))
            
            print(" 1 . Hr")
            print(" 2 . Dev")
            choice=int(input("Enter Choice = "))
            if choice==1:
                ecom=float(input("Enter com = "))
                emp=Hr(emp_id,emp_name,emp_sal,ecom)
            elif choice==2:
                ebonus=float(input("Enter bonus = "))
                emp=Dev(emp_id,emp_name,emp_sal,ebonus)
            else:
                print("Invalid choice .")
                return
            empManage.empDetail[emp_id]=emp
            print("Emp added ")
            
    def displayEmp(self):
        if len(empManage.empDetail)==0:
            print("Emp is not exist .")
        else:
            for var in empManage.empDetail.values():
                print(var)
        
    def searchEmp(self):
        print("Search by id .")
        eid=int(input("Enter id ="))
        if eid in empManage.empDetail:
            emp=empManage.empDetail[eid]
            print(emp)
        else:
            print("Employee Not found ")
        
    def updateEmp(self):
        id=int(input("Enter id = "))
        if id not in empManage.empDetail:
            print("Employee not exist .")
            return
        else:
            emp=empManage.empDetail[id]
            print("What you want to update ")
            print("1 . Hr")
            print("2 . Dev")
            ch=int(input("Enter choice : "))
            if ch==1 and isinstance(emp,Hr):
                print("1 . Update Name")
                print("2 . Update Salary")
                print("2 . Update com")
                choice=int(input("Enter choice : "))
                if choice==1:
                    newname=input("Enter name of hr :")
                    emp.setName(newname)
                elif choice==2:
                    newsal=float(input("Enter new salary : "))
                    emp.setSal(newsal)
                elif choice==3:
                    newcom=float(input("Enter new com : "))
                    emp.setCom(newcom)
                else:
                    print("Invalid choice .")
            elif ch==2 and isinstance(emp,Dev):
                print("1 . Update Name")
                print("2 . Update Salary")
                print("3 . Update com")
                choice=int(input("Enter choice : "))
                if choice==1:
                    newname=input("Enter name of Dev :")
                    emp.setName(newname)
                elif choice==2:
                    newsal=float(input("Enter new salary : "))
                    emp.setSal(newsal)
                elif choice==3:
                    newbonus=float(input("Enter new com : "))
                    emp.setCom(newbonus)
                else:
                    print("Invalid choice .")
            else:
                print("mismatched")
            
            
    
    def deleteEmp(self):
        eid=int(input("Enter id :"))
        if eid in empManage.empDetail:
            del empManage.empDetail[eid]
            print("Employee deleted successfully .")
        else:
            print("Employee is not available .")
        
    
        