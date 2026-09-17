# Level 1 — Basic List Questions
# Create a list of 5 integers and print all elements.
# Find the length of a list without using len().
# def search(li):
#     count=0
#     for i in li:
#         count+=1
#     print("Length : ",count)
# li=[50,40,30,20,10]
# search(li)

# Find the sum of all elements in a list without using sum().
# def search(li):
#     total=0
#     for i in li:
#         total+=i
#     print("sum : ",total)
# li=[50,40,30,20,10]
# search(li)

# def search(li):
#     total=0
#     for i in range(0,len(li)):
#         total+=li[i]
#     print("sum : ",total)
# li=[50,40,30,20,10]
# search(li)

# Find the largest element in a list without using max().
# def search(li):
#     largest=li[0]
#     for i in range(1,len(li)):
#         if li[i]>largest:
#             largest=li[i]
#     print("largest: ",largest)
# li=[50,40,30,20,10]
# search(li)

# Find the smallest element in a list without using min().
# def search(li):
#     smallest=li[0]
#     for i in range(1,len(li)):
#         if li[i]<smallest:
#             smallest=li[i]
#     print("smallest: ",smallest)
# li=[50,40,30,20,10]
# search(li)

# Count how many even and odd numbers are present in a list.
# def search(li):
#     even=0
#     odd=0
#     for i in range(0,len(li)):
#         if li[i]%2==0:
#             even+=1
#         else:
#             odd+=1
#     print("even : ",even)
#     print("odd : ",odd)
# li=[50,34,33,45,66,78,55]
# search(li)

# Count the number of positive, negative and zero elements.
# def search(li):
#     positive=0
#     negative=0
#     zero=0
#     for i in range(0,len(li)):
#         if li[i]>0:
#             positive+=1
#         elif li[i]<0:
#             negative+=1
#         else:
#             zero+=1
#     print("positive : ",positive)
#     print("negative : ",negative)
#     print("zero : ",zero)
# li=[50,34,33,45,66,78,55,-3,-8,0,0,0]
# search(li)

# Search for an element in a list and print whether it is present or not.
# def search(li,ele):
    
#     for i in range(0,len(li)):
#         if ele==li[i]:
#             return i
#     else:
#         return -1

# li=[50,34,33,45,66,78,55,-3,-8,0,0,0]
# searchele=int(input("Enter number to search : "))
# res=search(li,searchele)
# if(res!=-1):
#     print(f"{searchele} is present at index {res} .")
# else:
#     print(f"{searchele} is not present .")

# Print all elements of a list in reverse order without using reverse().
# def rev(li):
#     for ind in range(len(li)-1,-1,-1):
#         print(li[ind],end=" ")
# li=[10,20,30,40,50]
# rev(li)

# Find the average of elements in a list.
# def average(li):
#     total=0
#     count=0
#     for ind in range(0,len(li)):
#         total+=li[ind]
#         count+=1
#     avg=total/count
#     print("Average : ",avg)

# li=[10,20,30]
# average(li)


# 🟡 Level 2 — Important DSA Questions
# Find the second largest element in a list.
# def search(li):
#     first=li[0]
#     second=li[1]
#     if second>first:
#         first,second=second,first
#     for ind in range(2,len(li)):
#         if li[ind]>first:
#             second=first
#             first=li[ind]
#         elif li[ind]>second and first!=li[ind]:
#             second=li[ind]
#     print("first : ",first)
#     print("Second : ",second)
# li=[50,40,30,20,10]
# search(li)


# Find the second smallest element in a list.
# def search(li):
#     first=li[0]
#     second=li[1]
#     if second<first:
#         first,second=second,first
#     for ind in range(2,len(li)):
#         if li[ind]<first:
#             second=first
#             first=li[ind]
#         elif li[ind]<second and first!=li[ind]:
#             second=li[ind]
#     print("first : ",first)
#     print("Second : ",second)
# li=[50,40,30,20,10]
# search(li)

# Remove all duplicate elements from a list.
# def remove_du(li):
#     new=[]
#     for i in li:
#         if i not in new:
#             new.append(i)
#     print("After removing duplicate : ",new)        

# li=[10,20,20,30,30,30,40]
# remove_du(li)

# Find all duplicate elements  
# def dup(li):
#     result=[]
#     dupp=[]
#     for i in li:
#         if i not in result:
#             result.append(i)
#         else:
#             if i not in dupp:
#                 dupp.append(i)
            
#     print(dupp)
    
# li=[1,3,5,1,6,3,6,4]
# dup(li)

# Find the frequency of each element in a list.
# def frequency(li):
#     freq={}
#     for i in li:
#         if i in freq:
#             freq[i]=freq[i]+1
#         else:
#             freq[i]=1
#     print(freq)
# li=[10,10,20,30,40,20]
# frequency(li)

# def sl(li):
#     visit=[]
#     for i in range(len(li)):
#         if li[i] not in visit:
#             count=0
#             for j in range(len(li)):
#                 if li[i]==li[j]:
#                     count+=1
            
#             print(li[i],"=",count)
#             visit.append(li[i])
      
# li=[10,20,30,30]
# sl(li)
            
# Find the element that occurs maximum number of times.
# def more(li):
#     freq={}
#     for i in li:
#         if i in freq:
#             freq[i]=freq[i]+1
#         else:
#             freq[i]=1
    
#     maximum=0   
#     for i in freq:     
#         if freq[i]>maximum:
#             maximum=freq[i]
#     print("Maximum :",maximum)
        
#     for i in freq:
#         if freq[i]==maximum:
#             print(i)
    
# li=[10,20,30,40,30,20,60]
# more(li)
    
# Find the element that occurs minimum number of times.
# def mini(li):
#     freq={}
#     for i in li:
#         if i in freq:
#             freq[i]=freq[i]+1
#         else:
#             freq[i]=1
#     minimum=1
#     for i in freq:
#         if freq[i]<minimum:
#             minimum=freq[i]
#     print("Minimum :",minimum)
    
#     for i in freq:
#         if freq[i]==minimum:
#             print(i)
            
# li=[10,20,30,40,30,20]
# mini(li)

# Separate even and odd numbers into two different lists.
# def sep(li):
#     even=[]
#     odd=[]
#     for i in li:
#         if i%2==0:
#             even.append(i)
#         else:
#             odd.append(i)
#     print("Even : ",even)
#     print("Odd : ",odd)
    
# li=[10,33,40,45]
# sep(li)

# Move all zeros to the end of the list.
# def zeros(li):
#     zero=[]
#     for i in li:
#         if i!=0:
#             zero.append(i)
    
#     for i in li:
#         if i==0:
#             zero.append(i)
            
#     print(zero)
# li=[10,0,0,20,40]
# zeros(li)

# Move all zeros to the beginning of the list.
# def zeros(li):
#     zero=[]
#     for i in li:
#             if i==0:
#                 zero.append(i)
#     for i in li:
#         if i!=0:
#             zero.append(i)
        
#     print(zero)
# li=[10,20,30,0,0,30,0,20,20]
# zeros(li)
            
# Find all elements that occur only once.
# def occur(li):
#     for i in li:
#         count=0
#         for j in li:
#             if i==j:
#                 count+=1
            
#         if count==1:
#             print(i)
    
# li=[10,20,10,40]
# occur(li)

# Find common elements between two lists.
# def common(li1,li2):
#     for i in li1:
#         for j in li2:
#             if i==j:
#                 print(i)
            
# li1=[18,57,57,88,99]
# li2=[18,66,57,888]
# common(li1,li2)
            
# # Find elements present in the first list but not in the second list.
# def first(li1,li2):
#     list=[]
#     for i in li1:
#         if i not in li2:
#             list.append(i)
#     print(list)
    
# li1=[1,2,3,4]
# li2=[1,2,5,6]
# first(li1,li2)

# Merge two lists without using +.
# def merge(li1,li2):
#     result=[]
#     for i in li1:
#         result.append(i)
        
#     for i in li2:
#         result.append(i)
        
#     print(result)
    
# li1=[1,2,3,4]
# li2=[4,3,5,6]
# merge(li1,li2)

# Find the intersection of two lists.
# def inter(li1,li2):
#     result=[]
#     for i in li1:
#         if i in li2:
#             result.append(i)
        
#     print(result)
    
# li1=[1,2,3,4]
# li2=[3,4,5,6]
# inter(li1,li2)

# Find the union of two lists.
# def union(li1,li2):
#     result=[]
#     for i in li1:
#         if i not in result:
#             result.append(i)
            
#     for i in li2:
#         if i not in result:
#             result.append(i)
            
#     print(result)
    
# li1=[1,2,3,4]
# li2=[3,4,5,6]
# union(li1,li2)

# Find the sum of elements at even indexes.
# def dup(li):
#     total=0
#     for i in range(0,len(li)):
#         if i%2==0:
#             total=total+li[i]
            
#     print(total)    
# li=[10,20,10,20,30,40]
# dup(li)

# Find the sum of elements at odd indexes.
# def dup(li):
#     total=0
#     for i in range(0,len(li)):
#         if i%2!=0:
#             total=total+li[i]
            
#     print(total)    
# li=[10,20,10,20,30,40]
# dup(li)


# Print elements present at even indexes.
# def dup(li):
#     for i in range(0,len(li)):
#         if i%2==0:
#             print(li[i])
    
# li=[10,20,10,20,30,40]
# dup(li)

# Print elements present at odd indexes.
# def dup(li):
#     for i in range(0,len(li)):
#         if i%2!=0:
#             print(li[i])
    
# li=[10,20,10,20,30,40]
# dup(li)



# 🟠 Level 3 — Sorting & Searching
# Implement linear search on a list.

# def search_element(li,ele):
#     for ind in range(0,len(li)):
#         if ele==li[ind]:
#             return ind
#     else:
#         return -1
    
# li=[10,20,30,40,50]
# element=int(input("Enter number : "))
# res=search_element(li,element)
# if(res!=-1):
#     print(f"{element} is present at index {res} .")
# else:
#     print(f"{element} is not present .")
    
# Implement binary search on a sorted list.

# Sort a list in ascending order without using sort().
# def sorting(li):
#     size=len(li)
#     for i in range(1,size):
#         for j in range(0,size-i):
#             if li[j]>li[j+1]:
#                 li[j],li[j+1]=li[j+1],li[j]
    
# li=[34,53,56,2,1,3]
# print("Before : ",li)
# sorting(li)
# print("After : ",li)

# Sort a list in descending order without using sort() or sorted().
# def sorting(li):
#     for i in range(len(li)):
#         for j in range(len(li)-i-1):
#             if li[j]<li[j+1]:
#                 li[j],li[j+1]=li[j+1],li[j]
# li=[45,33,4,1,35,63]
# print("Before :",li)
# sorting(li)
# print("After :",li)

# Implement Bubble Sort.
def asc_bubble(li):
    size=len(li)
    for i in range(1,size):
        for j in range(0,size-i):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]

li=[46,86,87,90,34,45]
asc_bubble(li)
print("Asc :",li)


def desc_bubble(li):
    size=len(li)
    for i in range(1,size):
        for j in range(0,size-i):
            if li[j]<li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]

li=[9878,77,99,2,90,98]
desc_bubble(li)
print("Desc :",li)
                
# Implement Selection Sort.
# Implement Insertion Sort.
# Find the position/index of the largest element.
# Find the position/index of the smallest element.
# Find the k-th largest element in a list.


# 🔴 Level 4 — Interview/DSA Level
# Rotate a list left by one position.
# Rotate a list right by one position.
# Rotate a list left by k positions.
# Rotate a list right by k positions.
# Find the missing number from a list containing numbers from 1 to n.
# Find the duplicate number in a list.
# Find two elements whose sum equals a given target (Two Sum).
# Find all pairs whose sum equals a given number.
# Find the maximum difference between two elements.
# Find the maximum subarray sum.
# Find the longest consecutive sequence in a list.
# Check whether a list is a palindrome.
# Find the first repeating element.
# Find the first non-repeating element.
# Check whether two lists are equal without directly using ==



# Good morning, sir. My name is Soyam. I am a diligent, adaptable, and self-motivated person with a strong willingness to learn and grow. I believe in continuous learning and always try to improve myself through new experiences and challenges. I am proactive in taking responsibility and committed to giving my best in every task I undertake. As a fresher, I am looking for an opportunity where I can apply my abilities, gain practical experience, and contribute positively to the organization. Thank you.