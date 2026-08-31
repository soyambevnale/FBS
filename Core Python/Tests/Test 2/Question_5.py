p1 = float(input("Enter price of product 1: "))
p2 = float(input("Enter price of product 2: "))
p3 = float(input("Enter price of product 3: "))
p4 = float(input("Enter price of product 4: "))
p5 = float(input("Enter price of product 5: "))

total = p1 + p2 + p3 + p4 + p5

gst = total * 18 / 100

final_bill = total + gst

print("Total =", total)
print("GST =", gst)
print("Final Bill =", final_bill)