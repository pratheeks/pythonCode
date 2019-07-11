











'''
#Generators
def demo():
    yield 1


print(next(demo()))
a=demo()
print(next(a))
print(next(a))

'''














'''
def demo():
    global x
    x=5
    print(1,x)
    return x


x=2
print(demo())
print(3,x)
'''

# a=list(filter(lambda x:x%3==0,range(1,101)))
# b=list(map(lambda x:x**5,a))
# c=list(filter(lambda x: x%5==0,b))
# d=list(map(lambda x: x//10,c))
# print(d)

