# WAP to find sum of first 5 numbers 

n = int(input("Enter the Number : "))
sum = 0 
for i in range(1,n+1):
    sum = sum + i

print("SUM OF Total numbers 1 to 5 is",sum)


# Factorial 

fact = 1 

for i in range(1,n+1,1):
    
    fact = fact * i
    
print("factorial of ",n,"is",fact)


