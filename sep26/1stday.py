a = "Hello, World!"
print(len(a)) # count the str line

for x in "banana":
  print(x) # presenting each character in the string

txt = "The best things in life are free!"
print("cook" in txt) # checking if a word is present in the string
# if the word is present, it will return True, otherwise False

txt = "Лучшее в жизни — бесплатно!"
print("expensive" in txt)
# same as above, but with a different string and word

txt = "Лучшие вещи в жизни бесплатны!"
if "expensive" not in txt: 
  print("Нет, слово 'expensive' отсутствует.")
# checking if a word is not present in the string, and printing a message if it is not found

b = "Hello, World!"
print(b[1:9])# slicing the string from index 1 to 9 (not including 9)

b = " ello, World!"
print(b[:5]) # slicing the string from the beginning to index 5 (not including 5)

b = "Hello, World!"
print(b [2:]) # b = "Hello, World!"

b = "Hello, World!"
print(b[-12:-2])
# slicing the string from index -12 to -2 (not including -2)

a = "HEllo, World!"
print(a.upper())
# converting the string to uppercase

a = "HEllo, World!"
print(a.lower())
# converting the string to lowercase

a = "    Hello, World!       "
print(a.strip())
# удаляет пробелы в начале и в конце строки

a = "Hello"
b = "World"
c = a + b
print(c)
# concatenating two strings

a = "Hello"
b = "World"
c = a +"     " +b
print(c) # concatenating two strings with spaces in between

price = 59
txt = f"The price is {price} dollars"
print(txt)
# using f-strings to format a string with a variable
# краткто говаря f это format значит, что мы можем вставлять переменные в строку, используя фигурные скобки {}
# также можем внутри форматированной строки использовать выражения, например {price + 10} или {price * 2} или {price / 2} и т.д.

print('hello\nworld') # using escape character \n to create a new line # перекидывает на новую строку 
print('helloworld.capitalize(2)') # using escape character \ to include a single quote in the string # позволяет использовать одинарную кавычку внутри строки
a = "Hello"
b = "World"
c = a +"     " +b
print(c) # concatenating two strings with spaces in betweena = "Hello"
b = "World"
c = a +"     " +b
print(c) # concatenating two strings with spaces in between
a = "Hello"
b = "World"
c = a +"     " +b
print(c) # concatenating two strings with spaces in between

print('sddfshjdhfjsdfs')
print('hiii there')