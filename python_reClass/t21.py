a='this is my class'

#counting words 
i=0
j=0
x=''
while i<len(a):
    if a[i]!=' ':
#        print(a[i],end='')
        x+=a[i]
        i+=1
        j+=1
    
    
    elif a[i]==' ':
#        print(j,' ',end='')
        x+=str(j)+' '
        i+=1
        j=0
x+=str(j)
#print(x)

#capitalising first letters of all the words:
j=''
for i in range(len(x)):
    
    if x[i]==' ' and x[i+1]!=' ':
        j+=' '+x[i+1].upper()
    elif x[i]!=' ' and x[i-1]!=' ':
        j+=x[i]
print(j)

#capitalising first letter:
n=''
n+=j[0].upper()+j[1:]
print(n)
