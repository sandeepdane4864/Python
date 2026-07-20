class Account:

    def __init__(self):
        self.name = input("Enter Account Holder Name: ")
        self.accno = int(input("Enter Account Number: "))
        self.balance = int(input("Enter Initial Amount: "))

        self.start()


    def credit(self):
        amount = int(input("Enter Amount to Credit: "))

        self.balance = self.balance + amount

        print("Amount Credited Successfully")
        print("Current Balance:", self.balance)


    def debit(self):
        amount = int(input("Enter Amount to Debit: "))

        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount Debited Successfully")
        else:
            print("Insufficient Balance")

        print("Current Balance:", self.balance)


    def checkbalance(self):
        print("Account Holder:", self.name)
        print("Account Number:", self.accno)
        print("Current Balance:", self.balance)


    def start(self):

        while True:

            print("\nChoose Option:")
            print("1. Credit Amount")
            print("2. Debit Amount")
            print("3. Check Balance")
            print("4. Exit")

            opt = int(input("Enter Option Number: "))


            if opt == 1:
                self.credit()

            elif opt == 2:
                self.debit()

            elif opt == 3:
                self.checkbalance()

            elif opt == 4:
                print("Thank You")
                break

            else:
                print("Wrong Option")


a = Account()