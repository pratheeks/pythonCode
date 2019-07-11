s=1231234567890
print(s)
x=''
for num in range(len(str(s))):
    r=s%10
    x+=str(r)
    s=s//10
print(x)