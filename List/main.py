# Python Lists Documentation Example

# 1. Creating Lists
# An empty list
empty_list = []
print("Empty List:", empty_list)  # Output: Empty List: []

# A list with initial values
fruits = ["apple", "banana", "cherry"]
print("Initial Fruits:", fruits)  # Output: Initial Fruits: ['apple', 'banana', 'cherry']

# Using the list() constructor
numbers = list((1, 2, 3))
print("Numbers List:", numbers)  # Output: Numbers List: [1, 2, 3]

# 2. Accessing List Items
# Accessing by index
first_fruit = fruits[0]
print("First Fruit:", first_fruit)  # Output: First Fruit: apple

# Negative indexing
last_fruit = fruits[-1]
print("Last Fruit:", last_fruit)  # Output: Last Fruit: cherry

# 3. Slicing Lists
# Basic slicing
sliced_fruits = fruits[1:3]
print("Sliced Fruits (1:3):", sliced_fruits)  # Output: Sliced Fruits (1:3): ['banana', 'cherry']

# Slicing with steps
even_indexed_fruits = fruits[::2]
print("Even Indexed Fruits:", even_indexed_fruits)  # Output: Even Indexed Fruits: ['apple', 'cherry']

# 4. Modifying Lists
# Changing item values
fruits[1] = "blueberry"
print("Fruits after modification:", fruits)  # Output: Fruits after modification: ['apple', 'blueberry', 'cherry']

# Appending items
fruits.append("orange")
print("Fruits after appending:", fruits)  # Output: Fruits after appending: ['apple', 'blueberry', 'cherry', 'orange']

# Inserting items
fruits.insert(1, "kiwi")
print("Fruits after inserting:", fruits)  # Output: Fruits after inserting: ['apple', 'kiwi', 'blueberry', 'cherry', 'orange']

# Removing items
# Using remove()
fruits.remove("cherry")
print("Fruits after removing 'cherry':", fruits)  # Output: Fruits after removing 'cherry': ['apple', 'kiwi', 'blueberry', 'orange']

# Using pop()
popped_fruit = fruits.pop()
print("Popped Fruit:", popped_fruit)  # Output: Popped Fruit: orange
print("Fruits after popping:", fruits)  # Output: Fruits after popping: ['apple', 'kiwi', 'blueberry']

# 5. List Methods
# Sorting lists
fruits.sort()
print("Sorted Fruits:", fruits)  # Output: Sorted Fruits: ['apple', 'blueberry', 'kiwi']

# Reversing lists
fruits.reverse()
print("Reversed Fruits:", fruits)  # Output: Reversed Fruits: ['kiwi', 'blueberry', 'apple']

# Finding the length
length = len(fruits)
print("Length of Fruits List:", length)  # Output: Length of Fruits List: 3

# Counting occurrences
count = fruits.count("apple")
print("Count of 'apple':", count)  # Output: Count of 'apple': 1

# 6. List Comprehensions
# Creating a list using a comprehension
squares = [x**2 for x in range(10)]
print("Squares from 0 to 9:", squares)  # Output: Squares from 0 to 9: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 7. Nested Lists
# Creating a nested list (2D array)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matrix:", matrix)  # Output: Matrix: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing nested list items
element = matrix[1][2]
print("Element at row 1, column 2:", element)  # Output: Element at row 1, column 2: 6

# 8. List Operations
# Concatenation
combined_list = fruits + ["grape", "melon"]
print("Combined List:", combined_list)  # Output: Combined List: ['kiwi', 'blueberry', 'apple', 'grape', 'melon']

# Repetition
repeated_list = ["a"] * 3
print("Repeated List:", repeated_list)  # Output: Repeated List: ['a', 'a', 'a']

# 9. Common Use Cases
# Storing user input
user_input = []
for i in range(3):
    item = input("Enter a fruit: ")
    user_input.append(item)
print("User Input Fruits:", user_input)

# Iterating through lists
print("Iterating through Fruits:")
for fruit in fruits:
    print(fruit)

# 10. Conclusion
print("List operations in Python are versatile and essential for data handling.")
