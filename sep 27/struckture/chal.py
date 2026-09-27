class Student:
    def __init__(self,name, grade):
        self.name = name
        self.grade = grade
s1 = Student("Anna", "A")
s2 = Student("Anna", "B")
print(s1.grade)
print(s2.grade)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy birthday! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()