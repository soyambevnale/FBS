#2 Write a program to calculate simple interest based on Principal, Rate and Time(SI = P*R*T/100)

principal=int(input("Enter principal:"))
rate=int(input("Enetr rate :"))
time=int(input("Enter time:"))

si=(principal*rate*time)/100

print(f"Simple Interest is:{si}")