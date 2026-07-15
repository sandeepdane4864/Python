# For Loops 

nums = [1,2,3,4,54,5,55,47]

for num in nums :
    if (num == 4):
        print("countinue Statement")
        continue
    print(num)
    
    
# for loop with else 

#case 1 
print("<-------Case 1 ---------->")
for num in nums :
    if (num == 4):
        print("break Statement")
        break
    print(num)
else:
    print("Complete Loop executed")
    
#case : 2
print("<-------Case 2 ---------->")
for num in nums :
    if (num == 4):
        print("break Statement")
        continue
    print(num)
else:
    print("Complete Loop executed")
    
    
# print * pattern

n = int(input("Enter n : "))

for i in range(1, n + 1,1):
    for j in range(1, i + 1,1):
        print('*', end=" ")
    print()


for i in range(1,n+1):
    for j in range(1,i+1):
        print(j ,end=" ")
    print()


for i in range(1,n+1):
    for j in range(1,i+1):
        print(j ,end=" ")
    for k in range(i-1,0,-1):
        print(k, end=" ")
    print()
    
# prime number 
l =  int(input("Enter l : "))
u = int(input("Enter u : "))

for i in range(l,u+1):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)

    