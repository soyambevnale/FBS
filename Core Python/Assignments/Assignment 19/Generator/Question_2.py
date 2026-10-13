# 2. Implement a generator function that yields palindrome numbers.
# Palindromes are numbers that read the same backward as forward
# (e.g., 121, 1331). Generate palindromes lazily and infinitely.

def palindrome():
    for i in range(101,1000):
        temp=i
        rev=0
        while(i>0):
            digit=i%10   #131 =13
            rev=(rev*10)+digit
            i=i//10    #13   =1
        if temp==rev:
            yield temp
        
res=palindrome()
print(next(res))
print(next(res))