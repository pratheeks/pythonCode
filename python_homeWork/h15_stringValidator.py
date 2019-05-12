s="#$%@^&*kjnk svskjnbui h 4oi3hheuh /dfh uidshvhdsuihv suihc 0hrem89m4c02mw4xo;,wh fwhncoishmxlxfkjsahnxu83v 08 n8OHOIHIOMOICWHOFCMHEOFMCOEJMC0J09C 03J J3L;JMFC3JM3JC3'JIOO9MMJ099U N090N9 OOHOLNHNLLKNLKNKNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333000000000000000000000000000000000000000000000000000000000000000000000000000"

x=len(s)
for i in s:
    if i.isalnum():
        print(1,True)
        break
    elif x>0:
        x-=1
        if x==0:
            print(1,False)
        continue
    
x=len(s)
for i in s:
    if i.isalpha():
        print(2,True)
        break
    elif x>0:
        x-=1
        if x==0:
            print(2,False)
        continue
    
x=len(s)
for i in s:
    if i.isdigit():
        print(3,True)
        break
    elif x>0:
        x-=1
        if x==0:
            print(3,False)
        continue

x=len(s)       
for i in s:     
    if i.islower():
        print(4,True)
        break
    elif x>0:
        x-=1
        if x==0:
            print(4,False)
        continue
    
x=len(s)
for i in s:
    if i.isupper():
        print(5,True)
        break
    elif x>0:
        x-=1
        if x==0:
            print(5,False)
        continue
    
print()
# method2:
        
print(1,any(c.isalnum() for c in s))
print(1,s.isalnum())
        
