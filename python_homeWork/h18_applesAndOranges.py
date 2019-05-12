def countApplesAndOranges(s, t, a, b, apples, oranges):
    l=[]
    l1=[]
    x=y=0
    for i in apples:
        l.append(a+i)
    print(l)
    for j in oranges:
        l1.append(b+j)
    print(l1)
    for i in l:
        if i>=s and i<=t:
            x+=1
    print(x)
    for i in l1:
        if i>=s and i<=t:
            y+=1
    print(y)

#st = input().split()

s = 7       #int(st[0])

t = 11      #int(st[1])

#ab = input().split()

a = 5        #int(ab[0])

b = 15      #int(ab[1])

#mn = input().split()

m = 3           #int(mn[0])

n = 2           #int(mn[1])

apples = [-2,2,1]           #list(map(int, input().rstrip().split()))

oranges = [5,-6]            #list(map(int, input().rstrip().split()))

countApplesAndOranges(s, t, a, b, apples, oranges)