class emp:
    def __init__(self,id,name,sal):
        self.id=id                # public
        self._name=name           # protected
        self.__sal=sal            # private
        
e=emp(101,'abc',500000)
print(e.id)
print(e._name)
# print(e.__sal )          #raise error
print(e._emp__sal)