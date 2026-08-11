print("To check if person is eligible to marry or not")
gender=input("Enter gender in f/m format :")
age=int(input("Enter age :"))
if(gender=='f'):
    if(age>=18):
        print("Eligible")
    else:
        print("not eligible")
else:
    if(age>=21):
        print("Eligible")
    else:
        print("not eligible")
    