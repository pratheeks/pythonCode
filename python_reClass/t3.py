a='this is my class'
i=0
count=0
temp=''
st=''
while i<len(a):
    if a[i]>='a' and a[i]<='z':
        count+=1
        st+=a[i]
        i+=1
    elif a[i]==' ':
        temp+=st[0].upper()+st[1:]+str(count)+' '
        count=0
        st=''
        i+=1
temp+=st[0].upper()+st[1:]+str(count)+' '
print(temp)
