#s=input()
##print(s.swapcase())
#n=''
#
#for x in s:
#    if x.islower():
##        print(x.upper(),end='')
#         n=n+x.upper()    
##    elif x.isupper():
##        print(x.lower(),end='')        
##        n=n+x.lower()
#    else:
#        n=n+x.lower()
#print(n)


s='PrathEEks'
x='ASDFGHJKLZXCVBNMQWERTYUIOP'
a=(len(x))
n=''
for i in range(len(s)):
#    print(list(range(len(s))))
    for j in range(a):
#        print(list(range(a)))
        if s[i]==x[j]:
            n+=s[i].lower()
            break
        else:
            n+=s[i].upper()
            break
print(n)
print(len(n))
