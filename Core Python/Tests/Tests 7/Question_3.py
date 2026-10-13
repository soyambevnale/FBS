# 3. Write a Python program that generates a list of odd numbers from 1
# to 50 using list comprehension and filters out the even numbers

odd=[x for x in range(1,51) if x%2!=0]
print(odd)

even=[x for x in range(1,51) if x%2==0]
print(even)
