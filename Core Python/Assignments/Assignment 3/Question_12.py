print("To check if given 3 digit number is a palindrome or not.")
num=int(input("Enter number :"))
first=num//100
last=num%10
if(first==last):
    print("Palindrome number .")
else:
    print("Not palindrome .")


# temp=num
# rev=0
# while(num>0):
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10

# if (temp==rev):
#     print("Palindrome number .")
# else:
#     print("Not palindrome .")