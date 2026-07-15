# WAP for even or odd number

num = int(input("Enter a number: "))
if((num % 2) == 0):
    print("{0} is Even".format(num))  # format() method formats the specified value(s) and insert them inside the string's placeholder.
else:
    print("{0} is Odd".format(num))

# find the greatest of 3 mumbers 

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if ( a >= b) and (a >= c):
    print("{0} is the greatest number".format(a))
elif (b >= a) and (b >= c):
    print("{0} is the greatest number".format(b))
else:  
    print("{0} is the greatest number".format(c))


# check whether a number is multiple of 7 or not 

num2 = int(input("Enter a number: "))
if(num2 % 7 == 0):
    print("{0} is a multiple of 7".format(num2))
else:   
    print("{0} is not a multiple of 7".format(num2))
    
    