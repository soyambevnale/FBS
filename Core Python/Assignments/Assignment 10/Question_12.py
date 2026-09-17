# 12. Write a program to create three lists of numbers, their squares and cubes

def threeList(li):
    numbers=[]
    squares=[]
    cubes=[]
    for i in li:
        numbers.append(i)
        squares.append(i**2)
        cubes.append(i**3)
        
    print("Number list :",numbers)
    print("Squares list :",squares)
    print("Cubes list :",cubes)
    
li=[2,3,4,5,6]
threeList(li)