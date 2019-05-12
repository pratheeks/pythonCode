'''
#method1:+6
def solve(s):
    x=''
    i=0
    try:
        while i<len(s):
            if s[i]!=' ':
                x+=s[i]
                i+=1
            elif s[i]==' ' and s[i+1]!=' ':
                x+=' '+s[i+1].upper()
                i+=2
            else:
                x+=s[i]
                i+=1
        print(x)
    except IndexError:
        print('Indexerror')
        
s = 'hello   world  lol'.capitalize()
print(s)

result = solve(s)
'''

'''
#method2:
print(' '.join(i.capitalize() for i in input().split(' ')))

'''
#method3:
string='hello   world  lol'
print(string)
l=string.split(' ')
print(l)
x=[]
#a = [i.capitalize() for i in l]    
for i in l:
    x.append(i.capitalize())
    print(x)
print(' '.join(x))
print('$'.join(x))
