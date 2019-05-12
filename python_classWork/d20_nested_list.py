n=int(input())
l=[]
score=[]
for i in range(n):
    a=[]

    name=input()
    grade=float(input())
    score.append(grade)
    a.append(name)
    a.append(grade)
    l.append(a)
#print(l)
x= len(l)
#print('score:',score)
min0=max(score)
min1=max(score)
for i in range(x):
#    print(l[i][1])
    if l[i][1]<min0:
        min1=min0
        min0=l[i][1]
    elif l[i][1]<min1 and l[i][1]!=min0:
        min1=l[i][1]
#print('first lowest:',min0)
#print('second lowest:',min1)
s=[]
for i in range(x):
    if l[i][1]==min1:
#        print(l[i])
#        print(l[i][0])
        s.append(l[i][0])
#print(s)
s.sort()
for i in range(len(s)):
    print(s[i])
    
    
    
    
    
    
    
    
    
    
    
    
    
    