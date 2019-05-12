#finding runner-up using user input
n=int(input())
a=list(input())
print(a)
if a.count(max(a))>1:
    for i in a:
        if i==max(a):
            
            a.remove(i)
            print(a)
            a.remove(max(a))
    

else:             
    a.remove(max(a))
print(max(a))