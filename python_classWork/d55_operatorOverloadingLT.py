class Check:
    def __init__(self,x):
        self.x=x
    def __lt__(self,other):
        return self.x<other.x
    
c1=Check(20)
c2=Check(15)
print(c1<c2)
