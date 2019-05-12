s='AABCAAADA'
n=len(s)
k=3

#print('n:',n)
#print('k:',k)

k1=n//k

#print('k1:',k1)
#
#st=[]
#string=''
#
#for i in s:
#    string+=(i)
#    if len(string)<k1:
#        continue
#    else:
#        st.append(string)
#        string=''
#        
#print(st)

stg=[]
len_stg=0
for i in s:
    len_stg+=1
    if i not in stg:
        stg+=i
    if len_stg==k:
        print(''.join(stg))
        stg=[]
        len_stg=0
'''
stg=''
for i in st:
#    print(i)
    for j in i:
#        print(j)
        cnt=i.count(j)
#        print(j,cnt)
        ind=i.index(j)
#        print(j,cnt,ind)
        if i.count(j)>1:
            
#            print(ind)
            ind1=i.index(j,ind+1)
            print(j,ind1)
            stg+=i[ind1]     #stg+=i[:ind1]+i[ind1+1:]

        elif i.count(j)==1:
            stg+=j
    print(stg)
    stg=''
    
'''