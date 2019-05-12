def miniMaxSum(arr):
    minSum=maxSum=0
    for i in range(len(arr)):
        minSum+=arr[i]
        maxSum+=arr[i]
#    minSum=minSum-max(arr)
    minSum=minSum-arr[-1]
#    maxSum=maxSum-min(arr)
    maxSum=maxSum-arr[0]
    print(minSum)
    print(maxSum)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
