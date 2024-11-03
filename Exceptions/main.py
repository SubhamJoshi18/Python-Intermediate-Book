# Python Exceptions Documentation Example

# 1. Introduction to Exceptions
# Exceptions in Python are events that can modify the flow of a program. They occur when the program encounters an error.
# Python has built-in exceptions and allows for user-defined exceptions.

# 2. Basic Exception Handling
# The basic way to handle exceptions is by using the try-except block.

try:
    # This will raise a ZeroDivisionError
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Caught an exception: {e}")  # Output: Caught an exception: division by zero

# 3. Multiple Except Blocks
# You can handle multiple exceptions with separate except blocks.

try:
    value = int("not_a_number")  # This will raise a ValueError
except ValueError as e:
    print(f"Caught a ValueError: {e}")  # Output: Caught a ValueError: invalid literal for int() with base 10: 'not_a_number'
except TypeError as e:
    print(f"Caught a TypeError: {e}")

# 4. Catching Multiple Exceptions in One Block
# You can catch multiple exceptions in a single except block using a tuple.

try:
    result = 10 / 0
except (ZeroDivisionError, ValueError) as e:
    print(f"Caught an exception: {e}")  # Output: Caught an exception: division by zero

# 5. The else Clause
# The else clause can be used to define a block of code to be executed if no exceptions were raised.

try:
    result = 10 / 2
except ZeroDivisionError as e:
    print(f"Caught an exception: {e}")
else:
    print(f"Result is: {result}")  # Output: Result is: 5.0

# 6. The finally Clause
# The finally clause is used to execute code regardless of whether an exception was raised or not.

try:
    file = open('non_existent_file.txt', 'r')
except FileNotFoundError as e:
    print(f"Caught a FileNotFoundError: {e}")
finally:
    print("This block always executes.")  # Output: This block always executes.

# 7. Raising Exceptions
# You can raise exceptions using the raise statement.

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return age

try:
    check_age(-1)
except ValueError as e:
    print(f"Caught an exception: {e}")  # Output: Caught an exception: Age cannot be negative.

# 8. Creating Custom Exceptions
# You can create your own exception classes by extending the built-in Exception class.

class CustomError(Exception):
    """Custom exception class."""
    pass

def do_something():
    raise CustomError("This is a custom error.")

try:
    do_something()
except CustomError as e:
    print(f"Caught a custom exception: {e}")  # Output: Caught a custom exception: This is a custom error.

# 9. Exception Hierarchy
# All exceptions in Python are derived from the BaseException class.
# You can catch exceptions by their hierarchy.

try:
    raise IndexError("Index out of range.")
except LookupError as e:  # Catching a superclass exception
    print(f"Caught a LookupError: {e}")  # Output: Caught a LookupError: Index out of range.

# 10. Conclusion
print("Exception handling is crucial for building robust applications that can gracefully handle errors.")
