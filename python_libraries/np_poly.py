import numpy as np
a=np.array(input().split(),float)
x=int(input())
print(np.polyval(a,x))