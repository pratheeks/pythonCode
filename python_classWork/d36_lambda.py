#sol1:
l=range(1,101)
l1=[]

def power(i):
    return i**5
    
for i in l:
    if i%3==0 and i%5==0:
#        l1.append(i)
        l1.append(power(i))
print(l1)

#sol2:

#filter :to check conditon
#map: to evalute or perform the expression

l=list(range(1,101))
l1=list(filter(lambda x:x%3==0 and x%5==0,l))       #filter : checking
l2=list(map(lambda x:x**5,l1))                      #map : operation
print(l2)

l2=list(map(lambda x:x**5,list(filter(lambda x:x%3==0 and x%5==0,l)))) #filter & map
print(l2)

#map:
#l2=list(map(lambda x:x*11,l))
#print(l2)
