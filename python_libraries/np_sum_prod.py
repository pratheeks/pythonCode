import numpy
n,m=map(int,input().split())
a=numpy.array([input().split() for i in range(n)],int)
# print(a)
b=numpy.sum(a,axis=0)
print(b)
print(numpy.prod(b))