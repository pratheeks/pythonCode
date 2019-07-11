b=10
keyboards=[3,1]
drives=[5,2,8]
x=-1
for i in keyboards:
    for j in drives:
        if i+j<=b:
            x=max(x,i+j)
print(x)
