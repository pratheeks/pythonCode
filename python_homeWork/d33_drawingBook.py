n=10
p=9
l=[]
l.append(p//2)
print(l)
if n%2==0:
    l.append((n-p+1)//2)
else:
    l.append((n-p)//2)
print(l)
print(min(l))


'''
count=0
l=[]
for i in range(1,p+1):
    if i<=p:
        count+=1
l.append(count//2)
print(count)
cnt=0   
for i in range(n,p-1,-1):
#    print(i)
    if i>p :
        cnt+=1
if n%2!=0:
    l.append(cnt//2)
else:
    l.append(cnt)
print(cnt)

print()

print(l)
print(min(l))

'''
















        