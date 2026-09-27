class dog:
    def __init__(self, name,age):
        self.name = name
        self.age = age  
    def bark(self):
        print(f"{self.name} gav gav")
         
d1 = dog("buddy",33)
d1.bark()
#Create a class called Dog
#Add an __init__ method with parameters name and age, and store them as properties using self
#Add a method called bark that prints the dog's name followed by " says Woof!"
#Create an object d1 of the Dog class with name "Buddy" and age 3
#Call the bark method on d1
#https://www.w3schools.com/python/python_challenges_classes_basics.asp