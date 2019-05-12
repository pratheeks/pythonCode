x,y=map(int,input().split())

for i in range(1,x,2):
    print(('.|.'*i).center(y,'-'))
print('WELCOME'.center(y,'-'))
for i in range(1,x,2):
    print(('.|.'*(x-1-i)).center(y,'-'))