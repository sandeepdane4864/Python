# reverse a number and count the no of digits in it

num = int(input("Enter number n : "))
original = num 
reverse = 0
count = 0 
while (num>0) : 
    last_digit = num % 10
    reverse = (reverse * 10)+last_digit
    num= num // 10 
    count = count +1
print("reverse  of number : ",reverse)
print("number of digits are",count)
    
# check if the number is palindrome 

is_palindrome = True

if(original != reverse):
    is_palindrome = False
    print("Not a Palindrome")
else:
    print("Palindrome")

# string is palindrome 

name = input("Enter the Word : ")

reverse_str = name[::-1]

if(name != reverse_str):
    is_palindrome = False
    print("Not a Palindrome")
else:
    print("Palindrome")

# Amstromg number
sum = 0 
new = original
while(original > 0):
    digit = original%10
    sum = sum + ( digit ** count)
    original = original//10
    
if (new == sum):
    print( "its armstrong number")
else: 
    print( "not a armstrong number")

