from empManage import empManage
class Main:
    @staticmethod
    def login():
        userid=input("Enter user_id = ")
        passwrd=input("Eneter Password =")
        
        if userid=='admin' and passwrd=='1234':
            print("Log is in done .") 
            return True
        else:
            print("Invalid Credentials .")
    
    def menu(self):
        em=empManage()
        while True:
            print(" 1 . Add Employee")
            print(" 2 . Display Employee")
            print(" 3 . Search Employee")
            print(" 4 . Update Employee")
            print(" 5 . Delete Employee")
            print(" 6 . Exit ")
        
            choice=int(input("Enter your choice to perform your operation = "))
            if choice==1:
                em.addEmp()
            elif choice==2:
                em.displayEmp()
            elif choice==3:
                em.searchEmp()
            elif choice==4:
                em.updateEmp()
            elif choice==5:
                em.deleteEmp()
            elif choice==6:
                print("Thank you for exit .")
                break
            else:
                print("Invalid choice .")
       
res=Main.login()
if res:
    m=Main()
    m.menu()