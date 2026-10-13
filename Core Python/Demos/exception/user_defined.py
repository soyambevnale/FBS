from myexception import Myexception
try:
    age=int(input("Enter the age : "))
    if age<=0:
        # m=Myexception(age)   #notebooklm   #geminilm
        raise Myexception(age)
    
except Myexception as m:
    print(m)
except Exception as e:
    print(e)