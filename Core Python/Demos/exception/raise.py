try:
    age=int(input("Enter age :"))
    if age<=0:
        raise ZeroDivisionError ("Enter valid age .")
    
except Exception as e :
    print(e)