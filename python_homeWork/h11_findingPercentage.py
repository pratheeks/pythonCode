n=3
d1={
    'Krishna':{67,68,69},
    'Arjun':{70,98,63},
    'Malika':{52,56,60}
    }
print((d1.get('Krishna')))
print((d1['Krishna']))
print(type(d1))

a=sum(d1['Krishna'])/n
b=sum(d1['Arjun'])/n
c=sum(d1['Malika'])/n
#x=sum(a)/n

print(a)
print(b)
print(c)

print(type(a))

x={a,b,c}
print(min(x))
