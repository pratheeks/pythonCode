s='BANANA'
x=0
y=0
for i in range(len(s)):
    if s[i] in 'AEIOU':
#        print(i)
        x+=(len(s)-(i))
#        print(x)
    else:
        y+=len(s)-i
#        print(y)
if x==y:
    print("DRAW")
elif x>y:
    print("KEVIN",x)
elif x<y:
    print("STUART",y)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
