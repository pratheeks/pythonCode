import numpy as np
n,m,p=map(int,input().strip().split())
ar=[]
l=[]
for i in range(n):
    l.append(list(map(int,(input().strip().split()))))
l=np.array(l)
print(l)
for i in range(m):
    ar.append(list(map(int,(input().strip().split()))))
ar=np.array(ar)
print(ar)
print(np.concatenate((l,ar),0))


'''
#method2:
import numpy as np
n,m,p=map(int,input().strip().split())
# print(n,m,p)

l=(np.array([input().strip().split() for i in range(n)],int))
print(l)

ar=(np.array([input().strip().split() for i in range(m)],int))
print(ar)
print(np.concatenate((l,ar)))
'''