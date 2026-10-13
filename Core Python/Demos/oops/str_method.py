class time:
    def __init__(self,hr,min,sec):
        self.hr=hr
        self.min=min
        self.sec=sec
        
    # def show(self):
    #     print( f"Hour : {self.hr}   Minute : {self.min}   Second : {self.sec}")
        
    def __str__(self):
        return  f"Hour : {self.hr}   Minute : {self.min}   Second : {self.sec}"
    
    
t=time(12,3,3)
print(t)