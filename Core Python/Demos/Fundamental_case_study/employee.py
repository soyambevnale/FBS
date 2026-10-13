def add():
    while True:
        id = input("Enter ID: ")

        if id.isdigit():
            if id not in emp_details:
                break
            else:
                print("Employee ID already available!")
        else:
            print("ID must contain digits only!")
            
    while True:
        name = input("Enter Name: ")

        if name.replace(" ", "").isalpha():
            break
        else:
            print("Please enter alphabets only!")

    while True:
        dept = input("Enter Department: ")

        if dept.replace(" ", "").isalpha():
            break
        else:
            print("Please enter alphabets only!")
            
    while True:
        salary = input("Enter Salary: ")

        if salary.replace(".", "", 1).isdigit() and salary != ".":
            if float(salary) > 0:
                salary = float(salary)
                break
            else:
                print("Salary must be greater than zero!")
        else:
            print("Please enter a valid salary!")
    
    if id not in emp_details:
        emp_details[id]=[id,name,dept,salary]
        return "Employee added successfully "
    else:
        return "Employee ID already available "
    


def update():
    id = input("Enter ID: ")
    emp_record = emp_details.get(id)

    if emp_record:
        while True:
            new_name = input(
                f"Enter new name ({emp_record[1]}): "
            ) or emp_record[1]

            if new_name.replace(" ", "").isalpha():
                break
            else:
                print("Please enter alphabets only!")

        while True:
            new_dept = input(
                f"Enter new department ({emp_record[2]}): "
            ) or emp_record[2]

            if new_dept.replace(" ", "").isalpha():
                break
            else:
                print("Please enter alphabets only!")

        while True:
            sal = input(
                f"Enter new salary ({emp_record[3]}): "
            )

            if sal == "":
                new_sal = emp_record[3]
                break

            elif sal.replace(".", "", 1).isdigit() and sal != ".":
                if float(sal) > 0:
                    new_sal = float(sal)
                    break
                else:
                    print("Salary must be greater than zero!")
            else:
                print("Please enter a valid salary!")

        emp_details[id] = [id, new_name, new_dept, new_sal]
        return "Employee updated successfully"

    else:
        return "ID not found"


def delete():
    id=input("Enter ID : ")
    if id in emp_details:
        print('''Enter choice that you want to delete ..
            1 : Delete Name
            2 : Delete Department
            3 : Delete Salary
            4 : Delete complete record''')
        ch=input("Enter choice : ")
        if ch=='1':
            emp_details[id][1]=''
            print("Name deleted successfully")
        elif ch=='2':
            emp_details[id][2]=''
            print("Department deleted successfully")
        elif ch=='3':
            emp_details[id][3]=''
            print("Salary deleted successfully")
        elif ch=='4':
            confirm=input("Are you want to delete complete record (yes / no ) : ")
            if confirm.lower()=='yes':
                del emp_details[id]
                print("Record deleted successfully")
            else:
                print("Deletion cancelled")
        else:
            print("Invalid Choice")
    else:
        print("ID not found")


def search():
    id=input("Enter ID : ")
    if id in emp_details:
        print(f'''Employee Found Successfully
                1 : ID         : {emp_details[id][0]}
                2 : Name       : {emp_details[id][1]}
                3 : Department : {emp_details[id][2]}
                4 : Salary     : {emp_details[id][3]}''')
    else:
        print("ID not found")

def show():
    if not emp_details:
        print("No employee records available")
    else:
        for id, record in emp_details.items():
            print("-------------------------")
            print("ID         :", record[0])
            print("Name       :", record[1])
            print("Department :", record[2])
            print("Salary     :", record[3])

def emp_manage():
    ch=0
    while(ch!='6'):
        print()
        print("            ###  Employee management  ###                   ")
        print('''Please select options from below ...!
                1 : Add Employee
                2 : Update Employee
                3 : Delete Employee
                4 : Search Employee
                5 : Show all Employees
                6 : Logout''')
        ch=input("Enter choice : ")
        if ch=='1':
            print(add())
        elif ch == '2':
            result = update()
            if result:
                print(result) 
        elif ch=='3':
            delete()
        elif ch=='4':
            search()
        elif ch=='5':
            show()
        elif ch=='6':
            print("Logout")
        else:
            print("Invalid choice ...")
            
        
        
def login():
    print("-----------------------------------------------")
    print("            ###  Login Page  ###                   ")
    print("-----------------------------------------------")
    uid='admin'
    pwd='1234'
    username=input("Enter username : ")
    password=input("Enter Password : ")
    if uid==username and pwd==password:
        emp_manage()
    else:
        print("Invalid Credentials ..")
        
emp_details={}
ch=0
while(ch!='2'):
    print()
    print('''Please select options from below ...!
            1 : Login
            2 : Exit ''')
    ch=input("Enter your choice : ")
    if ch=='1':
        login()
    elif ch=='2':
        print("Thank you for choosing us !!")
    else:
        print("Invalid choice ... ")