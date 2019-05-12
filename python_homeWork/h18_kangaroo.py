
# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if x2>x1 and v2>=v1:
        print('NO')
    else:
        while(x2>x1):
            x1+=v1
            x2+=v2
            if x1==x2:
                print('YES')
            elif x1>x2:
                print('NO')
    
    '''  try:
        w=((x2-x1)/(v1-v2))
        if x2>x1 and v2>=v1:
            print("NO")
        elif w==int(w):
            print("YES")
        else:
            print("NO")
    except ZeroDivisionError:
        print("NO")
 '''       
'''   
    else:
        while x1<x2:
            x1+=v1
            x2+=v2
            if x1==x2:
                print("YES")
            else:
                continue
                print("NO")
'''
x1 = 21

v1 = 6

x2 = 47

v2 =3

result = kangaroo(x1, v1, x2, v2)

   
