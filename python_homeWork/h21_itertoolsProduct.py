a=list(map(int,input().rstrip().split(' ')))
print(a)
b=list(map(int,input().rstrip().split(' ')))
print(b)

w=[(x,y) for x in a for y in b]
#print(w)
print(' '.join(map(str,w)))
    
from itertools import product
print(*(product(a,b)))