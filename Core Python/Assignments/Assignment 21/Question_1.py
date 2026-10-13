# 1. Develop a simple calculator program that performs basic arithmetic operations (+,
# -, *, /) on two numbers provided by the user. The program should ask the user for
# the numbers and the operator. However, the program should handle the following
# exceptions:
# a. Invalid Number: If the user enters a number that is not valid, catch the
# exception and display an error message.
# b. Invalid Operator: If the user enters an operator other than "+", "-", "*", or
# "/", catch the exception and display an error message.
# c. Division by Zero: If the user tries to divide by zero, catch the exception and
# display an error message.
# Write a program that performs the requested arithmetic operation and
# handles the exceptions as described above.
try:
    num1=int(input("Enter num 1 : "))
    num2=int(input("Enter num 2 : "))
except ValueError :
    print("Enter valid number ")
except Exception as e:
    print(e)
    
else: 
    try: 
        print("1 . + ( Addition ) ")
        print("2 . - ( Subtraction ) ")
        print("3 . * ( Multiplication )")
        print("4 . / ( Division ) ")
        print("5 . % ( Modulus ) ")
        choice=input("Enter operation you want to perform in operator format like + , - , * , / , % : ")
        if choice not in '+-*/%':
            raise Exception ("Operator not valid")
    
    except Exception as e:
        print(e)
    else:

        try:
            if num1==0 or num2==0 :
                if choice=='/':
                    raise ZeroDivisionError ("Enter valid number , you entered zero so zero can not be divide")
        except ZeroDivisionError as z:
            print(z)
        except Exception as e:
            print(e)
        
        else:
            def addition(num1,num2):
                add=num1+num2
                print("Addition is : ",add)

            def subtraction(num1,num2):
                sub=num1-num2
                print("Subtraction is : ",sub)
    
            def multiplication(num1,num2):
                mul=num1*num2
                print("Multiplication is : ",mul)
    
            def division(num1,num2):
                div=num1/num2
                print("Division is : ",div)
    
            def modulus(num1,num2):
                mod=num1%num2
                print("Modulus is : ",mod)

            if choice=='+':
                addition(num1,num2)
            elif choice=='-':
                subtraction(num1,num2)
            elif choice=='*':
                multiplication(num1,num2)
            elif choice=='/':
                division(num1,num2)
            elif choice=='%':
                modulus(num1,num2)
            else:
                print("Invalid choice ")
    