try:
    num1=int(input("Enter num1 :"))
    num2=int(input("Enter num 2 :"))
    print(num1//num2)
except ZeroDivisionError as a:
    print(f"I am in zero :",a)
except ValueError as v:
    print(f"Value error : {v}")
except Exception as e:
    print(e)
else:
    print("I am in else block")
finally:
    print("I am in finally block")
    
