import numpy as np
a=input().strip().split()
print(a)
a=np.array(a,float)
print((a))

arr=input().strip().split()
ar=np.array(arr,int)
# ar.shape=(3,3)
print(ar)
print(np.reshape(ar,(3,3)))
