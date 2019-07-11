s={'x':1,'y':3,'z':5}
s1={'q':10,'gh':15}
print(s)
s.update(a='ss',w=0)
print(s)
s.update(s1)
print(s)

s=dict(x=10,t=20)
s=dict([(1,'apple'),(2,'orange')])
print(s)

x={}.fromkeys('asdfgh',1)
print(x)

x.pop('a')
print(x)

del x['s']
print(x)

del(x['d'])
print(x)

# print(del(x))


print({s[i] for i in s })