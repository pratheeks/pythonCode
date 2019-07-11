n=8
s='UDDDUDUU'
cnt=0
val=0
for i in s:
    if i=='U':
        cnt+=1
        if cnt==0:
            val+=1
    elif i=='D':
        cnt-=1
print(val)


