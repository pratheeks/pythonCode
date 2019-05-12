#n=int(input())
n=8
for i in range(n):
    for j in range(n):
        print(' ',end='')
    for j in range(n-i):
        print(' ',end='')
    for j in range(i):
        print('^',end='')
    for j in range(i+1):
        print('^',end='')
    print()
for i in range(n):
    for j in range(n):
        print(' ',end='')
    for j in range(n):
        if (i==0 or j<=2 and j>=0 or j==n-1 or i==n-1 or j>=n-3  ): 
            print('*',end='')
        else:
            print(' ',end='')
    for j in range(n):
        if (i==0 or j==0 or j==n-1 or i==n-1 or j>n//2): 
            print('*',end='')
        else:
            print(' ',end='')
    print()
for i in range(n):
    for j in range(n-i):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    for j in range(n-1):
        if i>=2 and i<=n-4 and j>=2 and j<=n-4 :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    for j in range(i+1):
        print('*',end='')
    print()       
for i in range(n):
    for j in range(n):
        print(' ',end='')
    for j in range(n):
        print('*',end=' ')
    print()
for i in range(n):
    for j in range(n-i):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    for j in range(i):
        print('*',end='')
    for j in range(n-i-1):
        print(' ',end='')
    for j in range(n-i-1):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    for j in range(i):
        print('*',end='')
    print()
for i in range(n):
    for j in range(1):
        print(' ',end='')
    for j in range(n):
#        print('!',end=' ')
        if  j==0  or j==1 or j==3 or j==6  or j==8 or j==9 or j==n-1 or j==n-2:
            print('!',end=' ')
        else:
            print(' ',end=' ')
    for j in range(n+1):
        if  j==0  or j==1 or j==3 or j==6  or j==8 or j==9 or j==n-1 or j==n-2:
            print('!',end=' ')
        else:
            print(' ',end=' ')
    print()