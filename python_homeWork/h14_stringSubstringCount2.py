x = "atat"
y = "aattpratiakatatata"
t=0
def lop():
    global x,y,t
#slicing the y to start from the value present in x:  
    if (x in y)==True:
        i=y.index(x[0])
        y=y[i:]
    print(y)

#converting to list   
    x=list(x)
    y=list(y)
    
    print(range(len(y)-1))

#comparing the lists:  
    for i in range(len(x)-1):
        
        print(x[i:],y[i:(len(x))])
        
        if x[i:]==y[i:len(x)]: 
            print(x[i],y[i])
            t+=1
            break
        else:
            break
    
    print(t)
    y.remove(y[0])  #removing first element of y

#converting to strings:
    y=(''.join(y))
    x=''.join(x)
#loop to check for subString to be in String:
while x in y:
    lop() 
print('count:',t)