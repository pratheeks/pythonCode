l=[1,1,1,4,3,2,1,7,8,3]
print(l)
res=0
for i in range(len(l)-1):
    l.sort(reverse=True)
    # print(l)
    x=l.pop()
    y=l.pop()
    res+=x+y
    l.append(x+y)
print(res)












l=[1,1,1,4,3,2,1,7,8,3]
r=0
while(len(l)>1):
    l.sort(reverse=True)
    # print(l)
    a=l.pop()
    b=l.pop()
    r+=a+b
    l.append(a+b)
# print(r)