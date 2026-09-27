#В Python можно сделать свойства приватными, используя префикс из двух символов подчеркивания __:
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.__age = age # Частное свойство

# p1 = Person("Emil", 25)
# print(p1.name)
# print(p1.__age)
#Примечание: к частным свойствам нельзя получить прямой доступ извне класса.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

p1 = Person("Tobias", 25)
print(p1.get_age())
#В Python также принято использовать префикс для обозначения защищенных свойств с помощью одного подчеркивания _ префикс:
