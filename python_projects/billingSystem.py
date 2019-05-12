b=True
n=''
x=[]
y=[]
price=[]
#j=0
#k=0
#z=0
#h=0
#def moreItems():
#         print('Need more pizzas? y/n')
#         a=input()
#         if a=='y':
#             continue
#         else:
#             break
#-------------------------------------------------------------------------------------------    
def pizza_menu():
    sum=0
#    t=1
    l=[[1,'A',270,320,390],[2,'B',280,330,400],
       [3,'C',290,340,410],[4,'D',300,350,420],
       [5,'E',310,360,430],[6,'F',320,370,440]]
    print('Select from the menu:')
    
    b=True
    while b:
        
        print('*'.center(25,'*'))
        for i in l:
            print(i[0],'--->' ,i[1],'               *')
            print('   small ','medium',' large','*')
            print('   ',i[2],'   ',i[3],'   ',i[4],'*')
        print('*'.center(25,'*'))
        
#        b=False
       
        print('choose the pizza')
        p=input()
        if p=='1':
            print('choose the size')
            s=input()
            if s=='s':
                sum+=l[0][2]
                price.append(l[0][2])
            elif s=='m':
                sum+=l[0][3]
                price.append(l[0][3])
            elif s=='l':
                sum+=l[0][4]
                price.append(l[0][4])
#            print(sum)
            x.append(l[0][1])
            print(x)
            y.append(s)
            print(y)
            print(price)
            print('Need more pizzas? y/n')
            a=input()
            if a=='y':
#                t+=1
                continue
            else:
                break
            

        elif p=='2':
            print('choose the size')
            s=input()
            if s=='s':
                sum+=l[1][2]
                price.append(l[1][2])
            elif s=='m':
                sum+=l[1][3]
                price.append(l[1][3])
            elif s=='l':
                sum+=l[1][4]
                price.append(l[1][4])
#            print(sum)
            x.append(l[1][1])
            print(x)
            y.append(s)
            print(y)
            print(price)
            print('Need more pizzas? y/n')
            a=input()
            if a=='y':
#                t+=1
                continue
            else:
                break            
        elif p=='3':
            print('choose the size')
            s=input()
            if s=='s':
                sum+=l[2][2]
                price.append(l[2][2])
            elif s=='m':
                sum+=l[2][3]
                price.append(l[2][3])
            elif s=='l':
                sum+=l[2][4]
                price.append(l[2][4])
#            print(sum)
            x.append(l[2][1])
#            print(x)
            y.append(s)
#            print(y)
#            print(price)
            print('Need more pizzas? y/n')
            a=input()
            if a=='y':
#                t+=1
                continue
            else:
                break            
        elif p=='4':
            print('choose the size')
            s=input()
            if s=='s':
                sum+=l[3][2]
                price.append(l[3][2])
            elif s=='m':
                sum+=l[3][3]
                price.append(l[3][3])
            elif s=='l':
                sum+=l[3][4]
                price.append(l[3][4])
#            print(sum)
            x.append(l[3][1])
#            print(x)
            y.append(s)
#            print(y)
#            print(price)
            print('Need more pizzas? y/n')
            a=input()
            if a=='y':
#                t+=1
                continue
            else:
                break            
        elif p=='5':
            print('choose the size')
            s=input()
            if s=='s':
                sum+=l[4][2]
                price.append(l[4][2])
            elif s=='m':
                sum+=l[4][3]
                price.append(l[4][3])
            elif s=='l':
                sum+=l[4][4]
                price.append(l[4][4])
#            print(sum)
            x.append(l[4][1])
#            print(x)
            y.append(s)
#            print(y)
#            print(price)
            print('Need more pizzas? y/n')
            a=input()
            if a=='y':
#                t+=1
                continue
            else:
                break    
        elif p=='6':
            print('choose the size')
            s=input()
            if s=='s':
                sum+=l[5][2]
                price.append(l[5][2])
            elif s=='m':
                sum+=l[5][3]
                price.append(l[5][3])
            elif s=='l':
                sum+=l[5][4]
                price.append(l[5][4])
#            print(sum)
            x.append(l[5][1])
#            print(x)
            y.append(s)
#            print(y)
#            print(price)
            print('Need more pizzas? y/n')
            a=input()
            if a=='y':
#                t+=1
                continue
            else:
                break            
        else:
            print('Invalid choice, do you wish to continue?, y/n')
            a=input()
            if a!='y':
#                t=0
                print('\nThank you for visiting.\n')
                b=False

#    print('sum of the amount of pizza -->',sum)
#    print('total count of pizza -->',t)
    print()
#    global h,j
#    h=0
#    j=0
#    h=sum
#    j=t
#    print(h)
#    return h
#-------------------------------------------------------------------------------------------    
def drinks_menu():
    sum=0
    t=1
    l=[[1,'Pepsi',30,60,90],[2,'Coke ',40,70,90],
       [3,'Fanta',35,70,99],[4,'Bindu',25,50,75],
       [5,'Limca',20,35,65],[6,'SipOn',20,40,80]]
    print('Select drinks from the menu:')
    
    b=True
    while b:
        
        print('*'.center(25,'*'))
        for i in l:
            print(i[0],'--->' ,i[1],'               *')
            print('   quarter ','half',' full','     *')
            print('   ',i[2],'   ',i[3],'   ',i[4],'       *')
        print('*'.center(25,'*'))
        
#        b=False
       
        print('choose the drink:')
        p=input()
        if p=='1':
            print('choose the quatity:')
            s=input()
            if s=='q':
                sum+=l[0][2]
                price.append(l[0][2])
            elif s=='h':
                sum+=l[0][3]
                price.append(l[0][3])
            elif s=='f':
                sum+=l[0][4]
                price.append(l[0][4])
#            print(sum)
            x.append(l[0][1])
#            print(x)
            y.append(s)
#            print(y)
#            print(price)
            print('Need more drink? y/n')
            a=input()
            if a=='y':
                t+=1
                continue
            else:
                break
            

        elif p=='2':
            print('choose the quantity:\t')
            s=input()
            if s=='q':
                sum+=l[1][2]
                price.append(l[1][2])
            elif s=='h':
                sum+=l[1][3]
                price.append(l[1][3])
            elif s=='f':
                sum+=l[1][4]
                price.append(l[1][4])
#            print(sum)
            x.append(l[1][1])
#            print(x)
            y.append(s)
#            print(y)
#            print(price)
            print('Need more drinks? y/n')
            a=input()
            if a=='y':
                t+=1
                continue
            else:
                break            
        elif p=='3':
            print('choose the quantity:')
            s=input()
            if s=='q':
                sum+=l[2][2]
                price.append(l[2][2])
            elif s=='h':
                sum+=l[2][3]
                price.append(l[2][3])
            elif s=='f':
                sum+=l[2][4]
                price.append(l[2][4])
#            print(sum)
            x.append(l[2][1])
#            print(x)
            y.append(s)
#            print(y)
#            print(price)
            print('Need more drinks? y/n')
            a=input()
            if a=='y':
                t+=1
                continue
            else:
                break            
        elif p=='4':
            print('choose the quantity:')
            s=input()
            if s=='q':
                sum+=l[3][2]
                price.append(l[3][2])
            elif s=='h':
                sum+=l[3][3]
                price.append(l[3][3])
            elif s=='f':
                sum+=l[3][4]
                price.append(l[3][4])
#            print(sum)
            x.append(l[3][1])
#            print(x)
            y.append(s)
#            print(y)
#            print(price)
            print('Need more drinks? y/n')
            a=input()
            if a=='y':
                t+=1
                continue
            else:
                break            
        elif p=='5':
            print('choose the quantity')
            s=input()
            if s=='q':
                sum+=l[4][2]
                price.append(l[4][2])
            elif s=='h':
                sum+=l[4][3]
                price.append(l[4][3])
            elif s=='f':
                sum+=l[4][4]
                price.append(l[4][4])
#            print(sum)
            x.append(l[4][1])
#            print(x)
            y.append(s)
#            print(y)
#            print(price)
            print('Need more drinks? y/n')
            a=input()
            if a=='y':
                t+=1
                continue
            else:
                break    
        elif p=='6':
            print('choose the quantity')
            s=input()
            if s=='q':
                sum+=l[5][2]
                price.append(l[5][2])
            elif s=='h':
                sum+=l[5][3]
                price.append(l[5][3])
            elif s=='f':
                sum+=l[5][4]
                price.append(l[5][4])
#            print(sum)
            x.append(l[5][1])
#            print(x)
            y.append(s)
#            print(y)
#            print(price)
            print('Need more drinks? y/n')
            a=input()
            if a=='y':
                t+=1
                continue
            else:
                break            
        else:
            print('Invalid choice, do you wish to continue?, y/n')
            a=input()
            if a!='y':
                t=0
                print('\nThank you for visiting.\n')
                b=False

#    print('sum of the amount of drinks -->',sum)
#    print('total count of drinks -->',t)
    
    print()

#    global k,z
#    k=0
#    z=0
#    k=sum
#    z=t
#-------------------------------------------------------------------------------------------    
while b:
    n=input('Enter your name : \t')
    if len(n)==0:
        a=input('Invalid name.Do you want to continue? y/n')
        if a!='y':
            b=False
            print('Thank You for visiting')
    else:
        b=False
print()
print()
c='Welcome to Dominos'
print(c.center(60,'*'))
print()
print('Welcome Mr/Ms.',n,'. We are happy to serve you.')
#-------------------------------------------------------------------------------------------    
cat=[[1,'pizza'],[2,'drinks'],[3,'sides'],[4,'desserts'],[5,'exit']]
b=True
print()
while b:
    print('Choose the categories',end='\n\n')
    for i in cat:
        print(i[0],'.',i[1])
    choose_cat=input()
#-------------------------------------------------------------------------------------------    
    if choose_cat=='1':
        pizza_menu()
#        print('total amount of pizza=',h)
#        print('total pizza count=',j)
#        print(x)
#        print(y)
        print()
        print('Need more items? y/n')
        a=input()
        if a=='y':
#           t+=1
            continue
        else:
            break 
#-------------------------------------------------------------------------------------------    
    elif choose_cat=='2':
        drinks_menu()
#        print('total amount of drinks=',k)
#        print('total drink count=',z)
#        print(x)
#        print(y)
        print()
        print('Need more items? y/n')
        a=input()
        if a=='y':
#           t+=1
            continue
        else:
            break 
#-------------------------------------------------------------------------------------------    
    elif choose_cat=='3':
        pass
        print('Need more items? y/n')
        a=input()
        if a=='y':
#           t+=1
            continue
        else:
            break 
#-------------------------------------------------------------------------------------------    
    elif choose_cat=='4':
        pass
        print('Need more items? y/n')
        a=input()
        if a=='y':
#           t+=1
            continue
        else:
            break 
#-------------------------------------------------------------------------------------------    
    elif choose_cat=='5':
        pass
        print('Need more items? y/n')
        a=input()
        if a=='y':
#           t+=1
            continue
        else:
            break 
#-------------------------------------------------------------------------------------------    
    else:
        print('Invalid choice, do you wish to continue?, y/n')
        a=input()
        if a!='y':
            print('Thank you for visiting')
            b=False
#-------------------------------------------------------------------------------------------    
print()
#item=j+z
#print('total items count:',item)
#tsum=h+k
#print('total amount of items:',tsum)
#print(list(x))
#print(list(y))
#print(price)
totl=0
print('No.','Item','   Quantity','price')    
for i in range(len(x)):
    print(i,'  ',x[i],'    ',y[i],'   ', price[i])
    totl+=price[i]
print('total amount in cart is=',totl)
 