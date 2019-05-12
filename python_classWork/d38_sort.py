l=[]
n=int(input('enter no of inputs?\t'))
for i in range(n):
    l.append(int(input('enter elements\t')))
print(l)
print(list(range(len(l)-1)))
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            a=l[i]
            l[i]=l[j]
            l[j]=a
print(l)