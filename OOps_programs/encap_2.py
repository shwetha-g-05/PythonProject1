class Student:
    def __init__(self, name ,marks, phone_no):
        self.name = name
        self.marks = marks
        self.__phone_no = phone_no


    def get_marks(self):
        return self.marks

    def get_phone_no(self):
        return self.__phone_no

    def get_name(self):
        return "Shwetha"

s1 = Student("Mily", 60, 235689)
print(s1.get_phone_no())
print(s1.get_name())
