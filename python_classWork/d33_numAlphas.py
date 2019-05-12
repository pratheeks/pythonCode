s='T1h2i3s i4s1 m1y2 c1la2s2s2'
t=''
n=0
for i in s:
    if (i>='a' and i<='z') or (i>='A' and i<='Z'):
        t+=i
    elif i>='0' and i<='9':
        n+=int(i)
    elif i==' ':
        t+=str(n)+' '
        n=0
t+=str(n)
print(t)


for i in s:
    pass