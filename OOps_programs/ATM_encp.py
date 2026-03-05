class ATM:
    def __init__(self, pin):
        self.__pin = pin


    def check_pin(self, enterd_pin):
        if enterd_pin == self.__pin:
            print("Access granted")
        else:
            print("Invalid pin")


a1 = ATM(123)
a1.check_pin(123)

