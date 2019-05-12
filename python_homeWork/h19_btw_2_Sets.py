def getTotalX(a, b):
    x=a[len(a)-1]
    i=1
    z=[]
    while x<b[0]:
        x=a[len(a)-1]
        x=x*i 
        z.append(x)
        i+=1
               
#    print('z:',z)
#    print('a:',a)
    w=[]
    for i in z:
        for j in a:
            if i%j==0:
                 w.append(i)
            else:
                break
             
    w=list(set(w))   
#    print('w:',w)
    g=[]
    
    for i in w:
        for j in b:
            if j%i==0:
                g.append(i)
#    print('g:',g)
    if g==[]:
        pass
    else:    
        leng=(max((g.count(i)) for i in g))
#    print('leng-',leng)
    cnt=0
    for i in list(set(g)):
#        print(g.count(i))
        if g.count(i)==leng:
            cnt+=1
    print(cnt)

a = [3,4]
b = [24,48]

a=[2,4]
b=[16,32,96]

a=[2]
b=[20,30,12]


a=[2,6]
b=[24,36]

a=[100,99,98,97,96,95,94,93,92,91]
b=[1,2,3,4,5,6,7,8,9,10]
total = getTotalX(a, b)
