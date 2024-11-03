# Python Tuples Documentation Example

# 1. Introduction to Tuples
# A tuple is a built-in data type in Python that is an ordered collection of elements.
# Tuples are immutable, meaning that once they are created, their elements cannot be changed.

# 2. Creating Tuples
# An empty tuple
empty_tuple = ()
print("Empty Tuple:", empty_tuple)  # Output: Empty Tuple: ()

# A tuple with initial values
fruits_tuple = ("apple", "banana", "cherry")
print("Initial Tuple:", fruits_tuple)  # Output: Initial Tuple: ('apple', 'banana', 'cherry')

# A tuple with mixed data types
mixed_tuple = (1, "two", 3.0, True)
print("Mixed Data Types Tuple:", mixed_tuple)  # Output: Mixed Data Types Tuple: (1, 'two', 3.0, True)

# A tuple with a single element (note the comma)
single_element_tuple = (42,)
print("Single Element Tuple:", single_element_tuple)  # Output: Single Element Tuple: (42,)

# 3. Accessing Tuple Items
# Accessing by index
first_fruit = fruits_tuple[0]
print("First Fruit:", first_fruit)  # Output: First Fruit: apple

# Accessing by negative index
last_fruit = fruits_tuple[-1]
print("Last Fruit:", last_fruit)  # Output: Last Fruit: cherry

# Slicing tuples
sliced_fruits = fruits_tuple[1:3]
print("Sliced Fruits:", sliced_fruits)  # Output: Sliced Fruits: ('banana', 'cherry')

# 4. Modifying Tuples
# Tuples are immutable, so you cannot change their elements directly.
# However, you can concatenate tuples to create a new one.
new_fruits_tuple = fruits_tuple + ("orange", "grape")
print("New Fruits Tuple after Concatenation:", new_fruits_tuple)  # Output: New Fruits Tuple after Concatenation: ('apple', 'banana', 'cherry', 'orange', 'grape')

# 5. Tuple Methods
# Count the occurrences of an element
count_banana = fruits_tuple.count("banana")
print("Count of 'banana' in Tuple:", count_banana)  # Output: Count of 'banana' in Tuple: 1

# Find the index of an element
index_cherry = fruits_tuple.index("cherry")
print("Index of 'cherry':", index_cherry)  # Output: Index of 'cherry': 2

# 6. Packing and Unpacking Tuples
# Packing a tuple
packed_tuple = 1, 2, 3
print("Packed Tuple:", packed_tuple)  # Output: Packed Tuple: (1, 2, 3)

# Unpacking a tuple
a, b, c = packed_tuple
print("Unpacked Values:", a, b, c)  # Output: Unpacked Values: 1 2 3

# 7. Nested Tuples
# Creating a tuple containing other tuples
nested_tuple = (("a", 1), ("b", 2), ("c", 3))
print("Nested Tuple:", nested_tuple)  # Output: Nested Tuple: (('a', 1), ('b', 2), ('c', 3))

# Accessing elements in a nested tuple
second_element_of_nested = nested_tuple[1][0]
print("Second Element of Nested Tuple:", second_element_of_nested)  # Output: Second Element of Nested Tuple: b

# 8. Common Use Cases
# Tuples can be used to return multiple values from a function
def coordinates():
    return (10.0, 20.0)

x, y = coordinates()
print("Coordinates:", x, y)  # Output: Coordinates: 10.0 20.0

# 9. Tuples vs. Lists
# Tuples are typically used for fixed collections of items, whereas lists are used for collections that may change.
# Here is a comparison:

# Creating a list
fruits_list = ["apple", "banana", "cherry"]
fruits_list[1] = "orange"  # Lists are mutable
print("Modified List:", fruits_list)  # Output: Modified List: ['apple', 'orange', 'cherry']

# Tuples are immutable, so the following line would raise an error:
# fruits_tuple[1] = "orange"  # This will raise a TypeError

# 10. Conclusion
print("Tuples are a lightweight, immutable data structure in Python, ideal for fixed collections of items.")
