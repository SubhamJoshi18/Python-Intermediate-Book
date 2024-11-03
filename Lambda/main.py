# Python Lambda Functions and Functional Programming Documentation Example

# 1. Introduction to Lambda Functions
# A lambda function is a small anonymous function defined with the lambda keyword.
# Lambda functions can take any number of arguments but can only have one expression.

# 2. Defining and Using a Lambda Function
# Example of a simple lambda function that adds two numbers.

add = lambda x, y: x + y
result = add(5, 3)
print(f"Result of adding 5 and 3 using lambda: {result}")  # Output: 8

# 3. Using Lambda with map()
# The map() function applies a given function to all items in an iterable (like a list).
# It returns an iterator that produces the results.

numbers = [1, 2, 3, 4, 5]

# Using lambda to square each number in the list
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("\nSquared Numbers using map():")
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# 4. Using Lambda with filter()
# The filter() function filters elements from an iterable based on a function that returns True or False.
# It returns an iterator containing only the items for which the function returns True.

# Using lambda to filter even numbers from the list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("\nEven Numbers using filter():")
print(even_numbers)  # Output: [2, 4]

# 5. Using Lambda with reduce()
# The reduce() function from the functools module applies a rolling computation to sequential pairs of values in an iterable.
# It requires importing the reduce function.

from functools import reduce

# Using lambda to calculate the product of all numbers in the list
product = reduce(lambda x, y: x * y, numbers)
print("\nProduct of Numbers using reduce():")
print(product)  # Output: 120 (1*2*3*4*5)

# 6. Combining Lambda with map, filter, and reduce
# Example of combining all three functions to process a list of numbers.
# 1. Square the numbers
# 2. Filter out the even squares
# 3. Calculate the sum of the remaining odd squares

# Step 1: Square the numbers
squared = list(map(lambda x: x ** 2, numbers))
print("\nSquared Numbers:")
print(squared)  # Output: [1, 4, 9, 16, 25]

# Step 2: Filter out even squares
odd_squares = list(filter(lambda x: x % 2 != 0, squared))
print("\nOdd Squares after filtering:")
print(odd_squares)  # Output: [1, 9, 25]

# Step 3: Calculate the sum of the odd squares
sum_of_odd_squares = reduce(lambda x, y: x + y, odd_squares)
print("\nSum of Odd Squares:")
print(sum_of_odd_squares)  # Output: 35 (1 + 9 + 25)

# 7. Conclusion
print("Lambda functions combined with map, filter, and reduce provide powerful tools for functional programming in Python.")
