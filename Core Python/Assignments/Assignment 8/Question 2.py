## 2. Write a program to calculate area of circle
# without passing parameter without returning value

def aoc():
    r=3
    area=3.14*r*r
    print(f"Area of circle is = {area}.")
    
aoc()

# with passing parameter without returning value

def aoc(r):
    area=3.14*r**2
    print(f"Area of circle is = {area}.")
    
r=float(input("Enter radius of circle : "))
aoc(r)

# without passing parameter with returning value

def aoc():
    r=3
    area=3.14*r*r
    return area

res=aoc()
print(f"Area of circle is = {res}.")

# with passing parameter with returning value

def aoc(r):
    area=3.14*r**2
    return area

radius=float(input("Enter radius of circle:"))
res=aoc(radius)
print(f"Area of circle is = {res}.")
