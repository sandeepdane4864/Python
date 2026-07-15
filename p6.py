# strings 


a = "apnacollege"
b= " is a good platform for learning"

c = a + b # concatenation of strings
print(c)

print( "length = ", len(c) ) # length of string

print(c[4]) # accessing a character from string

# slicing of string

d = "Hello"


print( d[0:3] ) # prints Hel
print( d[1:4] ) # prints ell
print( d[2:] ) # prints llo
print( d[:3] ) # prints Hel


# negative indexing
print( d[-1] ) # prints o
print(d[:-1])

# print reverse of string
print( d[::2] )  # prints every second character
print( d[::-1] ) # prints reverse of string
print( d[::-2] ) # prints every second character in reverse order


# string Functions 

h = "hello world"
print(h.upper()) # converts to uppercase
print(h.lower()) # converts to lowercase
print(h.capitalize()) # capitalizes the first letter
print(h.title()) # capitalizes the first letter of each word
print(h.strip()) # removes whitespace from the beginning and end
print(h.replace("world", "Python")) # replaces a substring with another substring
print(h.split()) # splits the string into a list of words
print(h.find("world")) # returns the index of the first occurrence of a substring
print(h.count("o")) # returns the number of occurrences of a substring
print(h.startswith("hello")) # returns True if the string starts with a substring
print(h.endswith("world")) # returns True if the string ends with a substring
print(h.isalpha()) # returns True if the string contains only alphabetic characters
print(h.isdigit()) # returns True if the string contains only digits
print(h.isalnum()) # returns True if the string contains only alphanumeric characters
print(h.islower()) # returns True if the string is in lowercase
print(h.isupper()) # returns True if the string is in uppercase
print(h.isspace()) # returns True if the string contains only whitespace
print(h.isprintable()) # returns True if the string is printable

# WAP to imput users name and print its length

str = input("Enter your name: ")
print("Length of your name is:", len(str))

st2 = "$apjnksnd$ kjnklj"
print(str.count("$")) # returns the number of occurrences of a substring
