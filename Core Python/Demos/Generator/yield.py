def generateValue(n):
    for i in range(1,n+1):
        yield i
        # return
        
        
res=generateValue(5)

# print(res)             # 1
# print(res)              # 2
print(next(res))         # 1
print(next(res))         # 2
print(next(res))         # 3 
print(next(res))         # 4
print(next(res))         # 5

# print(next(res))       ## raise error