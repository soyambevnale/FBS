# 13. Python Program to count number of digits and letters in a string.

string='1 . Data '
digit=0
for i in string:
    if i.isdigit():
        digit+=1

letter=0
for i in string:
    if i.isalpha():
        letter+=1
        
print("Digit : " ,digit)
print("Letter : " , letter)
    