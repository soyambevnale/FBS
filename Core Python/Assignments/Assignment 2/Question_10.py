print("Reverse a Three-Digit Number")

num = int(input("Enter a three-digit number: "))

digit1 = num // 100
digit2 = (num // 10) % 10
digit3 = num % 10

reverse = (digit3 * 100) + (digit2 * 10) + digit1

print(f"Reverse number is: {reverse}")