d=4
m=1
s=[4]
sum=0
count=0
for i in range(len(s)):
#    print('i:',i)
    sum=0
    
    for j in range(m):
#        print('i1:',i)
        if i==len(s):
            break
#        print(s[i])
        sum+=s[i]
#        print(sum)
        i+=1
        if sum==d and j+1==m:
            count+=1
#            print('count:',count)
print(count)