import itertools
n='HACK 2'.split()
#print(n)
perm=itertools.permutations(n[0],int(n[1]))
#print(sorted(list(perm)))
newp=''
for i in sorted(list(perm)):
    for j in range(int(n[1])):
        newp+=i[j]
    print(newp)
    newp=''
