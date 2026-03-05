class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance


    def deposit(self,amount):
        self.__balance += amount
        print("Total amount is ", self.__balance)

    def withdraw(self,amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print("remaining amount is :",self.__balance )
        else:
            print("Insufficient balance")



    def balance_amt(self):
        print("Balance amount is ", self.__balance)

b1 = Bank("Charvi",200)

b1.deposit(100)
b1.withdraw(20)
b1.balance_amt()


