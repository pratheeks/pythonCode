q=[1,2,9,9]
ans=[0 for _ in range(len(q))]
print(ans)
carry=1
sum=0
l=len(q)-1

for i in range(l,-1,-1):
    sum=q[i]+carry
    if sum==10:
        carry=1
    else:
        carry=0
    ans[i]=sum%10
if carry==1:
    ans.insert(0,1)
print(ans)
