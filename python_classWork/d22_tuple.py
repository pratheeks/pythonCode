t=('hello',)
print(t)
print(type(t))
print()

t=(1,2,3,4,5)
print(t)
#t[0]=10
#print(t)
print()

t=(1,2,3,4,5,[6,7,8,9],10)
print(t)
t[-2][1]=20
print(t)
del(t)
#print(t)

print((1,2,3)+(4,5,6))

l=(1,2,3,4,5,6)
print(enumerate(l))
l1=list(enumerate(l))
print(l1)
