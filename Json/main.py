# Python JSON Documentation Example

# 1. Introduction to JSON
# JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write,
# and easy for machines to parse and generate. Python has a built-in package called `json` to work with JSON data.

# 2. Importing the JSON Module
import json

# 3. Converting Python Objects to JSON
# The `json.dumps()` method is used to convert a Python object (like a dictionary) to a JSON string.

python_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "courses": ["Math", "Science"],
}

# Convert Python dictionary to JSON string
json_string = json.dumps(python_dict)
print("JSON String:")
print(json_string)

# 4. Converting JSON to Python Objects
# The `json.loads()` method is used to convert a JSON string back into a Python object.

# Convert JSON string back to Python dictionary
converted_dict = json.loads(json_string)
print("\nConverted Python Dictionary:")
print(converted_dict)

# 5. Writing JSON Data to a File
# The `json.dump()` method is used to write a Python object to a file in JSON format.

with open('data.json', 'w') as json_file:
    json.dump(python_dict, json_file)
    print("\nData written to 'data.json'.")

# 6. Reading JSON Data from a File
# The `json.load()` method is used to read JSON data from a file and convert it into a Python object.

with open('data.json', 'r') as json_file:
    loaded_data = json.load(json_file)
    print("\nLoaded Data from 'data.json':")
    print(loaded_data)

# 7. Pretty Printing JSON
# The `json.dumps()` method can take an optional argument `indent` to make the JSON output more readable.

pretty_json_string = json.dumps(python_dict, indent=4)
print("\nPretty Printed JSON String:")
print(pretty_json_string)

# 8. Handling JSON with Custom Objects
# To work with custom Python objects, you need to define how to serialize and deserialize them.

class Person:
    """A class to represent a person."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Custom serialization function
def person_to_json(person):
    return {"name": person.name, "age": person.age}

# Custom deserialization function
def json_to_person(json_obj):
    return Person(name=json_obj['name'], age=json_obj['age'])

# Creating a Person object
person = Person("Bob", 25)

# Serialize the Person object
person_json = json.dumps(person, default=person_to_json)
print("\nSerialized Person Object to JSON:")
print(person_json)

# Deserialize the JSON back to a Person object
deserialized_person = json.loads(person_json, object_hook=json_to_person)
print("\nDeserialized Person Object:")
print(f"Name: {deserialized_person.name}, Age: {deserialized_person.age}")

# 9. Conclusion
print("Working with JSON in Python is straightforward with the json module.")
