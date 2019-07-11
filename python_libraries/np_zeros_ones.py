import numpy as np
n,m,p=tuple(map(int,input().strip().split()))
# for i in range(n):
#     print(np.ones((m,p),int))
# l=([np.ones((m,p),int) for i in range(n)],int)
# print(l)
# for i in range(n):
#     print(np.zeros((m,p),int))
# ar=([np.zeros((m,p),int) for i in range(n)],int)
# print(ar)

# print(np.concatenate((l,ar)))
print(np.zeros((n,m,p),int))
print(np.ones((n,m,p),int))