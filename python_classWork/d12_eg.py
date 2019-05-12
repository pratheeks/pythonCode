n=int(input('enter the no.?'))
if n%3==0 and n%5==0:
    print('FuZZ BUZZ')
elif n%5==0:
    print('BUZZ!')
elif n%3==0:
    print('FUZZ!')
else:
    print('Get Out;')
