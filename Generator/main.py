# Python Generators Documentation Example

# 1. Introduction to Generators
# A generator is a special type of iterator that allows you to iterate over a sequence of values.
# Generators are defined using a function and the 'yield' statement, which makes them memory efficient.

# 2. Creating Generators
# A simple generator function
def simple_generator():
    yield 1
    yield 2
    yield 3

# Create a generator object
gen = simple_generator()

# 3. Using Generators
# Iterating through a generator using a for loop
print("Simple Generator Output:")
for value in gen:
    print(value)  # Output: 1, 2, 3

# 4. Generators with Yield
# A generator that produces a sequence of squares
def square_generator(n):
    for i in range(n):
        yield i ** 2

# Using the square_generator
squares = square_generator(5)
print("Squares from Generator:")
for square in squares:
    print(square)  # Output: 0, 1, 4, 9, 16

# 5. Generator Expressions
# A concise way to create generators using a generator expression
squared_numbers = (x ** 2 for x in range(5))
print("Squared Numbers from Generator Expression:")
for num in squared_numbers:
    print(num)  # Output: 0, 1, 4, 9, 16

# 6. Benefits of Generators
# Generators are memory efficient since they yield items one at a time and only when requested.
# Example of a large range using a generator
def large_range_generator(n):
    for i in range(n):
        yield i

# Using large_range_generator
large_gen = large_range_generator(1000000)
print("First 5 values from a large generator:")
for _ in range(5):
    print(next(large_gen))  # Output: 0, 1, 2, 3, 4

# 7. State Retention in Generators
# Generators maintain their state between yields, allowing them to resume where they left off.
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

# Using count_up_to generator
counter = count_up_to(3)
print("Counting Up To 3:")
print(next(counter))  # Output: 1
print(next(counter))  # Output: 2
print(next(counter))  # Output: 3

# 8. Handling StopIteration Exception
# When there are no more values to yield, a generator raises a StopIteration exception.
try:
    print(next(counter))  # This will raise StopIteration
except StopIteration:
    print("Reached the end of the generator.")  # Output: Reached the end of the generator.

# 9. Generators in Practical Use Cases
# Generators can be useful for reading large files line by line
def read_large_file(file_name):
    with open(file_name) as file:
        for line in file:
            yield line.strip()

# Example usage (assuming 'large_file.txt' exists)
# file_generator = read_large_file('large_file.txt')
# for line in file_generator:
#     print(line)

# 10. Conclusion
print("Generators provide a powerful and memory-efficient way to work with large data sets and streams of data.")
