l=list(range(500))
a=1
for i in l:
    if a%10!=0:
        print(i,end=' ')
    else:
        print(i)
    a+=1
    