my_dict = {
    
    "table": [
        "a peice of furniture",
        "list of facts and figures"
    ],
    "cat": "a small animal "
}

print(my_dict)

sub = {'python', "c","java", 'c',"python", "c++","ruby"}

print(len(sub))



# take 3 subject names and marks from user and add in dict one by one in key value pair 

student = {}
for i in range(3):
    key = input("enter Subject name :")
    value = float(input("enter Subject Marks : "))
    student.update({key: value})
    
print(student)
