#1. Write a program to find the area and perimeter of following figure (Accept the length, breadth and radius from user:

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
radius = float(input("Enter radius: "))

pi = 3.14

rectangle_area = length * breadth
semicircle_area = (pi * radius * radius) / 2

area = rectangle_area + semicircle_area

perimeter = length + length + breadth + (pi * radius)

print(f"Area ={area}")
print(f"Perimeter ={perimeter}")