'''
n=int(input())
try:
    if n<0:
        raise ValueError("Negative!!!")
    else:
        print("Positive!")

except ValueError as v:
    print(v)

'''    
    
n=input()
try:
    if n in '0123456789':
        raise TypeError("Invalid Input")
    else:
        print(n)
except TypeError as t:
    print(t)
    
