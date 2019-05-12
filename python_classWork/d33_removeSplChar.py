s='This i@s m|y c4la1s@s3'
j=''
for i in s:
    if i>='A' and i<='Z':
        j+=i
    elif i>='a' and i<='z':
        j+=i
    elif i==' ' :
        j+=i
print(j)
#method1:
t=''
for i in s:
    if (i>='A' and i<='Z') or (i>='a' and i<='z') or i==' ':
        t+=i
print(t)
#Method2:
k=''
for i in s:
    if i.isalpha():
        k+=i
    elif i==' ':
        k+=i
print(k)
