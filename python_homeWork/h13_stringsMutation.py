#sring mutation:

a='abracadabra'
#a=input()
print(a)
b,c=input().split()
b=int(b)
l=list(a)
print(l)
l[b]=c
print(l)
#s=str(l)
#print(s)
#print(type(s))
str=''.join(l)
print(str)



#using slicing:
print(a)
s=a[:b]+c+a[b+1:]
print(s)
