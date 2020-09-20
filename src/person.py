class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def happy_birthday(self):
        self.age = self.age + 1

    def change_name(self, new_name):
        self.name = new_name

