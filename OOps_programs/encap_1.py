class Bank:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

b1 = Bank(5000)
print(b1.get_balance())