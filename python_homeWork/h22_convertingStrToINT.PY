x=[]
s=['2,2']
for i in s:
    n=list(i)
    print(s)
    print(n)
    for i in n:
        if i.isalnum():
            x.append(int(i))
        
    print(x)