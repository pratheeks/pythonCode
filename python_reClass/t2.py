a='t1hi2s i1s1 he2l2l2o wo3r1ld1'.lower()
print("\ninput:",a)
i=0
j=''
sum=0
for i in a:
    if i>='a' and i<='z':
        if i=='a' or i=='e' or i=='o' or i=='u' or i=='i':
            j+='*'+i
        else:
            j+=i
    elif i>='0' and i<='9':
        sum+=int(i)
    elif i==' ':
        j+=str(sum)+i
        sum=0
j+=str(sum)
print()
print("output:",j)
  