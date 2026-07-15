# Looping statements 

# 1 .While Loop

""" Initialize
While (condition):
    work
    incre/decre """


# print numbers from 1 to 10

i = 1

while (i <= 10):
    print(i)
    i = i+1



# print number from 10 to 1 

i = 10
while (i >= 1 ):
    print(i)
    i -=1
    
    
# print multiplication fof table n 

n = int(input("Enter a number: "))

i = 1
while (i <=10):
    print(n*i)
    i+=1

    

# print the elements of the list using while loop

list1 = [1,21,54,554,55,45,45,54,8,555,583,5,16,4]
i = 0

while ( i < len(list1)):
    num = list1[i]
    print(num)
    i +=1

# search for the number X in the tuple 

tup1 = (1,54,55,46,4,685,5,86,5,6,56,6,658)
x = int(input("Enter the NUmber : "))
found = False
i = 0 
while (i < len(tup1)):
    if( x == tup1[i]):
        found = True
        break
    i+=1

if (found == True ):
    print("found")
else:
    print("Not Found")
     
    
    

 