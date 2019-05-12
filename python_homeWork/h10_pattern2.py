n=int(input())
for i in range(n):
    for j in range(n):
        print(' ',end='')
    for j in range(n-i):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    for j in range(i):
        print('*',end='')
    print()
for i in range(n):
    for j in range(n):
        print(' ',end='')
    for j in range(n):
        print('*',end='')
    for j in range(n):
        print('*',end='')
    print()
for i in range(n):
    for j in range(n-i):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    for j in range(n):
        print('*',end='')
    for j in range(n):
        print('*',end='')
    for j in range(i):
        print('*',end='')
    print()
for i in range(n):
    for j in range(n-i):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    for j in range(n):
        print('*',end='')
    for j in range(n):
        print('*',end='')
    for j in range(i):
        print('*',end='')
    print()
for i in range(n):
    for j in range(n):
        print(' ',end='')
        
    for j in range(n):
        if j==0 or j==n-1 or j==n-3 or j==3:
            print('*',end='')
        else:
            print(' ',end='')
    for j in range(n):
        if j==0 or j==n-1 or j==n-3 or j==3:
            print('*',end='')
        else:
            print(' ',end='')
    print()