l=list(range(1,10))
print(l)
'''
l.extend([92,93,94,95,96,97])
print(l)

print()

l.insert(0,0)
print(l)

l.extend([36,37,38])
print(l)
'''
l[9:9]=list(range(10,20))
print(l)
'''
l2=[3,4,5,7]
l.insert(2,l.extend([3,4,5]))
print(l)

print()

del l[0]
print(l)
print()

del(l[0])
print(l)

print(del l[0])
print(l)
'''