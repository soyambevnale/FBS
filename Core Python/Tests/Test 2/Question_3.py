r = 20
l = 50
b = 40
cost_per_meter = 35

semicircle = 3.14 * r
rectangle = 2 * (l + b)

total_fencing = semicircle + rectangle

total_wire = total_fencing * 5

total_cost = total_wire * cost_per_meter

print("Total fencing =", total_wire, "m")
print("Total cost =", total_cost, "Rs")

