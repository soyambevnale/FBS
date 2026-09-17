# 9. Write a program to check if entered number is a palindrome or not. 
# without passing parameter without returning value
def palindrome():
    rev=0
    num=123
    temp=num
    while num>0:
        digit=num%10
        rev=rev*10+digit
        num=num//10
        
    if temp==rev:
        print("Number is palindrome .")
    else:
        print("Number is not palindrome .")

palindrome()

# with passing parameter without returning value
def palindrome(n):
    rev=0
    temp=n
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
        
    if temp==rev:
        print("Number is palindrome .")
    else:
        print("Number is not palindrome .")
        
num=int(input("Enter number :"))
palindrome(num)

# without passing parameter with returning value
def palindrome():
    rev=0
    num=121
    temp=num
    while num>0:
        digit=num%10
        rev=rev*10+digit
        num=num//10
    if temp==rev:
        return True
    else:
        return False

res=palindrome()
if res:
    print(f"palindrome number .")
else:
    print(f"not palindrome number .")

# with passing parameter with returning value
def palindrome(num):
    rev=0
    temp=num
    while num>0:
        digit=num%10
        rev=rev*10+digit
        num=num//10
        
    if temp==rev:
        return True
    else:
        return False
    
n=int(input("Enter number :"))
res=palindrome(n)
if res:
    print(f"palindrome number .")
else:
    print(f"not palindrome number .")