# 9. Write a program to create three lists of numbers, their squares and cubes 

def numSC(li):
    numbers=[]
    squares=[]
    cubes=[]
    
    for i in  li:
        numbers.append(i)
        squares.append(i**2)
        cubes.append(i**3)
        
    print("Numbers : ",numbers)
    print("Squares : ",squares)
    print("Cubes   : " , cubes)
    
li=[2,3,4,5,6]
numSC(li)
