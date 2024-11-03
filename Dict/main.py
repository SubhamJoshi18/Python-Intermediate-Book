# Python Dictionaries Documentation Example

# 1. Introduction to Dictionaries
# A dictionary is a built-in data type in Python that stores key-value pairs.
# Keys are unique and immutable, while values can be of any data type.

# 2. Creating Dictionaries
# An empty dictionary
empty_dict = {}
print("Empty Dictionary:", empty_dict)  # Output: Empty Dictionary: {}

# A dictionary with initial key-value pairs
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print("Initial Dictionary:", person)  # Output: Initial Dictionary: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Using the dict() constructor
another_person = dict(name="Bob", age=25, city="Los Angeles")
print("Another Person Dictionary:", another_person)  # Output: Another Person Dictionary: {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'}

# 3. Accessing Dictionary Items
# Accessing by key
name = person["name"]
print("Name:", name)  # Output: Name: Alice

# Using get() method
age = person.get("age")
print("Age:", age)  # Output: Age: 30

# 4. Modifying Dictionaries
# Changing a value
person["age"] = 31
print("Updated Age:", person)  # Output: Updated Age: {'name': 'Alice', 'age': 31, 'city': 'New York'}

# Adding a new key-value pair
person["email"] = "alice@example.com"
print("Dictionary after adding email:", person)  # Output: Dictionary after adding email: {'name': 'Alice', 'age': 31, 'city': 'New York', 'email': 'alice@example.com'}

# Removing items
# Using del keyword
del person["city"]
print("Dictionary after removing city:", person)  # Output: Dictionary after removing city: {'name': 'Alice', 'age': 31, 'email': 'alice@example.com'}

# Using pop() method
email = person.pop("email")
print("Popped Email:", email)  # Output: Popped Email: alice@example.com
print("Dictionary after popping email:", person)  # Output: Dictionary after popping email: {'name': 'Alice', 'age': 31}

# 5. Dictionary Methods
# Getting all keys
keys = person.keys()
print("Keys in Dictionary:", keys)  # Output: Keys in Dictionary: dict_keys(['name', 'age'])

# Getting all values
values = person.values()
print("Values in Dictionary:", values)  # Output: Values in Dictionary: dict_values(['Alice', 31])

# Getting all items (key-value pairs)
items = person.items()
print("Items in Dictionary:", items)  # Output: Items in Dictionary: dict_items([('name', 'Alice'), ('age', 31)])

# Clearing the dictionary
person.clear()
print("Dictionary after clearing:", person)  # Output: Dictionary after clearing: {}

# 6. Merging Dictionaries
# Using the update() method
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict1.update(dict2)
print("Merged Dictionary using update():", dict1)  # Output: Merged Dictionary using update(): {'a': 1, 'b': 3, 'c': 4}

# 7. Nested Dictionaries
# Creating a nested dictionary
students = {
    "student1": {
        "name": "John",
        "age": 20,
        "grades": {"math": 90, "science": 85}
    },
    "student2": {
        "name": "Jane",
        "age": 22,
        "grades": {"math": 95, "science": 90}
    }
}
print("Students Dictionary:", students)  # Output: Students Dictionary: {...}

# Accessing nested dictionary items
john_math_grade = students["student1"]["grades"]["math"]
print("John's Math Grade:", john_math_grade)  # Output: John's Math Grade: 90

# 8. Dictionary Comprehensions
# Creating a dictionary using comprehension
squares_dict = {x: x**2 for x in range(5)}
print("Squares Dictionary:", squares_dict)  # Output: Squares Dictionary: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 9. Common Use Cases
# Storing user preferences
user_preferences = {
    "theme": "dark",
    "language": "English",
    "notifications": True
}
print("User Preferences:", user_preferences)

# Iterating through a dictionary
print("Iterating through dictionary:")
for key, value in user_preferences.items():
    print(f"{key}: {value}")

# 10. Conclusion
print("Dictionaries are powerful and versatile data structures in Python, perfect for storing key-value pairs.")
