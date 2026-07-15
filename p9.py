# list 

a = [1, 2, 3, 4, 5]
print(a) # prints the list

b = [1, "hello ", 3.14, True]
print(b) # prints the list

b[1] = "world" # changing the value of an element in the list
print(b) # prints the list

b.append("new element") # adding an element to the end of the list
print(b) 
b.remove("new element") # removing an element from the list
print(b) 
b.insert(1, "new element") # adding an element at a specific index
print(b) 
b.pop(1) # removing an element at a specific index
print(b)
b.sort() # sorting the list
print(b)
b.sort(reverse=True) # sorting the list in reverse order
print(b) 
b.reverse() # reversing the list
print(b)
b.clear() # removing all elements from the list
print(b)
