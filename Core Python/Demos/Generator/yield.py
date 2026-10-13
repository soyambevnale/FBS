# def generateValue(n):
#     for i in range(1,n+1):
#         yield i
#         # return
        
        
# res=generateValue(5)

# # print(res)             # 1
# # print(res)              # 2
# print(next(res))         # 1
# print(next(res))         # 2
# print(next(res))         # 3 
# print(next(res))         # 4
# print(next(res))         # 5

# print(next(res))       ## raise error

# We want to generate Fibonacci numbers up to a certain limit.
# Instead of computing and storing the entire sequence in memory,
# create generator to yield Fibonacci numbers one by one,
# conserving memory and allowing for easy iteration.
# def fib(n):
#     a=-1
#     b=1
#     for i in range(1,n+1):
#         c=a+b
#         yield c
#         a=b
#         b=c
        
# n=5
# res=fib(n)
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))



# 2. Implement a generator function that yields palindrome numbers.
# Palindromes are numbers that read the same backward as forward
# (e.g., 121, 1331). Generate palindromes lazily and infinitely.
# def palindrome():
#     for i in range(101,1000):
#         temp=i
#         rev=0
#         while(i>0):
#             digit=i%10   #131 =13
#             rev=(rev*10)+digit
#             i=i//10    #13   =1
#         if temp==rev:
#             yield temp
        
# res=palindrome()
# print(next(res))
# print(next(res))

# 3. Write a generator function that mimics the behavior of the built-in
# range() function. The generator should take start, stop, and step
# arguments and yield numbers within the specified range.

def generator(start,stop,steps):
    while(start<stop):
        start=start+steps
        yield start

    
start=0
stop=11
step=2
res=generator(start,stop,step)
print(next(res))
print(next(res))