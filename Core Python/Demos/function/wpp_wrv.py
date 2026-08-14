# def palindrome(num):
#     start=num//100
#     end=num%10
#     if(start==end):
#         return True
#     else:
#         return False
# num=int(input("Enter num:"))
# res=palindrome(num)
# print(res)


# def check(num):
#     temp=num
#     rev=0
#     while(temp>0):
#         d=temp%10
#         temp=temp//10
#         rev=rev*10+d
#     if(num==rev):
#         return True
#     else:
#         return False
# num=int(input("Enter num:"))
# print(check(num))
 
 
#  w/o pp and w/o rv
# def aor():
#     l=float(input("Enter length:"))
#     b=float(input("Enter breadth:"))
#     area=l*b
#     print(area)
# aor()

#  w pp and w/o rv
# def aor(l,b):
#     area=l*b
#     print(area)
# x=10
# y=10
# aor(x,y)

#  w/o pp and w rv
# def aor():
#     l=float(input("Enter length:"))
#     b=float(input("Enter breadth:"))
#     area=l*b
#     return area
# res=aor()
# print(res)

#  w pp and w rv
def aor(l,b):
    area=l*b
    return area

x=float(input("Enter length:"))
y=float(input("Enter breadth:"))
res=aor(x,y)
print(res)
    