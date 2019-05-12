class Demo:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return '({0},{1})'.format(self.x,self.y)
    
d1=Demo(10,20)
d2=Demo(-5,7)
print(d1,d2)