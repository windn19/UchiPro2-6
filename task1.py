class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return f'Человек: {self.name}'

    def get_age(self):
        return f'Возраст: {self.age}'


class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def get_name(self):
        return f'Ученик: {self.name} ({self.course} класс)'


name = input()
age = input()
course = input()

student = Student(name, age, course)
print(student.get_name())
print(student.get_age())

men = Person(name, age)
print(men.get_name())
print(men.get_age())
