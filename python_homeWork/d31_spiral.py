a=[
    [1,2,3,4],
    [5,6,7,8,],
    [9,10,11,12],
    [13,14,15,16],
    [17,18,19,20],
    [21,22,23,24]
]


top=left=0
bottom=len(a)-1
right=len(a[1])-1

while top<=bottom and left<=right:
    for i in range(left,right+1):
        print(a[top][i])
    top+=1
    
    for i in range(top,bottom+1):
        print(a[i][right])
    right-=1
    
    for i in range(right,left-1,-1):
        print(a[bottom][i])
    bottom-=1
    
    for i in range(bottom,top-1,-1):
        print(a[i][left])
    left+=1
   
        

'''
for i in a:
    print(i)
le=len(a[0])-1
l=[]
for i in range(len(a)):
    for j in range(len(a[i])):

        if a[i][j]==a[-1][j]:
#            print('btm',a[i][3-j])
            l.append(a[i][3-j])

        elif a[i][j]==a[i][-1]:
#            print('rsd',a[i][j])
            l.append(a[i][j])
            
        elif a[i][j]==a[0][j]:
#            print('top',a[i][j])
            l.append(a[i][j])
#print(l)
for i in range(len(a)):    
    for j in range(len(a[i])): 
        if a[i][j]==a[i][0]:
#            print('lsde',a[le-i][j])
            if a[le-i][j] not in l:
                l.append(a[le-i][j])
#print(l)            
for i in range(len(a)):    
    for j in range(len(a[i])):
        if a[i][j]==a[1][j]:
#            print('*',a[i][j])
            if a[i][j] not in l:
                l.append(a[i][j])
#        
        elif a[i][j]==a[i][le-1]:
#            print('$',a[i][j])
            if a[i][j] not in l:
                l.append(a[i][j])
for i in range(len(a)):    
    for j in range(len(a[i])):
        if a[i][j]==a[-2][j]:
#            print('@',a[i][3-j])
            if a[i][3-j] not in l:
                l.append(a[i][3-j])
print(l)
for i in a:
    for j in i:
        if j not in l:
            l.append(j)
            
print(l)
                
                
'''             