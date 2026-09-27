#Классы и объекты в Python
#Python — объектно-ориентированный язык программирования.
#Почти все в Python — это объекты со своими свойствами и методами.

#Класс — это своего рода конструктор объектов или «чертёж» для создания объектов.
class MyClass:
    x = 5
#Теперь мы можем использовать класс MyClass для создания объектов:
#Создайте объект с именем p1 и выведите значение x:
a = MyClass()
print(a.x)
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)

class MyClass:
    x=4
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()
#del p3
print(p1.x)
print(p2.x)
print(p3.x)
class ap:
    pass