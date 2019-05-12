def staircase(n):
    for i in range(1,n+1):
        print(('#'*i).rjust(n))
    for i in range(1,n+1):
        a=(' '*(n-1))+('#'*i)
        n-=1
        print(a)
n = 6
staircase(n)
