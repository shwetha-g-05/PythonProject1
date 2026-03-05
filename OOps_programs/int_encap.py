class Employee:
    def __init__(self, name , salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return  self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("invalid salary")

e1= Employee("Mily", 50000)
print(e1.get_salary())

e1.set_salary(60000)

print(e1.get_salary())