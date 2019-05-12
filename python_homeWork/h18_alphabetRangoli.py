n = 3
for i in range(n):
    s = "-".join(chr(ord('a')+n-j-1) for j in range(i+1))
    print((s+s[::-1][1:]).center(n*4-3, '-'))

for i in range(n-1):
    s = "-".join(chr(ord('a')+n-j-1) for j in range(n-i-1))
    print((s+s[::-1][1:]).center(n*4-3, '-'))



'''
n=3
wi=((2*n)+(2*(n-1))-1)
st=''
x='' 
y='' 
z=''
for i in range(n+(n-1)):
    if i%2==0:
            x+=chr(97+i//2)
    else:
        x+='-'
y=x[::-1]
z=y+x[1:]
fin=z[0:1]
fir=4
sec=wi-1
for i in range(n):
    print(fin.center(wi,'-'))
    fin=z[0:fir]+z[sec:wi]
    fir+=2
    sec-=2
fir-=4
sec+=4
for j in range(n-1):
    fir-=2
    sec+=2
    fin=z[0:fir]+z[sec:wi]
    print(fin.center(wi,'-'))
'''
    

    
'''    
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

'''