#Aggregation Example 

class Customer:
    
    def __init__(self ,name, gender, address):
        self.name = name 
        self.gender = gender
        self.address = address
    
    def get_address(self):
        print(self.address.city, self.address.pin,self.address.state)
        
        
class address :
    def __init__(self, city, pin,state):
        self.city = city
        self.pin = pin
        self.state = state

add1 = address('Shelgaon', 431723, "MH")
Cust1 = Customer('Sandeep', "Male", add1)
Cust1.get_address()
print(add1.state)
        
        