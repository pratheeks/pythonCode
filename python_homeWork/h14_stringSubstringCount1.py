x = "at"
y = "pratiakataata"
t=0
def lop():
    t=0
    global x,y
    print(1,x)
    print(2,y)
    print()
    if (x in y)==True:
        i=y.index(x[0])
        y=y[i:]
        print(y)
    x=list(x)
    y=list(y)
    
    for i in range(len(x)):
        if x[i]==y[i]:
            print(x[i],y[i])
            t+=1
    y.remove(x[0])
    print('y:',y)
    print(t)
    y=(''.join(y))
    x=''.join(x)
while x in y:
    print(x,y)
    t+=1
    lop()
    continue
print(x)
print(y)
print(t)

'''
x = "at"
y = "pratikatataa"
a=0
def cnt():
    b=0
    for i in range(len(x)-1):
        print('x[i+1]',x[i+1])
        print()
        for j in range(len(y)):
            print('y[n+1]',y[n+1])
            if x[i+1]==y[n+1]:
                b+=1
                print('b:',b)
                print()
            
            break
z=0
n=0    
for i in range(len(x)):
    print('x[i]:',x[i])

    for j in range(len(y)):
        print('y[j]:',y[j])
        if x[i]==y[j]:

            a+=1
            print('a:',a)
            n=j
            print('indexOfJ',n)
            print()
            cnt()

#            print('z:',z)
            break
            
#    continue
print(a)
'''