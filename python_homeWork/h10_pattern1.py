n=10
for i in range(n):
    for j in range(n):
        print('   ',end=' ')
    for j in range(n-i):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    for j in range(i):
        print('*',end='')
    print()
for i in range(n):
    for j in range(n):
        print(' ',end=' ')
    for j in range(i+2):
        print(' ',end='')
    for j in range(n-i):
        print('*',end='')
    for j in range(n-i-1):
        print('*',end='')
        
        
    for j in range(i+1):
        print(' ',end='')
    for j in range(n-2):
        print('  ',end='')
    for j in range(i+1):
        print(' ',end='')
    for j in range(n-i):
        print('*',end='')
    for j in range(n-i-1):
        print('*',end='')
    print()
for i in range(n):
    for j in range(n):
        print(' ',end=' ')
    for j in range(n-i+1):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    for j in range(i):
        print('*',end='')
        
        
    for j in range(n-i):
        print(' ',end='')
    for j in range(n-2):
        print('  ',end='')
    for j in range(n-i):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    for j in range(i):
        print('*',end='')
    print()
for i in range(n):
    for j in range(n):
        print('   ',end=' ')
    for j in range(i+1):
        print(' ',end='')
    for j in range(n-i):
        print('*',end='')
    for j in range(n-i-1):
        print('*',end='')
    print()

    