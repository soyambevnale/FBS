#1
#print("Enter five subject marks .")
#marathi=int(input("Enter marks of Marathi : "))
#hindi=int(input("Enter marks of Hindi : "))
#math=int(input("Enter marks of Math : "))
#science=int(input("Enter marks of Science : "))
#history=int(input("Enter marks of History : "))
#result=(marathi+hindi+math+science+history)/500*100
#print(f"Percentage of five subjects is {result} % .")

#2
#print("Calculate area of rectangle .")
#length=float(input("Enter length : "))
#breadth=float(input("Enter breadth : "))
#a_o_r=length*breadth
#print(f"Area of Rectangle is {a_o_r} cm. ")

#3
#print("Fine quotient and remainder of two numbers .")
#num1=int(input("Enter number1:"))
#num2=int(input("Enter number2:"))
#quotient=num1/num2
#print(f"Quotient is {quotient} .")
#remainder=num1%num2
#print(f"Remainder is {remainder} .")

#4
#print("Calculate simple interest .")
#p=int(input("Enter principal :"))
#r=int(input("Enter rate :"))
#t=int(input("Enter time :"))
#si=(p*r*t)/100
#print(f"SI is {si} .")

#5
#print("Calculate compound interest .")
#p=int(input("Enter principal :"))
#r=int(input("Enter rate :"))
#t=int(input("Enter time :"))
#amount=p*((1+r/100)**t)
#ci=amount-p
#print(f"ci is {ci} .")

#6
#a1=int(input("Enter a1:"))
#a2=int(input("Enter a1:"))
#a3=180-(a1+a2)
#print(a3)

#7
#days=int(input("Enter days:"))
#year=days//365
#print(year)
#days=days%365
#weeks=days//7
#print(weeks)
#days=days%7
#print(days)

#9
#base=int(input("Enter base:"))
#height=int(input("Enter height"))
#aot=1/2*base*height
#print(aot)

#10
#a=float(input("Enter side"))
#aoet=(1.732/4)*(a**2)
#print(aoet)

#11
#r=float(input("Enter radius:"))
#aoc=3.14*r**2
#print(aoc)
#coc=2*3.14*r
#print(coc)

# for i in range(1,6):
#     for j in range(5,i-1,-1):
#         print(j, end=" ")
#     print()

# for i in range(1,6):
#     for j in range(6-i,6):
#         print(j, end=" ")
#     print()
    
# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(j, end=" ")
#     print()
    
# for i in range(1,6):
#     for j in range(1,7-i):
#         print(j, end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j, end=" ")
        
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j, end=" ") 
        
#     for j in range(1, 2 * i - 1):
#         print(" ", end=" ")
        
#     for j in range(5,5-i,-1):
#         print(j,end=" ")
#     print()

# for i in range(5):

#     for j in range(1,6-i):
#         print(j, end=" ")

#     for j in range(2 * i):
#         print(" ", end=" ")

#     for j in range(5,i,-1):
#         print(j, end=" ")

#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         if((i+j)%2==0):
#             print("*",end=" ")
#         else:
#             print("$",end=" ")
#     print()
    
# for i in range(1,6):
#     for j in range(1,i):
#             print(" ",end=" ")
      
#     for j in range(1,7-i):
#             print("*",end=" ")
#     print()

# k=7
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
      
#     for j in range(1,k+1):
#         print(" ",end=" ")
#     k-=2
            
#     for j in range(i,i+1):
#         if(i!=5 or j!=5):
#             print('*',end=" ")
            
#     print()

# for i in range(0,5):
#     for j in range(5,i,-1):
#         print(j,end=" ")
#     print()

# for i in range(1,6):
#     for j in range(5,5-i, -1):
#         print(j, end=" ")
#     print()

# num=1
# for i in range(1,6):
#     for j in range(i):
#         print(num,end=" ")
#         num+=1
#     print()

# for i in range(1,6):
#     for j in range(1,6-i):
#         print(" ",end=" ")
        
#     for j in range(1,i+1):
#         print("*",end=" ")
        
#     for j in range(1,i):
#         print("*",end=" ")
        
#     print()

# for i in range(1,6):
#     for j in range(5,5-i,-1):
#         print(j,end=" ")
        
#     print()

# for i in range(1,6):
#     for j in range(1,i):
#         print(" ",end=" ")
    
#     for j in range(1,7-i):
#         print(chr(64+i),end=" ")
        
#     print()

# userid='soyam'
# password='1234'

# for i in range(3):
#     uid=input("Enter Userid :")
#     pwd=input("Enter Password :")
    
#     if uid==userid and pwd==password:
#         print("Login Successfully !!")
#         break
#     else:
#         print("Invalid userid and password !!")   
    
# else:
#     print("3 attempts completed .")
    
# for i in range(1,6):
#     for j in range(1,6):
#         if i==5 or j==1 or i==j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
    
# for i in range(1,6):
#     for j in range(1,6):
#         if i==1 or j==1 or i+j==6:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

for i in range(1,5):
    for j in range(1,5):
        print(chr(64+j),end=" ")
    print()