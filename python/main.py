# #Variables

# name = "ASK"
# age = 25
# salary = 35000

# print(name)
# print(age)
# print(salary)

# #Datatypes
# # String
# name = "ASK"

# # Integer
# age = 25

# # Float
# salary = 35000.50

# # Boolean
# is_learning = True

# # List
# skills = ["Python", "SQL", "Java"]

# # Tuple
# coordinates = (10.5, 76.2)

# # Set
# languages = {"Python", "Java", "C"}

# # Dictionary
# person = {
#     "name": "ASK",
#     "age": 25
# }

# # None
# result = None

# print(type(name))
# print(type(age))
# print(type(salary))
# print(type(is_learning))
# print(type(skills))
# print(type(coordinates))
# print(type(languages))
# print(type(person))
# print(type(result))

# #Input & Output
# name = input("Enter your name: ")
# age = input("Enter your age: ")

# print(name)
# print(age)

# print("My name is", name)
# print("My age is", age)

# print(f"My name is {name} and I am {age} years old.")

# #Operators
# a = 10
# b = 3

# # Arithmetic
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)

# # Comparison
# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)

# # Assignment
# x = 10
# x += 5
# print(x)

# x -= 3
# print(x)

# x *= 2
# print(x)

# x /= 4
# print(x)

# # Logical
# age = 25

# print(age >= 18 and age <= 60)
# print(age < 18 or age > 60)
# print(not age >= 18)

#String
name = "ASK"

print(name)
print(name[0])
print(name[-1])
print(len(name))

print(name.lower())
print(name.upper())

text = "  Python Developer  "
print(text.strip())

message = "I am learning Python"
print(message.replace("Python", "AI"))

print(message.split())

first_name = "Amith"
last_name = "Kumar"

full_name = first_name + " " + last_name
print(full_name)

print(f"My name is {full_name}")

#Typecasting

# String to Integer
age = "25"
age = int(age)
print(age)
print(type(age))

# String to Float
price = "99.50"
price = float(price)
print(price)
print(type(price))

# Integer to String
number = 100
number = str(number)
print(number)
print(type(number))

# Float to Integer
value = 10.99
value = int(value)
print(value)

# Integer to Float
score = 95
score = float(score)
print(score)


# Practice

# Create a simple bill calculator

# Input
# Product name
product = input("Enter product name: ")
# Price
price = float(input("Enter price: "))
# Quantity
quantity = int(input("Enter quantity: "))

# Calculate:
# Total price = price * quantity
total_price = price * quantity
# 10% discount
discount = total_price * 0.10
# Final price after discount
final_price = total_price - discount

# Print all results
print(f"Product: {product}")
print(f"Price: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total Price: ${total_price:.2f}")
print(f"Discount: ${discount:.2f}")
print(f"Final Price: ${final_price:.2f}")