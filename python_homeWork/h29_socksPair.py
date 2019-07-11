a='1 1 3 1 2 1 3 3 3 3'.rstrip().split()
ar=list(map(int,a))
ar.sort()
#print(ar)
x=0
i=0
while ar!=set(ar):
    try:    
        if ar[i]==ar[i+1]:
            ar[i:i+2]=[]
#            print(ar)
            i=0
            x+=1
        else:
            i+=1
            continue
    except IndexError:
        break
print(len(ar))
print(x)
