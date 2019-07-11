def check(func):
    def inner(a,b):
        print("Inner")
        if b==0:
            print("Cannot Divide")
            return
        return func(a,b)
    return inner

@check
def divide(a,b):
    return a/b
#d=check(divide)
 
#print(d(5,10)) 
print(divide(5,10))

