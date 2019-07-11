s='ABCAB'
l={}
for i in s:
    if i in l:
        print(i)
        break
    else:
        l[i]=1
