y=1918
if y==1918:
    print('26.09.'+str(y))
elif y<1918:
    if y%4==0:
        print('12.09.'+str(y))
    else:
        print('13.09.'+str(y))
else: 
    if y%4==0 and y%100!=0:
        print('12.09.'+str(y))
    elif y%400==0:
        print('12.09.'+str(y))
    else:
        print('13.09.'+str(y))
    