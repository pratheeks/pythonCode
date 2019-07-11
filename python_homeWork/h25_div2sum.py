#nk=input().split()
n=6
k=3

a=0
ar=[1,3,2,6,1,2]

for i in range(len(ar)):
    for j in range(i+1,len(ar)):
        print(ar[i],ar[j])
        sum=ar[i]+ar[j]
        try:
            if sum%k==0:
                a+=1
                print(a)
        except ZeroDivisionError:
            print(a)