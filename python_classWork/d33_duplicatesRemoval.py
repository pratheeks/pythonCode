s=input('Enter the input\n')
s=sorted(s)
t=''
i=0
print(len(s)-1)
while i<len(s)-1:
    if s[i]!=s[i+1]:
        t+=s[i]
        print(t)
        i+=1
    else:
        i+=1
t+=s[-1]
print(t)
#print(s)