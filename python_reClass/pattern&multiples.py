n=5
l=[]
x=[]
for i in range(1,n+1):
    for j in range(1,i+1):
        l.append(i*j)
    x.append(l)
    l=[]
print(x)

for i in range(1,11):
    print(f'{n} * {i} =',n*i)


for i in range(n+1):
    for j in range(n-i):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    for j in range(i):
        print('*',end='')
    for j in range(n-i):
        print(' ',end='')
    for j in range(n-i):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    for j in range(i):
        print('*',end='')
    print()
for i in range(n+1):
    for j in range(i+1):
        print(' ',end='')
    for j in range(n-i):
        print('*',end='')
    for j in range(n-i-1):
        print('*',end='')
    for j in range(i+1):
        print(' ',end='')
    for j in range(i+1):
        print(' ',end='')
    for j in range(n-i):
        print('*',end='')
    for j in range(n-i-1):
        print('*',end='')
    print()