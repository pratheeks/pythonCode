#pattern1
#n=int(input())
n=10
for i in range(n):
    for j in range(n):
        print('*',end='')
    print()
    
    
print() 

#pattern 2
for i in range(n):
    for j in range(i+1):
        print('*',end='')
    print()

#pattern 3:

for i in range(n):
    for j in range(n-i):
        print('*',end='')
    print()
    
