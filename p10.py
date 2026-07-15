# WAP to take 3 names of favoutre dishes from user and print them in a list

dishes = []
for i in range(3):
    dish = input("Enter the name of your favourite dish: ")
    dishes.append(dish)
    
print("Your favourite dishes are:", dishes)


# WAP to check list is palindrome or not

list = []
for i in range(5):
    element = input("Enter an element for the list: ")
    list.append(element)

print("The list is:", list)

if list == list[::-1]:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")

# without using slicing
is_palindrome = True

for i in range(len(list) // 2):
    if list[i] != list[len(list) - 1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print("The list is a palindrome.")
else:   
    print("The list is not a palindrome.")
        
        
        
        
copy_list = list.copy().reverse()

if list == copy_list:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")

        

