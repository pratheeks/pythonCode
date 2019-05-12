year=[1992,1995,2000,2005,2008,2016,2020,2021,2009,2000,1900]
for i in year:
    if i%4==0 and i%100!=0:
        print(i)
    elif i%400==0:
        print(i)