n=int(input('enter'))
for i in range(1,n):
    a=(str(i)*i)    
    print(a)
    print(type(a))    #output is in str format
    print()
    
for i in range(1,n):
    b=("".join((str(i))*i))   
    print(b)
    print(type(b))  #output is in str format
    print()
    
for i in range(1,n):
    c=(i*((10**i-1)//9))
    print(c)
    print(type(c))  #output is in int format
    
    
    