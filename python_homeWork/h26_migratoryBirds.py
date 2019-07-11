
arr=[1,4,4,4,5,3]
#arr=[1,2,3,4,5,4,3,2,1,3,4]
arr=sorted(arr)
#print(arr)
l=[]
for i in sorted(set(arr)):
#    print(i)
    l.append(arr.count(i))
#print(l)
maxNum=(max(l))
#print(max(l))
for i in sorted(set(arr)):
    if maxNum==arr.count(i):
        print(i)
        break

# =============================================================================
# 
# from collections import Counter
# #n = input()
# arr = Counter(map(int, input().split()))
# print(arr.most_common(5))
# print(sorted(arr.most_common(5)))
# print(arr)
# print(arr.most_common(1)[0][0])
# 
# =============================================================================
