def demo():
    global x
    x+=1
    print(x)
#    return x
x=20
demo()
print(x)
print(demo())


def demo(a,b,c):
    print('The value of a,b,c is',a,b,c)
    
demo(10,20,10)



def det(a,b,c=20,d=10):
    print(a+b+c+d)
det(10,20,30,40)