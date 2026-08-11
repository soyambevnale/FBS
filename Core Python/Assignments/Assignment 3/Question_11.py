print("Accept age of five people and also per person ticket amount and then calculate total amount to ticket to travel .")
total=0
age=int(input("Enter age of person 1:"))
ticket=int(input("Enter ticket of person 1 :"))
if(age<12):
    amount=ticket-(ticket*30/100)
elif(age>50):
    amount=ticket-(ticket*50/100)
else:
    amount=ticket
total=total+amount

age=int(input("Enter age of person 2:"))
ticket=int(input("Enter ticket of person 2 :"))
if(age<12):
    amount=ticket-(ticket*30/100)
elif(age>50):
    amount=ticket-(ticket*50/100)
else:
    amount=ticket
total=total+amount

age=int(input("Enter age of person 3:"))
ticket=int(input("Enter ticket of person 3 :"))
if(age<12):
    amount=ticket-(ticket*30/100)
elif(age>50):
    amount=ticket-(ticket*50/100)
else:
    amount=ticket
total=total+amount

age=int(input("Enter age of person 4:"))
ticket=int(input("Enter ticket of person 4 :"))
if(age<12):
    amount=ticket-(ticket*30/100)
elif(age>50):
    amount=ticket-(ticket*50/100)
else:
    amount=ticket
total=total+amount

age=int(input("Enter age of person 5:"))
ticket=int(input("Enter ticket of person 5 :"))
if(age<12):
    amount=ticket-(ticket*30/100)
elif(age>50):
    amount=ticket-(ticket*50/100)
else:
    amount=ticket
total=total+amount

print(f"Total ticket is :{total}")


