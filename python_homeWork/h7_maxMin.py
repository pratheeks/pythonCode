l=[]
n=int(input())
for i in range(n):
    a=int(input())
    l.append(a)
print(l)

fmax=-100
smax=-100

for i in l:
    if i>fmax:
        smax=fmax
        fmax=i
    elif i>smax and i!=fmax:
        smax=i
print(fmax,'is the maximum value')
print(smax,'is the runner-up value')
        