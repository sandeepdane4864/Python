 # duplicate and frq of ele,emts in arary
 
nums = [1,2,55,4,457,4,1,5,48,8,4]

empty_dict = {}

n = len(nums)

for i in range(0,n):
    if ( nums[i] in empty_dict):
        empty_dict[nums[i]] = empty_dict[nums[i]] + 1
    else:
        empty_dict[nums[i]] = 1 
else:
    print(empty_dict)
    

empt =[]
n = len(nums)

hash_map = {}
for i in range (0,n):
    hash_map[nums[i]] = hash_map.get(nums[i],0) + 1
    
print(hash_map)
freq = {}
for num in nums :
    if (num in freq):
        freq[num] +=1
    else:
        freq[num] =1
    
for key,value in freq.items():
    if (value ==1):
        continue
    else:
        print('{}->{} times'.format(key,value))
    

    