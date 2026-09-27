class cat:
    def sound(self):
        return f"Meow"
class Fox:
    def sound(self):
        return f"Wa-pa-pa-pa-pa-pow!"
c1 = cat()
f1 = Fox()
for animal in [c1,f1]:
    print(animal.sound())
