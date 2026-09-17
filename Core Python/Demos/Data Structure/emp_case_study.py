def addEmp():
    pass
def delEmp():
    pass
def searchEmp():
    pass
def showAllEmp():
    pass
def 
def empManage():
    ch=0
    while (ch!='6'):
        print("#### EMPLOYEE MANAGEMENT ####")
        print('''Please select options from below ...
            1 : Add emp
            2 : Upd emp
            3 : Del emp
            4 : Search emp
            5 : Show all emp
            6 : Log out''')
        ch=input("Enter your choice :")
        if(ch=='1'):
            addEmp()
        elif(ch=='2'):
            updEmp()
        elif(ch=='3'):
            delEmp()
        elif(ch=='4'):
            searchEmp()
        elif(ch=='5'):
            showAllEmp()
        elif(ch=='6'):
            print("Logged out")
        else:
            print("Invalid choice")
        
        
def login():
    print('### LOGIN PAGE ###')
    uid='admin'
    passw='1234'
    username=input("Enter userid : ")
    password=input("Enter Password :")
    if(uid==username and passw==password):
        empManage()
    else:
        print("Invalid credentials ..! ")
ch=0
while ch!='2':
    print('''Please select options from below :
        1 . Login
        2 . Exit''')
    ch=input("Enter choice :")
    if(ch=='1'):
        login()
    elif(ch=='2'):
        print("Thank you for choosing us ..!")
    else:
        print("Invalid choice ...")