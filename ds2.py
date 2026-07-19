# factors of a number 

n = int(input("Enter a number : "))
factors = []
for i in range (1,n+1,1):
    if(n%i == 0 ):
        factors.append(i)
else:
    print("factors of {} = ".format(n) ,factors)
    

