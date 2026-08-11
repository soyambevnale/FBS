print("Calculate selling price of Book")
cost_price=float(input("Enter cost price of Book : "))
discount=float(input("Enter discount (%)  : "))
discount_amount=(cost_price*discount)/100
selling_price=(cost_price-discount_amount)
print(f"Discount amount : {discount_amount}")
print(f"Selling price of Book : {selling_price}")