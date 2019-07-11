n=3


l=[[0]*n for i in range(n)]

num=n*n

top=left=0
bottom=right=n-1

while top<=bottom and left<=right:
    for i in range(left,right+1):
        l[top][i]=num
        num-=1
    top+=1
    
    for i in range(top,bottom+1):
        l[i][right]=num
        num-=1
    right-=1
    
    for i in range(right,left-1,-1):
        l[bottom][i]=num
        num-=1
    bottom-=1
    
    for i in range(bottom,top-1,-1):
        l[i][left]=num
        num-=1
    left+=1
   
        
print(l)


'''
n=4
l=[]
w=1

for i in range(n):
    for j in range(n):
        if i==0:            
            N=n*n-j
            l.append(n*n-j)
a=[]
for i in range(n):
    for j in range(n):
        if j==n-1 and w<n-1:
            w+=1
            N=N-1
            a.append(N)
c=[]
i=1
for i in range(n):
    for j in range(n):
        if i==n-1:
            N=N-1
            c.append(N)
b=[]
w=1
for i in range(n):
    for j in range(n):
        if j==0 and w<n-1:
            w+=1
            N=N-1
            b.append(N)
print(l)
print(a)
print(c)
print(b)

'''