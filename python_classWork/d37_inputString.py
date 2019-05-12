#method1:
#a=('acdb')
#print(a)
#a=list(a)
#print(a)
#
#for i in range(len(a)):
#    for j in range(len(a)):
#        if a[i]<a[j]:
#            x=a[i]
#            a[i]=a[j]
#            a[j]=x
#    print(a)
#       
##print(a)


#method2:
a=list(input('enter the string?\n'))
m=list(filter(lambda x: x.isalpha(),a))
print(m)
#w=[]
#for i in a:
#    if i.isalpha():
#        w+=i
#print(w)    
def sort(a):
    t=''
    for i in range(len(a)):
        for j in range(i,len(a)):
            if a[i]>a[j]:
                x=a[j]
                a[j]=a[i]
                a[i]=x    
        t+=a[i]
    return t
print(sort(m))
