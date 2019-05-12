a=''
try:
    with open('D:\python\python_abc\dummy.txt','r') as f:
#        print(f.read())
        a+=f.read()
    print(a[-1]=='\n')
    wc=para=vc=cc=sp=c=0
    t=a
    t=t.replace(',','')
    t=t.replace('.','')
    for i in t:
        if i==' ':
            wc+=1
        elif i=='\n':
            c+=1
            if c%2==0:
                wc+=1
                para+=1
                c=0
    print("wordCount",wc+1)
    print("paraCount",para+1)
    
    for i in a:
        if (i>'A' and i<'Z') or (i>'a' and i<'z'):
            if( i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or 
            i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
                vc+=1
            else:
                cc+=1
        elif(not(i>='0' and i<='9')):
            sp+=1
    print("vowelCount",vc)
    print("ConsonentCount",cc)
    print("spCount",sp)
except:
    print("File Not Found")

