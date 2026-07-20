class Account:

    def __init__(self, name, password):
        self.name = name
        self.__password = password   # Private attribute 

    def show_name(self):
        print("Name:", self.name)

    def show_password(self):
        print("Password:", self.__password) 


a = Account("Ved", "12345")

a.show_name()
a.show_password()