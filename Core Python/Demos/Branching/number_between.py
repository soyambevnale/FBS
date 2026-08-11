#if else ladder
num=int(input("Enter Number :"))
if(num<=0):
    print(f"{num} is less than 0 or equal to 0.")
elif(num<=50):
    print(f"{num} is between 1 to 50 .")
elif(num<=100):
    print(f"{num} is between 51 to 100 .")
elif(num<=150):
    print(f"{num} is between 101 to  150 .")
elif(num<=150):
    print(f"{num} is between 151 to 250 .")
else:
    print(f"{num} is above 250 .")
    
    
#nested if else   
num = int(input("Enter Number: "))

if num <= 0:
    print(f"{num} is less than or equal to 0.")
else:
    if num <= 50:
        print(f"{num} is between 1 to 50.")
    else:
        if num <= 100:
            print(f"{num} is between 51 to 100.")
        else:
            if num <= 150:
                print(f"{num} is between 101 to 150.")
            else:
                if num <= 250:
                    print(f"{num} is between 151 to 250.")
                else:
                    print(f"{num} is above 250.")
    
    