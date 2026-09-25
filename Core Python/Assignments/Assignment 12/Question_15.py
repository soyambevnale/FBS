# 15. Python Program to find larger string without using built-in functions.

string_1=input("Enter string 1  : ")
string_2=input("Enter string 1 : ")
string_3=input("Enter string 3 :")

count_1=0
count_2=0
count_3=0 

for i in string_1:
    count_1+=1
    
for i in string_2:
    count_2+=1

for i in string_3:
    count_3+=1

if count_1>count_2:
    if count_1>count_3:
        print("String 1 is larger .")
    else:
        print("String 3 is larger .")

else:
    if count_2>count_3:
        print("String 2 is larger .")
    else:
        print("String 3 is larger .")