#Sum of even numbers and odd numbers

num=[2,22,27,29,35,42,8,75,88]
even=0
odd=0
for i in num:
    if i%2==0:
        even+=i
    else:
        odd+=i
print(even)
print(odd)        
        