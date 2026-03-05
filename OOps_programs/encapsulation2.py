class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


    def deposit(self,amount):
        self.balance += amount
        print("Total balance is ", self.balance)

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Balance amount is :",self.balance )
        else:
            print("Insufficient balance")



    def balance_amt(self):
        print("Banalnce amount is ", self.balance)

b1 = Bank("Charvi",200)

print(b1.deposit(100))
print(b1.balance)
print(b1.withdraw(20))

