# # 10. Write a program to print list after removing even numbers. 

def removeEven(li):
    temp=[]
    for i in li:
        if i%2!=0:
            temp.append(i)
            
    print("After removing even elements : " , temp)
    
li=[2,3,4,5,6]
removeEven(li)
