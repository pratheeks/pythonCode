s='praratheek'
ss='rat'
n=len(ss)
for i in range(len(s)):
    if ss==s[i:i+n]:
        print("Pass")
        break
else:
    print("Fail")
