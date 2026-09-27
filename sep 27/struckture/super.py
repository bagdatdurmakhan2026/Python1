#В Python также есть функция super(), которая позволяет дочернему классу наследовать все методы и свойства родительского класса:
# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year

#   def welcome(self):
#     print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# x = Student("Mike", "Olsen", 2024)
# x.welcome()

class Animal:
    def __init__(self, name):
        self.name=name
    def speak(self):
        return self.name
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        print("name is", self.name)
d1 = Dog("Rex") 
d1.speak()       

