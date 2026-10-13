# 6. Write a Python program to find the two numbers whose product is
# maximum among all the pairs in a given list of numbers. Use the
# Python set.

li=[2,3,4,5,6]
s=set(li)

maximum=0
for i in s:
    for j in s:
        if i!=j:
            product=i*j
            if product>maximum:
                maximum=product
                n1=i
                n2=j

print("Two numbers : ",n1," , ",n2)
print("Product : ",product)