#special char and spaces
s=" Hello  World..!"
vow=cons=spl=spc=word=0
s=s.lower()
for i in range(len(s)-1):
	if s[i]==' ' and s[i+1]!=' ':
		word+=1
	if s[i] in 'aeiou':
		vow+=1
	elif s[i]>='a' and s[i]<='z' :
		cons+=1
	elif not(s[i]>='a' and s[i]<='z') and s[i]!=' ':
		spl+=1
	else:
		spc+=1
print(vow,cons,spl,spc,word)