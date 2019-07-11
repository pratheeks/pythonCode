#method1:
a=('aabbcdaaewrhryreffgg')
print(type(a))
x=set(a)
b=0
for i in sorted(x):
    b=a.count(i)
    print(i,b)

#method2:
#b=sorted('aabbcdaaewrhryreffgg')
#print(b)                            
#print(type(b))                      #sorted returns list
#count=1
#i=0
#while i<len(b)-1:
#    if b[i]==b[i+1]:
#        count+=1
#        i+=1
#    else:
#        print(b[i],count)
#        i+=1
#        count=1
#print(b[-1],count)
