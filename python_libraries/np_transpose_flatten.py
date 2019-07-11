n,m=map(int,input().strip().split())
# print(type(n),m)
l=[]
for i in range(n):
    l.append(input().strip().split())
# print(l)
a=np.array(l,int)
print(a)
print(np.transpose(a))
print(a.flatten())