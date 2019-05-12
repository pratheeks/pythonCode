a=input('Enter the input:\n')

def wordCount(a):
    c=0
    i=0
    while i<len(a):
        if a[i]==' ' and a[i+1]!=' ':
            c+=1
            i+=1
        else:
            i+=1
    return(c+1)


st=0
k=0
while k<len(a):
    if a[k]!=' ':
        st=k
        break
    else:
        k+=1
ed=0
j=len(a)-1
while j>=0:
    if a[j]!=' ':
        ed=j
        break
    else:
        j-=1
s=a[st:ed+1]
#print(s)
print('WordCount:',wordCount(s))    


#method2
#for i in range(len(a)):
#    if a[i]==' ' and a[i+1]!=' ':
#        j+=1
#print(j)

#print()