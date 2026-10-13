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