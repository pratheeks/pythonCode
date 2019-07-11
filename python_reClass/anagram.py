n=int(input("Enter the number"))
l=[]
# l=["asdfg","hgfdsa"]
for i in range(n):
    l.append(input("Enter the input"))
print(l)
L=[]
for i in l:
    L.append(''.join(sorted(i.lower())))
print(L)


for i in range(len(L)):
    # print(i)
    for j in range(i+1,len(L)):
        # print(1,j)
        if L[i]==L[j]:
            print((l[i],l[j]),"Anagram")
        else:
            print((l[i],l[j]),"NOT Anagram")
        