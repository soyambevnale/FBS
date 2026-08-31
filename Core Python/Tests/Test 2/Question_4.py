length = float(input("Enter length of wall: "))
height = float(input("Enter height of wall: "))
rate = float(input("Enter painting cost per sq.m: "))

area = 4 * length * height

total_cost = area * rate

print("Total painting area =", area, "sq.m")
print("Total painting cost =", total_cost, "Rs")