import numpy
n,m=numpy.array(input().split(),int)
print(str(numpy.eye(n,m)))
print(str(numpy.eye(n,m)).replace('0',' 0').replace('1',' 1'))