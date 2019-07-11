s1="python IS easy."
s2="python is EaSy"
print(s1)
print(s1.capitalize())
print()

#casefold
print(s1.casefold())
print(s1.casefold()==s2.casefold())
print(s1==s2)
print()

#count
s1=" python "
print(s1.count(''))
print(len(s1))

#endswith
print(s1.endswith('n '))