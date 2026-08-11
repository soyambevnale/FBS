print("Program to Find the Roots of a Quadratic Equation")

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

D = b*b - 4*a*c

root1 = (-b + D**0.5) / (2*a)
root2 = (-b - D**0.5) / (2*a)

print("Quadratic root1 is:", root1)
print("Quadratic root2 is:", root2)