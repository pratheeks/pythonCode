#Finding the Runner-up 
'''
n=5
a=[2,3,4,6,6,5]
print(a)
#a.sort()
#a.reverse()
#print(a.count(max(a)))
if a.count(max(a))>1:
    for i in a:
        if i==max(a):
            
  
            a.remove(i)
            print(a)
            a.remove(max(a))
else:             
    a.remove(max(a))
print(max(a))
'''
n=5
a={2,3,6,6,5}
a=list(a)
print(a)
b=max(a)
#a.sort()
#a.reverse()
#print(a.count(max(a)))
if a.count(b)>1:
    for i in a:
        if i==b:
            
        
            a.remove(i)
#            print(a)
#            a.remove(max(a))
    

else:             
    a.remove(max(a))
print(max(a))
