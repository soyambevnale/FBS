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


#2 Write a program to calculate simple interest based on Principal, Rate and Time(SI = P*R*T/100)

principal=int(input("Enter principal:"))
rate=int(input("Enetr rate :"))
time=int(input("Enter time:"))

si=(principal*rate*time)/100

print(f"Simple Interest is:{si}")


#3 Write a program to accept distance in km and convert it into meters and centimeters both.

km=int(input("Enter Distance in km:"))

meter=km*1000
centimeters=km*10000

print(f"Distance in meter:{meter}")
print(f"Distance in centimeters:{centimeters}")

#4. Calculate the cost of painting the following building’s walls (both interior and exterior). You need to accept area (one wall) and cost of both interior and exterior wall.
# (Note: 1. Below diagram is of two joint rooms.
# 2. It is upper view of building.)

area = float(input("Enter area of one wall: "))
interior_cost = float(input("Enter cost of interior wall: "))
exterior_cost = float(input("Enter cost of exterior wall: "))

interior_total = area * 2 * interior_cost
exterior_total = area * 7 * exterior_cost

total_cost = interior_total + exterior_total

print(f"Interior painting cost = {interior_total}")
print(f"Exterior painting cost ={ exterior_total}")
print(f"Total painting cost = {total_cost}")