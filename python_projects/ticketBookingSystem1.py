from datetime import datetime
import mysql.connector
x=[]
#-----------------------------------------------------------------------------------
def logic():
    global se_dic,x1,s,seat_cnt,ex
    se_dic={
            'a':[1,2,3,4,5,6,7,8,9,10],
            'b':[1,2,3,4,5,6,7,8,9,10],
            'c':[1,2,3,4,5,6,7,8,9,10],
            'd':[1,2,3,4,5,6,7,8,9,10],
            'e':[1,2,3,4,5,6,7,8,9,10],
            'f':[1,2,3,4,5,6,7,8,9,10],
            'g':[1,2,3,4,5,6,7,8,9,10],
            'h':[1,2,3,4,5,6,7,8,9,10]
               }
    seat_show()  
    f=True 
    x1=[] 
    while f:   
        try:
            seat_cnt=int(input("Select the no. of seats."))
            if seat_cnt>10 or seat_cnt<=0:
                raise ValueError
        except ValueError:
            joker=input("Invalid. Do you wish to continue?y/n:\t ")
            if joker=='y':
                continue
            else:
                print()
                print("Thank You!".center(60,'-'))
                break
                
        s=seat_cnt
        calling()
        if ex==1:
            a=input("Do you wish to continue? y/n:\t")
            if a=='y':
                continue
            else:
                print()
                print("Thank You!".center(60,'-'))
                break
        seat_show()
        full=input("Confirm ticket? y/n:")
        print()
        if full=='y':
            ticket()
            print()
            print("Thank You!".center(60,'-'))
            f=False
        else:
            print("Thank You!".center(60,'-'))
            break              
#-------------------------------------------------------------------------------
def English():
    b=True
    english=[[1,'Avengers: End Game','English'],[2,"Avengers: Infinity War",'English'],
             [3,'The Avengers','English']]
    print('-'.center(50,'-'))
    print("MOVIES:")
    for a in english:
        print(a[0],a[1])
    
    while b:
        print()
        a=input("Enter the Movie Choice:\t")
        if a not in '123' or len(a)!=1:
            que=input("Invalid Input. Continue? y/n:\t")
            if que=='y':
                continue
            else:
                print("Thank You!".center(60,'-'))
            break
        else:
            i=int(a)
            t=english[i-1]
            x.append(t)
            Location()
            b=False
#-----------------------------------------------------------------------
def Hindi():
    b=True
    hindi=[[1,'HindiMedium','Hindi'],[2,"Kala",'Hindi'],[3,'Luka Chuppi','Hindi']]
    print('-'.center(50,'-'))
    print("MOVIES:")
    for a in hindi:
        print(a[0],a[1])
    while b:
        print()
        a=input("Enter the Movie Choice:\t")
        if a not in '123' or len(a)!=1:
            que=input("Invalid Input. Continue? y/n:\t")
            if que=='y':
                continue
            else:
                print("Thank You!".center(60,'-'))
            break
        else:
            v=int(a)
            t=hindi[v-1]
            x.append(t)
            print()
            Location()
            b=False       
#-------------------------------------------------------------------
def Kannada():
    b=True
    kannada=[[1,'99',"Kannada"],[2,"TV9","Kannada"],[3,'kannada2',"Kannada"]]
    print('-'.center(50,'-'))
    print("MOVIES:")
    for a in kannada:
        print(a[0],a[1])
    while b:
        a=input("Enter the Movie Choice:\t")
        print()
        if a not in '123' or len(a)!=1:
            que=input("Invalid Input. Continue? y/n:\t")
            if que=='y':
                continue
            else:
                print("Thank You!".center(60,'-'))
            break
        else:
            v=int(a)
            t=kannada[v-1]
            x.append(t)
            Location()
            b=False
#---------------------------------------------------------------------
def Location():
    l=[[1,'Cinepolis, Bengaluru'],
       [2,'PVR: 4DX, Dr Rajkumar Road'],
       [3,'PVR, Whitefield Road']]
    print('-'.center(50,'-'))
    print("LOCATION:")
    for i in l:
        print(i[0],i[1])  
    b=True
    while b:
        n=input("Enter your Choice: \t")
        print()
        if n.isdigit() and n <'4' and len(n)==1 :
            if n=='1':
                print("Cinepolis,Bengaluru")
            elif n=='2':
                print('PVR, Dr Rajkumar Road')
            elif n=='3':
                print('PVR, Whitefield Road')
            print()
            v=int(n)
            t=l[v-1]
            x.append(t)
            Time()
            break
        else:
            que=input("Invalid Input. Continue? y/n:\t")
            if que=='y':
                continue
            else:
                print("Thank You!".center(60,'-'))
            break
#-------------------------------------------------------------------------
def Time():
    l=[[1,'10:00 AM'],[2,'01:55 PM'],[3,'05:55 PM'],[4,'09:55 PM']]
    print('-'.center(50,'-'))
    print("TIMINGS:")
    for i in l:
        print(i[0],i[1])
    b=True
    while b:
        n=input("Enter Time Choice:\t")
        print()
        if n.isdigit() and n <='4'and len(n)==1 :
            if n=='1':
                print("10:00 AM")
            elif n=='2':
                print('01:55 PM')
            elif n=='3':
                print('05:55 PM')
            elif n=='4':
                print('09:55 PM')
            v=int(n)
            temp=l[v-1]
            x.append(temp)
            logic()
            break
        else:
            que=input("Invalid Input. Continue? y/n:\t")
            if que=='y':
                continue
            else:
                print("Thank You!".center(60,'-'))
            break
#------------------------------------------------------------------------
def seat_show():
    print('-'.center(50,'-'))
    print('\n')
    print("Seat Choice:")
    print("PREMIUM".rjust(45,'-'),':',550)
    for i in se_dic:
        print(i,se_dic.get(i))
        if i=='c':
            print("EXECUTIVE".rjust(45,'-'),':',350)
        if i=='f':
            print("NORMAL".rjust(45,'-'),':',250)
    print('\n')
    print('-'.center(50,'-'))
#-------------------------------------------------------------------------------------  
def updated_list():
    global seat_cnt
    l=se_dic[seat_row]
    i=0+frm_seat-1
    try:
        while (seat_cnt)>0:
            if l[i]==0:
                print('"',seat_row,'"','th rows seats are full.')
                calling()
            elif l[i]!=0:
                l[i]=0
                seat_cnt-=1
            i+=1
    except IndexError:
        pass
    finally:
        return
#-------------------------------------------------------------------------------------  
def reupdated_list():
    global seat_cnt
    l=se_dic[seat_row]
    i=0+frm_seat-1
    try:
        while (seat_cnt)>0:
            if l[i]==0:
                print('"',seat_row,'"','th rows seats are full.')
                calling()
            elif l[i]!=0:
                l[i]=0
                seat_cnt-=1
            i-=1
    except IndexError:
        pass
    finally:
        return
#-------------------------------------------------------------------------------------       
def calling():
    f=True
    while True:
        global seat_cnt,seat_row,frm_seat,ex 
        ex=0
        seat_row=(input("Select the seat row."))
        if seat_row.isalpha()!=True or len(seat_row)!=1 or seat_row>'h':
            joker=input("Invalid. Continue?y/n:\t ")
            if joker=='y':
                continue
            else:
                ex=1
                f=False
                break
        else:
            break
    while f:
        try:
            frm_seat=int(input("Enter the starting point of seat?"))
            if frm_seat>10:
                raise ValueError
        except ValueError:
            joker=input("Invalid. Continue?y/n:\t ")
            if joker=='y':
                continue
            else:
                ex=1
                f=False
                break
        print()
        seat_aval=se_dic[seat_row]
        x1.clear()
        x1.append(seat_row)
        
        
        limit=seat_aval[frm_seat-1:frm_seat+seat_cnt-1]
        limit1=seat_aval[(frm_seat-1):(-10+frm_seat-seat_cnt-1):-1]        
        if len(limit)==seat_cnt:
            x1.append(limit)                
            updated_list()
            break
        elif len(limit1)==seat_cnt:
            x1.append(limit1)
            reupdated_list()
            break
        elif len(limit)!=seat_cnt or len(limit1)!=seat_cnt:
            print('''Available seats in the selected row are limited.
                   \nSelect some other row. ''')
            ex=1
            break
#-----------------------------------------------------------------------------------
def ticket():
    global ticket_list
    ticket_list=[]
    for i in x:
        ticket_list.append(i[1])
    bill()
#-------------------------------------------------------------------------------------
def bill():
    print()
    print('-'.center(60,'-'))
    print("BOOKING SUMMARY".center(60,' '))
    print('-'.center(60,'-'))
    now=datetime.now()
    dt_now = now.strftime("%d/%m/%Y %H:%M:%S")
    print(dt_now.rjust(60))	
    print('Movie'.ljust(13),':',ticket_list[0])
    print('Language'.ljust(13),':',x[0][2])
    print('Time'.ljust(13),':',ticket_list[2])
    print('Theatre'.ljust(13),':',ticket_list[1])
    print('-'.center(50,'-'))
    print()
    if x1[0] in'abc':
        print('Seat'.ljust(13),':','PREMIUM')
    elif x1[0] in'def':
        print('Seat'.ljust(13),':','EXECUTIVE')
    elif x1[0] in'gh':
        print('Seat'.ljust(13),':','NORMAL')
    print('Seat Row'.ljust(13),':',x1[0])
    print('Seat Numbers'.ljust(13),':',x1[1])
    print('-'.center(50,'-'))
    print()
    price=0
    global seat_cnt
    if x1[0] in 'abc':
        price=550*s
        print('Price'.ljust(13),':',550)
        print('Total Price'.ljust(13),':',price)
    elif x1[0] in 'def':
        price=350*s
        print('Price'.ljust(13),':',350)
        print('Total Price'.ljust(13),':',price)
    elif x1[0] in 'gh':
        price=250*s
        print('Price'.ljust(13),':',250)
        print('Total Price'.ljust(13),':',price)
    print('-'.center(50,'-'))
    print()
    gst=price*4//100
    print('GST @4%'.ljust(13),':',gst)
    print('-'.center(50,'-'))
    print()
    print('AMOUNT PAYABLE'.ljust(15),':',price+gst)
    print()
#-------------------------------------------------------------------------------------
a=input("Enter Name:")
if len(a)==0:
    b=input('Invalid. Do you wish to continue? y/n:')
    if b=='y':
        pass
    else:
        print("Thank you")
else:
    print('~'.center(60,'~'))
    print('Welcome to BookMyShow'.center(60,' '))
    print('~'.center(60,'~' ))
    print('Location: Bengaluru'.rjust(60))
    now=datetime.today()
    nowstr=now.strftime('%B %d,%Y')
    print(f'Date:   {nowstr}'.rjust(60))
    print()
    print('WELCOME Mr.'+a.capitalize()+'.')
    print('-'.center(60,'-'))
    print()
#---------------------------------------------------------------------------------
def Main():
    z=[[1,'.English'],[2,'.Hindi'],[3,'.Kannada']]
    b=True
    while b:
        print("Choose the Preferred Movie Language:\t",end='\n\n')
        for i in z:
            print(i[0],i[1])
            
        menu_input=input("Enter the Language Choice?: ")
        print()
        if menu_input=='1':
            English()
        elif menu_input=='2':
            Hindi()
        elif menu_input=='3':
            Kannada()
            print()
        else:
            a=input("Invalid choice. Do you wish to continue? y/n:\t")
            print()
            if a!='y':                
                print("THANK YOU!!!".center(60,'-'))
                b=False
            else:
                Main()
        b=False
 #---------------------------------------------------------------------------------       
Main()
#----------------------------------------------------------------------------------
try:
    movie_name=ticket_list[0]
    # print(movie_name)
    # print(type(movie_name))
    Language=x[0][2]
    # print(Language)
    # print(type(Language))
    Timings=ticket_list[2]
    # print(Timings)
    # print(type(Timings))
    Theatre=ticket_list[1]
    # print(Theatre)
    # print(type(Theatre))
except NameError:
    pass

if x1[0] in'abc':
    Seat='PREMIUM'
elif x1[0] in'def':
    Seat='EXECUTIVE'
elif x1[0] in'gh':
    Seat='NORMAL'
# print(Seat)
# print(type(Seat))
Seat_Row=x1[0]
# print(Seat_Row)
# print(type(Seat_Row))
Seat_Numbers=str(x1[1])
# print(Seat_Numbers)
# print(type(Seat_Numbers))
if x1[0] in 'abc':
    Price=550
    Total_Price=Price*s
elif x1[0] in 'def':
    Price=350
    Total_Price=Price*s
elif x1[0] in 'gh':
    Price=250
    Total_Price=Price*s
# print(Price)
# print(type(Price))
# print(Total_Price)
# print(type(Total_Price))
gst=Total_Price*4//100
# print(gst)
# print(type(gst))
AMOUNT_PAYABLE=Total_Price+gst
# print(AMOUNT_PAYABLE)
# print(type(AMOUNT_PAYABLE))
try:
    # print("Connecting")
    connection = mysql.connector.connect(host='localhost',database='ticket_booking',username='root',password='toor')
    print("Connected")

    cursor = connection.cursor()

    sql_insert_query = """insert into billing(`User`,`Movie`,`Language`,`Timings`,`Theatre`,`Seat Class`,`Seat Row`,`Seat Numbers`,
    `Price`,`Total Price`,`GST`,`Amount Payable`) 
    values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    insert_tuple = (a,movie_name,Language,Timings,Theatre,Seat,Seat_Row,Seat_Numbers,Price,Total_Price,gst,AMOUNT_PAYABLE)
    cursor.execute(sql_insert_query,insert_tuple)
    connection.commit()

    print("Row inserted")
except Exception as e:
    print("Exception occured",e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("connection closed")