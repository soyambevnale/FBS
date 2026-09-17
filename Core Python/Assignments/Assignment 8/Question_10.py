# 10. Write a program to check if entered year is a leap year or not.
# without passing parameter without returning value
def leap():
    year=2024
    if year%400==0 or (year%4==0 and year%100!=0):
        print("leap year .")
    else:
        print("Not leap year .")
leap()

# with passing parameter without returning value
def leap(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        print("leap year .")
    else:
        print("Not leap year .")

y=int(input("Enter year :"))
leap(y)

# without passing parameter with returning value
def leap():
    year=2024
    if year%400==0 or (year%4==0 and year%100!=0):
        return True
    else:
        return False
    
res=leap()
if res:
    print("Leap year .")
else:
    print("Not leap year .")
    
# with passing parameter with returning value
def leap(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        return True
    else:
        return False
    
y=int(input("Enter year ."))
res=leap(y)
if res:
    print("Leap year .")
else:
    print("Not leap year .")