
# Complete the breakingRecords function below.
def breakingRecords(a):
    maxC=0
    minC=0
    max=a[0]
    min=a[0]
    for i in range(len(a)):
        if a[i]>max:
            max=a[i]
#            print(max)
            maxC+=1
        if a[i]<min:
            min=a[i]
#            print(min)
            minC+=1
    print(maxC,minC)
#n = int(input())
n=9

#scores = list(map(int, input().rstrip().split()))
scores = [10,5,20,20,4,5,2,25,1]

result = breakingRecords(scores)
  