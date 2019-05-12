class Rectangle:
    def __init__(self,l,w):
        self.l = l
        self.w= w
        print("This is Rectangle")
    def area(self):
        print(self.l*self.w)
    
    def perimeter(self):
        print(2*(self.l+self.w))
        
class square1(Rectangle):
    def __init__(self,s):
        super().__init__(s,s)
        print("This is square1")


class square2(Rectangle):
    def __init__(self,s):
        super().__init__(s,s)
        print("This is square2")
        
r=Rectangle(10,20)
r.area()
r.perimeter()

print()

s1=square1(5)
s1.area()
s1.perimeter()

print()

s2=square2(2)
s2.area()
s2.perimeter()
