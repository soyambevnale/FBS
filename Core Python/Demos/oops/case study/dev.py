from emp import Employee
class Dev(Employee):
    def __init__(self, id, name, sal,bonus):
        super().__init__(id, name, sal)
        self.__bonus=bonus
        
    def getBonus(self):
        return self.__bonus
    
    def setBonus(self,new_bonus):
        self.__bonus=new_bonus
        
    def __str__(self):
        return super().__str__()+f"   Bonus={self.__bonus}" 