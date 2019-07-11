k=3
l=[4,1,5,2,3,0,10]
max3=l[:3]
print(max3)

for i in range(k,len(l)):
    # print(l[i])
    m=(max(max3))
    # print(m)
    if m>=l[i]:
        # max3.index(max(max3))=i
        max3[max3.index(m)]=l[i]
print(max3)