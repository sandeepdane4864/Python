# reverse an array 

nums = [1,2,55,4,457,4,1,5,48,8,4]
nums.reverse()

print(nums)
new_nums=[1,2,55,4,457,4,1,5,48,8,4]
rev_arary = new_nums[::-1]

print(rev_arary)

numss = [1, 2, 3, 4, 5]

left = 0
right = len(numss)-1

while(left<right):
    numss[left],numss[right]= numss[right],numss[left]
    left +=1
    right -=1
    
print(numss)

