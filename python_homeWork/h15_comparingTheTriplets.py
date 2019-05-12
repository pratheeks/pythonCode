def compareTriplets(a, b):
    x=0
    y=0
    for i in range(len(a)):
        if a[i]>b[i]:
            x+=1
        elif a[i]<b[i]:
            y+=1
        elif a[i]==b[i]:
            continue
    print (x,y)
            
a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))

result = compareTriplets(a, b)

