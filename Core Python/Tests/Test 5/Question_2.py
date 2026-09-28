# # 2. A teacher came to class with a large box tokhat has
# several coins. Each coin has a number printed on it.
# Before coming to class, she ensured that All the
# numbers occur an Even number of times. However,
# while coming to the class, one coin fell down and got
# lost. She wants to find out the number on the missing
# coin.
# Inputs:
# The original number of coins and the actual
# number on each of the coins, separated by spaces.
# Output: The number on the missing coin
# Sample Input: 8
# 5 7 2 7 5 2 5
# Sample Output: 5

li=[5,7,2,7,5,2,5]
freq={}
for i in li:
    if i in freq:
        freq[i]=freq[i]+1
    else:
        freq[i]=1
for i in freq:   
    if freq[i]%2==0:
        pass
    else:
        print(i)
