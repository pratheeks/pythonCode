def diagonalDifference(arr):
    x=0
    y=0
    for i in range(n):
        x+=arr[i][i]
        y+=arr[i][(n-1-i)]
    print(x)
    print(y)
    l=x-y
    if l>0:
        return l
    else:
        return -l
    


n = 3#int(input())

arr = []

for _ in range(n):
#    arr.append(list(map(int, input().rstrip().split())))
    arr=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(arr)

result = diagonalDifference(arr)
print(result)