
n=552

s=''
while n>0:
    if n%26!=0:
        s+=chr(64+(n%26))
        n=n//26
    else:
        s+='Z'
        n=n//26-1
print(s[::-1])