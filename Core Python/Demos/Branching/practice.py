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

# for i in range(1,5):
#     for j in range(1,5):
#         print(chr(64+j),end=" ")
#     print()

# cp=int(input("Enter cost price:"))
# sp=int(input("Enter selling price:"))
# if(sp>cp):
#     profit=sp-cp
#     print("profit:",profit)
# elif(cp>sp):
#     loss=cp-sp
#     print("Loss:",loss)
# else:
#     print("no profit,no loss")

# userid=input("Enter userid:")
# password=input("Enter password:")
# uid='soyam'
# pwd='1234'
# if(userid==uid and password==pwd):
#     print("Successfully login!!")
# else:
#     print("Invalid userid and password.")

# import random
# userid=input("Enter userid:")
# password=input("Enter password:")
# uid='soyam'
# pwd='1234'
# if(userid==uid and password==pwd):
#     captcha=random.randint(1000,9999)
#     print("Captcha:",captcha)
#     user_captcha=int(input("Enter captcha:"))
#     if (user_captcha==captcha):
#         print("Succefully login!")
#     else:
#         print("Incorrect captcha.")
# else:
#     print("Incorrect userid and password. ")
        
# sub1=int(input("Enter marks sub1:"))
# sub2=int(input("Enter marks sub2:"))
# sub3=int(input("Enter marks sub3:"))
# sub4=int(input("Enter marks sub4:"))
# sub5=int(input("Enter marks sub5:"))
# total=sub1+sub2+sub3+sub4+sub5
# percentage=total/500*100
# if(percentage>=90):
#     print("A+")
# elif(percentage>=80):
#     print("A")
# elif(percentage>=70):
#     print("B")
# elif(percentage>=60):
#     print("C")
# elif(percentage>=50):
#     print("D")
# else:
#     print("E")

# num=int(input("Enter number:"))
# start=num//100
# end=num%10
# if(start==end):
#     print("Palindrome.")
# else:
#     print("Not palindrome.")

# num=int(input("Enter num:"))
# sum=0
# for i in range(1,num):
#     if(num%i==0):
#         sum=sum+i
# if (sum==num):
#     print("Perfect")
# else:
#     print("Not perfect")
  
# num=int(input("Enter num:"))
# sum=0
# temp=num
# while num>0:
#     digit=num%10
#     fact=1
#     for i in range(1,digit+1):
#         fact=fact*i
        
#     sum=sum+fact
#     num=num//10
# if(sum==temp):
#     print("Strong")
# else:
#     print("Not strong")

# num=int(input("Enter number:"))
# sum=0
# temp=num
# count=0

# n=num
# while n>0:
    
#     count=count+1
#     n=n//10
    
# n=num
# while n>0:
#     digit=n%10
#     sum=sum+digit**count
#     n=n//10
# if sum==temp:
#     print("armstrong")
# else:
#     print("Not armstrong")

# num=int(input("Enter num of student:"))
# total_per=0
# for i in range(1,num+1):
#     total=0
#     for j in range(1,6):
#         marks=float(input("Enter Marks:"))
#         total=total+marks
#         per=total/5
#     total_per=total_per+per
# avg_per=total_per/num
# print((avg_per))
# sum=0
# for i in range(1,5):
#     for j in range(1,5):
#         print(num,end=" ")
#         num=num
#     print()

# for i in range(1,6):
#     for j in range(1,6-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     for j in range(1,i):
#         print(j,end=" ")
#     print()

# num=int(input("Enter num:"))
# temp=num
# count=0

# for i in str(num):
#     count=count+1
  
# sum=0  
# for i in str(num):
#     digit=int(i)
#     sum=sum+digit**count

# if sum==num:
#     print("yes")
# else:
#     print("no")

# for i in range(1, 6):
#     for j in range(1, 6 - i):
#         print(" ", end=" ")

#     for j in range(1, 2 * i):
#         if j == 1 or j == 2 * i - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# for i in range(4, 0, -1):
#     for j in range(1, 6 - i):
#         print(" ", end=" ")

#     for j in range(1, 2 * i):
#         if j == 1 or j == 2 * i - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# for i in range(1, 5):

#     for j in range(1,i):
#         print(" ", end=" ")

#     for j in range(1,6-i):
#         print("*", end=" ")

#     print()

# num=153
# temp=num
# count=0
# while temp>0:
#     count+=1
#     temp=temp//10
    
# temp=num
# sum=0
    
# for i in range(1,count+1):
#     digit=temp%10
#     sum=sum+digit**count
#     temp=temp//10
    
# if sum==num:
#     print("Yes")
# else:
#     print("no")


