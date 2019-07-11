#decimal to binary conversion:
for num in range(0,16):
    l=[]
    def binary(num):
        div=num//2
        re=num%2
        l.append(re)
        if div>1:
            binary(div)
        else:
            l.append(div)
    binary(num)
    print(l[::-1])
    
#binary to decimal conversion:    
    decimal=0
    j=0
    for i in l:
        if i==1:
            decimal+= 2**j
        j+=1
    print(decimal)
    print()