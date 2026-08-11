#WAP to print Armstrong number within a given range 
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for num in range(start, end + 1):

    temp = num
    digits = 0

    while temp > 0:
        digits = digits + 1
        temp = temp // 10

    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + digit ** digits
        temp = temp // 10

    if total == num:
        print(num)