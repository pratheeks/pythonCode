n=4
l=[]
l=["qwertyuioplkjhgfdsazxcvbnm","hgfdaaaasa"]
# for i in range(n):
#     l.append(input("Enter the input"))
# print(l)
L=[]
for i in l:
    L.append(''.join(sorted(set((i.lower())))))
print(L)

x=[]
for i in L:
    if len(i)==26:
        print(i,"=> Panagram")
        # for j in i:
        #     if j not in x:
        #         x.append([l.count(j),j])
        #         print(x)
    else:
        print(i,"=> not Panagram")
    
        