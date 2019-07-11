#Count Negative Integers in Row/Column-Wise Sorted Matrix:

l=[ [-3,-2,-1,1],
    [-2,2,3,4],
    [4,5,7,8] ]
n=3
m=4
cnt=0
i=0
j=m-1
while i<n and j>=0:
    if l[i][j]<0:
        cnt+=j+1
        i+=1
    else:
        j-=1
print(cnt)

