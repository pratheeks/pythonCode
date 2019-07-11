# method1:
n=[3,2,1]
n=[1,2,3,4,5]
mul=1

for i in n:
    mul*=i
# print(mul)
l=[]
for i in range(len(n)):
    l.append(mul//n[i])
print(l)

#-------------------------------------#
# method2:
l=[]
mul=1
for i in range(len(n)):
    mul=1
    for j in range(len(n)):
        if i!=j:
            # print(n[j])
            mul*=n[j]
    l.append(mul)
print(l)