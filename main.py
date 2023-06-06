numbers = [1, 2, 3, 4, 5]
squared = [x ** 2 for x in numbers]

numbers = [1, 2, 3, 4, 5]
evens = [x for x in numbers if x % 2 ==0]

matrix = [1, 2, 3], [4, 5, 6], [7, 8, 9]
flattened = [x for row in matrix for x in row]

text = "Hello"
characters = [ch for ch in text]

print(squared)
print(evens)
print(flattened)
print(characters)
