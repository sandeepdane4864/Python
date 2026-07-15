# using for loop search for a number x in tuple and print 
# its index and found at message

nums = (1, 2, 4, 8, 7, 6, 48, 2, 5, 6, 4, 62, 56, 12, 5, 62, 15)

for index, num in enumerate(nums):
    if num == 4:
        print("found", num, "at index", index)
        
        
        
        
# 2nd way to get value and index without ennumerate 

idx = 0
for element in nums :
    if (element == 4):
        print("Element",element," found at index",idx)
    idx = idx + 1


    
    
    
