
n=int(input())
#l=[]
#for i in range(n):
#    if i%2==0:
#        l.append(2**i)
l=[2**i for i in range(n) if i%2==0]
print(l)



a=['python','c']
b=['language','programming']
#l=[]
#for i in a:
#    for j in b:
#        l.append(i+' '+j)
l=[i+' '+j for i in a for j in b]
print(l)
