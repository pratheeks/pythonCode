def cart_menu():
    print()
    print('#'.center(50,'#'))
    print()
    print('****'.center(50,'*'))
    print('CART'.center(50,' '))
    print('****'.center(50,'*'))
    print()
    print('SI   Item    Size    Quantity    Price   Total')
    print('-'.center(50,'-'))
    print()
    j=1
    totl=0
    for i in t:
        print(j,'  ',i[1],' ',i[2],'    ',i[3],'         ',i[4],'   ',i[5])
        j=j+1
        totl+=i[5]   
    print()
    print('-'.center(50,'-'))
    print()
    print('Total Amount of the Cart items=',totl)
    l=input('Do you wish to remove any items?y/n:\t')
    print()
    if l=='y':
        c=int(input('Enter the SI no of item you wish to remove:\t'))
        c=c-1
        t.pop(c)  
        print()      
        j=1
        totl=0
        for i in t:
                j=j+1
                totl+=i[5]        
        print()
        print('Total Amount of the Cart =',totl)
        print()    
    print('1.Menu     2.Bill')
    print()
    a=input('Enter the option...\t')
    print()
    if a=='1':
        if y!='y':
            print()
#            break
    elif a=='2':
        print('$$$'.center(50,'$'))
        print('Bill'.center(50,' '))
        print('$$$'.center(50,'$'))
        print()
        print('SI   Item    Size    Quantity    Price   Total')
        print('-'.center(50,'-'))
        print()
        j=1
        totl=0
        for i in t:
            print(j,'  ',i[1],' ',i[2],'    ',i[3],'         ',i[4],'   ',i[5])
            j=j+1
            totl+=i[5]   
        print()
        print('-'.center(50,'-'))
        print()
        print('Total Amount of the Cart items=',totl)
        print()
        print('1.To Menu   2.Back to Cart')
        print()
        a=input('Enter the option...\t')
        print()
        if a=='1':
            if y!='y':
                print()
        elif a=='2':
            cart_menu()
#        l=input('Do you wish to remove any items?')
#        print()
#        print(t)
#        if l=='y':
#            c=int(input('Enter the SI no of item you wish to remove:'))
#            c=c-1
#            print(t.pop(c))   
##            for i in range(len(i[2])):
##                print(i)
##                c=int(input('Enter the SI no of item you wish to remove:'))
##                print('c',c)
##                if c==i:
##                    print('i',i)
##                    print(t[i])
##                    del t[i]
#            print()      
#            j=1
#            totl=0
#            for i in t:
#                    print(j,'  ',i[1],' ',i[2],'    ',i[3],'         ',i[4],'   ',i[5])
#                    j=j+1
#                    totl+=i[5]        
#            print()
#            print('Total Amount of the Cart items is ',totl)
                
    else:
            f=input('Invalid Choice! Do you wish to continue? y/n\t')
            if f!='y':
                print()                
#----------------------------------------------------------------------------------
def desserts_menu():
    l=[[1,'Jamun1',15,30],
       [2,'Jamon2',20,40]]
    print('\n  Select from the menu')
    while True:
        print('-'.center(25,'-'))
        for i in l:
            print(i[0],i[1].center(20,' '))
            print()
            print('    small        large')
            print()
            print('   ',i[2],'          ',i[3])
            print()
        print('-'.center(25,'-'))
        p=input('Choose the Desserts?:\t')
        if p=='1':
            s=input('Choose the size? s/l:\t')
            if s=='s':
                q=int(input('Choose Quantity?\t'))
                n=q*15
                x=[1,'Jamun1','s',q,15,n]
            elif s=='l':
                q=int(input('Choose Quantity?\t'))
                n=q*30
                x=[1,'Jamun1','l',q,30,n]
            else:
                f=input('Invalid Choice! Do you wish to continue? y/n:\t')
                if f!='y':
                    break
                else:
                    continue
            t.append(x)
            x=[]
        elif p=='2':
            s=input('Choose the size? s/l:\t')
            if s=='s':
                q=int(input('Choose Quantity:\t'))
                n=q*20
                x=[2,'Jamon2','s',q,20,n]
            elif s=='l':
                q=int(input('Choose Quantity:\t'))
                n=q*40
                x=[2,'Jamon2','l',q,40,n]
            else:
                f=input('Invalid Choice! Do you wish to continue? y/n:\t')
                if f!='y':
                    print()
                    break
                else:
                    continue
            t.append(x)
            x=[]
        else:
            f=input('Invalid Choice! Do you wish to continue? y/n:\t')
            if f!='y':
                break
            else:
                continue
        g=input('Need more Desserts? y/n:\t')
        print()
        if g=='y':
            continue
        else:
            print()
            break
#----------------------------------------------------------------------------------
def sides_menu():
    l=[[1,'Sides1',30,60],
       [2,'Sides2',40,80]]
    print('\n  Select from the menu')
    while True:
        print('-'.center(25,'-'))
        for i in l:
            print(i[0],i[1].center(20,' '))
            print()
            print('    small        large')
            print()
            print('   ',i[2],'          ',i[3])
            print()
        print('-'.center(25,'-'))
        p=input('Choose the Sides?:\t')
        if p=='1':
            s=input('Choose the size? s/l:\t')
            if s=='s':
                q=int(input('Choose Quantity?\t'))
                n=q*30
                x=[1,'Sides1','s',q,30,n]
            elif s=='l':
                q=int(input('Choose Quantity?\t'))
                n=q*60
                x=[1,'Sides1','l',q,60,n]
            else:
                f=input('Invalid Choice! Do you wish to continue? y/n:\t')
                if f!='y':
                    break
                else:
                    continue
            t.append(x)
            x=[]
        elif p=='2':
            s=input('Choose the size? s/l:\t')
            if s=='s':
                q=int(input('Choose Quantity:\t'))
                n=q*40
                x=[2,'Sides2','s',q,40,n]
            elif s=='l':
                q=int(input('Choose Quantity:\t'))
                n=q*80
                x=[2,'Sides2','l',q,80,n]
            else:
                f=input('Invalid Choice! Do you wish to continue? y/n:\t')
                if f!='y':
                    print()
                    break
                else:
                    continue
            t.append(x)
            x=[]
        else:
            f=input('Invalid Choice! Do you wish to continue? y/n:\t')
            if f!='y':
                break
            else:
                continue
        g=input('Need more Sides? y/n:\t')
        print()
        if g=='y':
            continue
        else:
            print()
            break
#----------------------------------------------------------------------------------
def drinks_menu():
    l=[[1,'Drink1',50,100],
       [2,'Drink2',60,120]]
    print('\n  Select from the menu')
    while True:
        print('-'.center(25,'-'))
        for i in l:
            print(i[0],i[1].center(20,' '))
            print()
            print('    small        large')
            print()
            print('   ',i[2],'          ',i[3])
            print()
        print('-'.center(25,'-'))
        p=input('Choose the Drink?:\t')
        if p=='1':
            s=input('Choose the size? s/l:\t')
            if s=='s':
                q=int(input('Choose Quantity?\t'))
                n=q*50
                x=[1,'Drink1','s',q,50,n]
            elif s=='l':
                q=int(input('Choose Quantity?\t'))
                n=q*100
                x=[1,'Drink1','l',q,100,n]
            else:
                f=input('Invalid Choice! Do you wish to continue? y/n\t')
                if f!='y':
                    break
                else:
                    continue
            t.append(x)
#            print(t)
            x=[]
        elif p=='2':
            s=input('Choose the size? s/l:\t')
            if s=='s':
                q=int(input('Choose Quantity:\t'))
                n=q*60
                x=[2,'Drink2','s',q,60,n]
            elif s=='l':
                q=int(input('Choose Quantity:\t'))
                n=q*120
                x=[2,'Drink2','l',q,120,n]
            else:
                f=input('Invalid Choice! Do you wish to continue? y/n:\t')
                if f!='y':
                    print()
                    break
                else:
                    continue
            t.append(x)
            x=[]
        else:
            f=input('Invalid Choice! Do you wish to continue? y/n:\t')
            if f!='y':
                break
            else:
                continue
        g=input('Need more Drinks? y/n:\t')
        print()
        if g=='y':
            continue
        else:
            print()
            break
#----------------------------------------------------------------------------------
x=[]
t=[]
def pizza_menu():
    l=[[1,'Veggie',200,230,250],
       [2,'NonVeg',220,260,300]]
    print('\n  Select from the menu')
    while True:
        print('-'.center(25,'-'))
        for i in l:
            print(i[0],i[1].center(25,' '))
            print()
            print('    small  medium  large')
            print()
            print('   ',i[2],'   ',i[3],'   ',i[4])
            print()
        print('-'.center(25,'-'))
        p=input('Choose the Pizza?\t')
        if p=='1':
            s=input('Choose the size?\t')
            if s=='s':
                q=int(input('Choose Quantity?\t'))
                n=q*200
                x=[1,'Veggie','s',q,200,n]
            elif s=='m':
                q=int(input('Choose Quantity?\t'))
                n=q*230
                x=[1,'Veggie','m',q,230,n]
            elif s=='l':
                q=int(input('Choose Quantity?\t'))
                n=q*250
#                print(n)
                x=[1,'Veggie','l',q,250,n]
            else:
                f=input('Invalid Choice! Do you wish to continue? y/n\t')
                if f!='y':
                    break
                else:
                    continue
            t.append(x)
#            print(t)
            x=[]
        elif p=='2':
            s=input('Choose the size?\t')
            if s=='s':
                q=int(input('Choose Quantity:\t'))
                n=q*220
                x=[2,'NonVeg','s',q,220,n]
            elif s=='m':
                q=int(input('Choose Quantity:\t'))
                n=q*260
                x=[2,'NonVeg','m',q,260,n]
            elif s=='l':
                q=int(input('Choose Quantity:\t'))
                n=q*300
                x=[2,'NonVeg','l',q,300,n]
            else:
                f=input('Invalid Choice! Do you wish to continue? y/n:\t')
                if f!='y':
                    print()
                    break
                else:
                    continue
            t.append(x)
#            print(t)
            x=[]
        else:
            f=input('Invalid Choice! Do you wish to continue? y/n:\t')
            if f!='y':
#                print('Thank You For Visiting.')
                break
            else:
                continue
        g=input('Need more Pizzas? y/n:\t')
        print()
        if g=='y':
            continue
        else:
            print()
            break
#-----------------------------------------------------------------------
f=True
while f:
    a=input('Enter Name:')
    print()
    if len(a)==0:
        b=input('Invalid. Do you wish to continue??? y/n:\t')
        if b=='y':
            continue
        else:
            print()
            print('Thank you for visiting!')
            print()
            break
    else:
        print('#'.center(60,'#'))
        print('Welcome to PizzaWorld!!'.center(60,' '))
        print('#'.center(60,'#'))
        print()
        print('Welcome Mr.',a,'.We are happy to serve you.')
        print()
        print('Choose your Menu?')
        cat=[[1,'. Pizza'],[2,'. Drinks'],[3,'. Sides'],[4,'. Desserts'],[5,'. Cart']]    
        x=True
        while x:
            print('-----------------')
            for i in cat:
                print(i[0],i[1])
            print('-----------------')
            choice=input('Enter the Menu:\t')
            if choice=='1':
                pizza_menu()
                y=input('Go to Menu? y/s:\t')
                print()
                if y!='y':
                    print('Thank You.Visit Again!')
                    f=False
                    x=False
            elif choice=='2':
                drinks_menu()
                y=input('Go to Menu? y/s:\t')
                print()
                if y!='y':
                    print('Thank You.Visit Again!')
                    f=False
                    x=False
            elif choice=='3':
                sides_menu()
                y=input('Go to Menu? y/s:\t')
                print()
                if y!='y':
                    print('Thank You.Visit Again!')
                    f=False
                    x=False
            elif choice=='4':
                desserts_menu()
                y=input('Go to Menu? y/s:\t')
                print()
                if y!='y':
                    print('Thank You.Visit Again!')
                    f=False
                    x=False
            elif choice=='5':
                cart_menu()
                y=input('Go to Menu? y/s:\t')
                print()
                if y!='y':
                    print()
                    print('Thank You.Visit Again!')
                    print()
                    f=False
                    x=False
            else:
                d=input('Invalid.Choose Menu? y/n:\t')
                print()
                if d!='y':
                    print()
                    print('Thank you for Visting.')
                    print()
                    f=False
                    x=False
