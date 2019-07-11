points=[(-2,4),(0,-2),(-1,0),(3,5),(-2,-3),(3,2)]
k=2
points_with_d=[]
dict={}
for i,j in points:
    # print(i,j)
    dict['c']=(i,j)
    d=(i**2 + j**2)**0.5
    # print('{:.5}'.format(d))
    dict['d']=d
    # print(dict)
    points_with_d.append(dict.copy())
# print(points_with_d)
# print(type(dicts))

max3=points_with_d[:k]
# print(max3)
l=[]
for i in max3:
    l.append(i.values())
#     m=max(l)
# print(l)
# # print(m)
# ind=l.index(m)
# # print(max3[ind])

for i in range(k,len(points_with_d)):
    l=[]
    for j in max3:
        l.append(j['d'])
        m=max(l)
    # print(l)
    # print(m)
    ind=l.index(m)
    # print(max3[ind])
    p=points_with_d[i]['d']
    # print(p)

    if m>p:
        # print(m,p)
        max3[ind]=points_with_d[i]

print(max3)