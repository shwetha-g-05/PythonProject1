class Student:
    def __init__(self,name,marks):
        self.name = name
        self.__marks = marks

    def display_marks(self):
        print(self.__marks)

s1 = Student("Shwetha", 32)
print(s1.name)
# print(s1.__marks)
print(s1.display_marks())