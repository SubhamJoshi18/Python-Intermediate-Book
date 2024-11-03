# Python Sets Documentation Example

# 1. Introduction to Sets
# A set is a built-in data type in Python that is an unordered collection of unique elements.

# 2. Creating Sets
# An empty set
empty_set = set()
print("Empty Set:", empty_set)  # Output: Empty Set: set()

# A set with initial values
fruits_set = {"apple", "banana", "cherry"}
print("Initial Set:", fruits_set)  # Output: Initial Set: {'banana', 'cherry', 'apple'}

# Using the set() constructor
numbers_set = set([1, 2, 3, 4, 4, 5])
print("Numbers Set:", numbers_set)  # Output: Numbers Set: {1, 2, 3, 4, 5} (duplicates removed)

# 3. Accessing Set Items
# Sets are unordered, so you cannot access items by index.
# However, you can iterate through the set.
print("Fruits in Set:")
for fruit in fruits_set:
    print(fruit)

# 4. Adding Items to a Set
# Using add() method
fruits_set.add("orange")
print("Set after adding orange:", fruits_set)  # Output: Set after adding orange: {...}

# Using update() method to add multiple items
fruits_set.update(["mango", "grape"])
print("Set after updating with mango and grape:", fruits_set)  # Output: Set after updating with mango and grape: {...}

# 5. Removing Items from a Set
# Using remove() method (will raise KeyError if the item is not found)
fruits_set.remove("banana")
print("Set after removing banana:", fruits_set)  # Output: Set after removing banana: {...}

# Using discard() method (won't raise an error if the item is not found)
fruits_set.discard("pineapple")  # No effect as 'pineapple' is not in the set
print("Set after attempting to discard pineapple:", fruits_set)  # Output: Set after attempting to discard pineapple: {...}

# Using pop() method (removes and returns an arbitrary element)
removed_fruit = fruits_set.pop()
print("Removed Fruit:", removed_fruit)  # Output: Removed Fruit: <some fruit>
print("Set after popping an element:", fruits_set)  # Output: Set after popping an element: {...}

# 6. Set Methods
# Checking the number of elements
set_length = len(fruits_set)
print("Length of Set:", set_length)  # Output: Length of Set: <number>

# Checking membership
is_apple_in_set = "apple" in fruits_set
print("Is apple in the set?", is_apple_in_set)  # Output: Is apple in the set? True/False

# 7. Set Operations
# Union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)  # Output: Union of set1 and set2: {1, 2, 3, 4, 5}

# Intersection of two sets
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)  # Output: Intersection of set1 and set2: {3}

# Difference of two sets
difference_set = set1.difference(set2)
print("Difference of set1 and set2:", difference_set)  # Output: Difference of set1 and set2: {1, 2}

# Symmetric Difference of two sets
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference of set1 and set2:", symmetric_difference_set)  # Output: Symmetric Difference of set1 and set2: {1, 2, 4, 5}

# 8. Set Comprehensions
# Creating a set using comprehension
squares_set = {x**2 for x in range(10)}
print("Squares Set:", squares_set)  # Output: Squares Set: {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# 9. Common Use Cases
# Removing duplicates from a list
numbers_list = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers_list)
print("Unique Numbers from List:", unique_numbers)  # Output: Unique Numbers from List: {1, 2, 3, 4, 5}

# 10. Conclusion
print("Sets are a powerful data structure in Python, providing unique elements and supporting various operations.")
