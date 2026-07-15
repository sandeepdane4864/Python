# Dictionary 

my_dict ={
    "name": "John",
    "age": 30,
    "city": "New York",
    "is_student": True,
    "married": False,
    "marks": [85, 90, 78] 
}

# accessing values
print("Name:", my_dict["name"])
print("Age:", my_dict["age"])

# updating values
my_dict["age"] = 31
print("Updated Age:", my_dict["age"])

# adding new key-value pair
my_dict["country"] = "USA"
print("Country:", my_dict["country"])

# removing key-value pair
del my_dict["is_student"]
print("Dictionary after removing 'is_student':", my_dict)

# checking if a key exists
if "city" in my_dict:
    print("City exists in the dictionary.")
    print("City:", my_dict["city"])

# methods in dictionary
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Items:", my_dict.items())
print("Length of dictionary:", len(my_dict))
print("Copy of dictionary:", my_dict.copy())
print("Get age using get method:", my_dict.get("age"))
print("Pop age from dictionary:", my_dict.pop("age"))
print("Dictionary after popping 'age':", my_dict)
print("Popitem from dictionary:", my_dict.popitem())
print("Dictionary after popitem:", my_dict)
print(my_dict.update({"gender": "male"}))
print("Dictionary after updating with gender:", my_dict)
print("Clearing the dictionary...")
my_dict.clear()
print("Dictionary after clearing:", my_dict)

# add new key value in dict
