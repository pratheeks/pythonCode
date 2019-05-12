hid=5
usr=0
count=0
while usr!=hid:
    usr=int(input("Enter the number?\t\n"))
    count+=1
    try:
        if usr>hid:
            raise ValueError('ValueTooLarge')
        elif usr<hid:
            raise ValueError('ValueTooSmall')
        elif usr==hid and count<=3:
            print("Congratulations!!!")
        else:
            print("Loser")
            print('attempts:',count)
    except ValueError as v:
        print(v)
        
        
    
    