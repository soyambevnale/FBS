class house:
    def __init__(self,rooms,members,child):
        self.rooms=rooms
        self.members=members
        self.child=child
        
    def getRooms(self):
        return self.rooms
    def setRooms(self,newRooms):
        self.rooms=newRooms
        
    def getMembers(self):
            return self.members  
    def setMembers(self,newMembers):
        self.members=newMembers
        
    def getChild(self):
        return self.child   
    def setChild(self,newChild):
        self.child=newChild
        
    def show(self):
        print(f"Rooms : {self.rooms}  ,  Members : {self.members} : child : {self.child}")
        
m=house(4,6,2)
m.show()
m.setChild(3)
print(m.getChild())