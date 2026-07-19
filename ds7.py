nums = [1,2,3,4,1,2,4,3,8]
target = 6

seen = set()
pairs = set()

for num in nums:
    complement = target - num
    if( complement in seen):
        pairs.add(tuple(sorted((num, complement))))
    seen.add(num)

print("Unique pairs:", pairs)
print("Count:", len(pairs))

numss = [1, 2, 3, 4, 5]
targett = 7
for i in range(len(numss)+1):
    for j in range(i+1,len(numss)):
        if ( numss[i]+numss[j]==targett):
            print(numss[i],numss[j])
        