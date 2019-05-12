
n=int(input())
l=[]
for i in range(n):
    l.insert(i,int(input()))
l.sort()

print(l)

for i in l:
    if(l[-1]==l[-2]):
        l.pop()
    else:
        break
        
print(l[-2])


#all test-case passed 
'''
n=int(input())
a=list(set(map(int,input().split())))
a.sort()
print(a[-2])
'''


