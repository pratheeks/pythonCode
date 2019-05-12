#printthe range of given no.

a=int(input('Enter the number'))
for i in range(2,a+1):
    for j in range(2,i//2+1):
        if i%j==0:
            break
    else: 
        print(i)
