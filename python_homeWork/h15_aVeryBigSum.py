def aVeryBigSum(ar):
    x=0
    for i in ar:
        x+=i 
    return x


#ar_count = int(input())

ar = list(map(int, input().rstrip().split()))
#print('ar:',ar)
result = aVeryBigSum(ar)
print(result)
