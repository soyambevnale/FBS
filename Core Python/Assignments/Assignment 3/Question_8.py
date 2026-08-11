print("Enter userid , password and catpcha for login .")
import random
name='soyambevnale'
passwrd='20051220'
userid=input("Enter userid :")
password=input("Enter password :")
if(name==userid and passwrd==password):
    captcha=random.randint(1000,9999)
    print("Captcha :",captcha)
    captcha_user=int(input("Enter captcha :"))
    if(captcha_user==captcha):
        print("Login successfully !!")
    else:
        print("Invalid Captcha .")
else:
    print("Invalid userid and password .")