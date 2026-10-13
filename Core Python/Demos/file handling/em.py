# import pickle
# class employee:
#     def __init__(self,eid,name):
#         self.id=eid
#         self.name=name
        
#     def getid(self):
#         return self.id
    
#     def setid(self,newid):
#         self.id=newid
    
#     def getname(self):
#         return self.name
    
#     def setname(self,newname):
#         self.name=newname

#     def __str__(self):
#         return f"id : {self.id}  Name : {self.name}"


# e=employee(1,"Sachin")

# f=open("em.dat","wb")
# print(f.tell())

# ## pickle.dump("Object name","Object of file")

# pickle.dump(e,f)
# f.seek(0)

# fr=open("em.dat","rb")
# data=pickle.load(fr)
# print(data)


# li=[1,3,2,21,18,12,9]
# temp=[]
# res=[]
# for i in li:
#     if i%2!=0:
#         temp.append(i)
        
# for i in range(len(temp)):
#     if i%2==0:
#         res.append(temp[i])
        
# print(res)
li=[1,3,2,21,18,12,9]
count=0
for i in range(len(li)):
    if li[i]%2!=0:
        count+=1
        
        if count%2!=0:
            print(li[i])
        
