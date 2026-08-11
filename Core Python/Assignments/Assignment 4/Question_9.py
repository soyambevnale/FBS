print("print all numbers in a range divisible by a given number. ")

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
num = int(input("Enter divisor: "))

for i in range(start, end + 1):
    if i % num == 0:
        print(i)