# Program to prompt user to enter userid and password. If Id and password is incorrect give him chance to re-enter the credentials. Let him try 3times. After that program to terminate. 

userid='soyam'
password='1234'
for i in range(3):
    uid=input("Enter Userid :")
    pwd=input("Enter Password :")
    
    if uid==userid and pwd==password:
        print("Login Successfully !!")
        break
    else:
        print("Invalid userid and password !!")   
    
else:
    print("3 attempts completed .")