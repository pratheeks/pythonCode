#x=input()
#size=list(map(int,input().split(' ')))
size=[2,3,4,5,6,8,7,6,5,18]

#n=int(input())
#xi=[]
#sp=[]
#for i in range(n):
#    xi+=list(map(int,input().split(' ')))
#    sp.append(xi)
#    xi=[]
sp=[[6,55],
[6,45],
[6,55],
[4,40],
[18,60],
[10,50]]
total=0
for i in sp:
#    print(i)
    if i[0] in size:
        total+=i[1]
        size.remove(i[0])
print(total)


'''
from collections import Counter
X = input()
S = Counter(map(int,input().split()))
print(S)
N = int(input())
earnings = 0
for customer in range(N):
    size, x_i = map(int,input().split())
    print(size,x_i)
    if size in S and S[size] > 0:
        S[size] -= 1
        earnings += x_i
            
print(earnings)
'''