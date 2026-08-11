print("To calculate profit or loss.")
cost_price=int(input("Enter cost price :"))
selling_price=int(input("Enter selling price :"))
if(cost_price<selling_price):
    profit=selling_price-cost_price
    print(f"Profit ={profit}")
elif(selling_price<cost_price):
    loss=cost_price-selling_price
    print(f"Loss ={loss}.")
else:
    print("No profit , No loss .")
    
    