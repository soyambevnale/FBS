class time:
    def __init__(self,hr,min,sec):
        self.hr=hr
        self.min=min
        self.sec=sec
        
    def __str__(self):
        return f"Hr= {self.hr}    Min={self.min}    sec={self.sec}" 
        
c=class(2,23,45)
print(c)
