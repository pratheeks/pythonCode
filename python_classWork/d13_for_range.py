a=list(range(357))
for i in a:
    if i%3==0:
        print(i,'FUZZ')
    elif i%5==0:
        print(i,'Buzz')
    else:
        print(i)