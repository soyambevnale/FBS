# 10.Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions

string_1=input("Enter string 1 : ")
string_2=input("Enter string 2 : ")

count_1=0
for i in string_1:
    count_1+=1
    
count_2=0
for i in string_2:
    count_2+=1
    
if count_1>count_2:
    print("String 1 is larger : " , string_1)
elif count_2>count_1:
    print("String 2 is larger : " , string_2)
else:
    print("Both are same in size ")
    