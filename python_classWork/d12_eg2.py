num=[2,22,27,29,35,42,8,75,88]
for n in num:
    if n%3==0 and n%5==0:
        print(n,'FuZZ BUZZ')
    elif n%5==0:
        print(n,'BUZZ!')
    elif n%3==0:
        print(n,'FUZZ!')

