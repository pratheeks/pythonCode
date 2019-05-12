import sys
l=['hello',1,2,0,"Bye"]
for i in l:
    try:
        print("The value of i:",i)
        r=1/int(i)
        print("Output:",r)
        print()
    except:
        print("The exception is:",sys.exc_info()[0])
        print()