# 2. Python Program to Remove the nth Index Character from a Non-Empty String

n=int(input("Enter index : "))

string=input("Enter string : ")
res=string[:n]+string[n+1:]
print(res)