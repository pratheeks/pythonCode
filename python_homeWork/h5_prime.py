#check whether the given no. is prime or not
a=int(input('Enter the number'))

c=range(2,a//2+1)
#print(list(c))

for i in c:
    if a%i==0:    
       print('nonprime')
       break
else:
    print('prime')
        