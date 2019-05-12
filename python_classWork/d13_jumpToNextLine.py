a=list(range(1900,2000))
for l in a:
    if l%4==0 and l%100!=0 or l%400==0:
        if l%7==0:
            print("VERY UNLUCKY YEAR",end= ' ')
        else:
            print("Leap Year",end= ' ')
    elif l%3==0 and l%5==0:
        print("FuzzzzBuzzzz")
    elif l%3==0:
        print("Fuzzzzz",end=' ')
    elif l%5==0:
        print("Buzzzzz",end=' ')
    elif l%7==0:
        print("Complex",end=' ')
    else:
        print(l,end=' ')
