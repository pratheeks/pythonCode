a='ThiS is Me Pratik'
for i in a:
    if i.islower():
        b=i.upper()
    elif i.isupper():
        b=i.lower()
    else:
        b=i
    print(b,end='')
#method2:
    
s=input("Enter the string\n")
j=''
for i in s:
    if i>='A' and i<='Z':
        j+=i.lower()
    elif i>='a' and i<='z':
        j+=i.upper()
    else:
        j+=i
print(j)