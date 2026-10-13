#Integer
age = int(input("Enter your age: "))

#Float 
salary = float(input("Enter your salary: "))

#String
name = input("Enter your name: ")

#Boolena
is_developer = input("Are you a Developer? (true/false): ").strip().lower() == "true"

#list of integers
numbers = list(map(int, input("Enter numbers seperated by space: ").split()))

#list of string 
languages = input("Enter programming language: ").split()

# Tuple of integers
coordinates = tuple(map(int, input("Enter coordinates: ").split()))

# Set of integers
unique_numbers = set(map(int, input("Enter numbers for a set: ").split()))

#Dictionary
person = {
    "name": input("Enter your name: "),
    "age": int(input("Enter your age: "))
}

#complex numbers
complex_number = complex(input("Enter a complex number (e.g. 2+3j): "))

#Display the value their types

values = [
    age, salary, is_developer,
    numbers, languages, coordinates, 
    unique_numbers, person, complex_number
]

for data in values:
    print(f"Data is {data} and it's Data type is {type(data)}")