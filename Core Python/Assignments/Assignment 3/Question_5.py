print("To check whether the triangle is equilateral, isosceles or scalene triangle. ")
side1=float(input("Enter side1:"))
side2=float(input("Enter side2:"))
side3=float(input("Enter side3:"))
if(side1+side2>side3 and side2+side3>side1 and side3+side1>side2):
    if(side1==side2==side3):
        print("Equilateral triangle .")
    elif(side1==side2 or side2==side3 or side3==side1):
        print("isosceles triangle .")
    else:
        print("scalene triangle .")
else:
    print("Invalid triangle .")