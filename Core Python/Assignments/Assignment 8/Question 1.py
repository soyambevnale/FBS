#  1. Write a program to calculate area of rectangle
# without passing parameter without returning value

def aor():
    length=2
    breadth=3
    area=length*breadth
    print(f"Area of rectangle is ={area}.")
    
aor()

# with passing parameter without returning value

def aor(l,b):
    area=l*b
    print(f"Area of rectangle is ={area}.")
    
aor(2,4)

# without passing parameter with returning value

def aor():
    length=5
    breadth=6
    area=length*breadth
    return area

res=aor()
print(f"Area of rectangle is ={res}.")

# with passing parameter with returning value

def aor(l,b):
    area=l*b
    return area

l=float(input("Enter length of rectangle:"))
b=float(input("Enter breadth of rectangle:"))
res=aor(l,b)
print(f"Area of rectangle is ={res}.")