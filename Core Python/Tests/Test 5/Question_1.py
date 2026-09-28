# 1. A list contains the denominations as follows :
# D = [2000, 500, 200, 100 , 50, 20, 10, 5]
# Accept an amount from user and calculate how many
# minimum number of notes will be needed for that
# amount.

D = [2000, 500, 200, 100 , 50, 20, 10, 5]
amount=int(input("Enter amount : "))
count=0
for notes in D:
    if amount>=notes:
        n=amount//notes  
        count+=n
        amount=amount%notes
        
print("Minimum number of notes : ",count)
        
        
    