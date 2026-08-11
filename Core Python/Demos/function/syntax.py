def greet():                       #function definition
    print("Good Afternoon!")       #block of code

greet()                            #function call
greet()                        


#with parameter
def sum(a,b):
    add=a+b
    print(add)
    
sum(10,20)

#without parameter
a=10
b=20
def sum():
    add=a+b
    print(add)
sum()

#user input
def sum():
    num1=int(input("Enter num 1:"))
    num2=int(input("Enter num 2:"))
    add=num1+num2
    print(add)
sum()