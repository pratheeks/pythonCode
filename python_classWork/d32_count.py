# a=input('Enter the input:\n').lower()
a='this is#$'
print()
print(a)
print()
i=0
c=0
while i<len(a):
    if a[i]==' ' and a[i+1]!=' ':
        c+=1
        i+=1
    else:
        i+=1
print('Words:',c+1)

vwl=0
csnt=0
numb=0
spcl=0
i=0
sp=0
while i<len(a):
    if a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u':
        vwl+=1
    elif a[i]>='a' and a[i]<='z':
        csnt+=1
    elif a[i]>='0' and a[i]<='9':
        numb+=1
    elif a[i]!=' ':
        spcl+=1
    else:
        sp+=1
    i+=1
#print(vwl,csnt,numb,spcl)
print('Vowels:',vwl)
print('Consonent:',csnt)
print('Numbers:',numb)
print('SpecialChar:',spcl)
print('SpaceCount:',sp)
print('SpaceB/wWords:',c)