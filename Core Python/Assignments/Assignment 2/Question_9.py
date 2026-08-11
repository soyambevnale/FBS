print("Swap Two Numbers Without Using Third Variable")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Before swapping: num1 = {num1}, num2 = {num2}")

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print(f"After swapping: num1 = {num1}, num2 = {num2}")