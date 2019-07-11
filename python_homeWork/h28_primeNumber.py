n=13
if n==0 or n==1:
    print("Not Prime")
else:
    for i in range(2,n+1):
        if n==i:
            print("Prime")
            break
        if n%i==0:
            print("Not Prime")
            break
        else:
            if i==n:
                print("Prime")
            else:
                continue