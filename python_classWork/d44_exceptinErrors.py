l = ['a',2,5,'c','D']
for i in l:
    try:
        print(i/0)
    except TypeError :
        print("cannot be divisible by no.s" )
    except ZeroDivisionError :
        print("cannot be divisible by zero" )
    except :
        print("cannot be divisible" )
    