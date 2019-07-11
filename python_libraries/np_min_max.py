import numpy as np
n,m=map(int,input().split())
a=np.array([input().split() for i in range(n)],int)
b=np.min(a,axis=1)
print(b)
print(max(b))