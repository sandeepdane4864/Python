# string is palindrome or not

s = input("Enter the String : ")

rev_string = s[::-1]

print(rev_string)

if(s!= rev_string):
    print("not palindrome")
else:
    print("palindrome")
    
newstring = []
left = 0
is_palindrome = True
right = len(s)-1
for i in range(left,right//2,1) :
    
    if (s[left] != s[right]):
        is_palindrome = False
        break
    

if is_palindrome:
    print("Sting is palindrome ")
else:
    print("Sting is not palindrome ")
    


    
    


