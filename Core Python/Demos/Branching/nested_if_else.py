gender=input("Enter gender (F/M) : ")
age=int(input("Enter age : "))
if(gender=='F'):
    if(age>=18):
        print("Girl is eligible to marriage . ")
    else:
        print("Pehle padh lo")
else:
    if(age>=21):
        print("Boy is eligible for marriage .")
    else:
        print("Pehle kama lo .")