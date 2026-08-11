#1 first way
for i in range(1,6):
    for j in range(1,6-i):
            print(" ",end=" ")
      
    for j in range(1,i*2):
            print(j,end=" ")
            
    print()
    
#2 second way   
for i in range(1,6):
    k=1
    for j in range(1,6-i):
            print(" ",end=" ")
      
    for j in range(1,i+1):
            print(k,end=" ")
            k+=1
    
    for j in range(1,i):
            print(k,end=" ")
            k+=1
            
    print()