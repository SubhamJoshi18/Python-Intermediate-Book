# Python Decorators Documentation Example

# 1. Introduction to Decorators
# Decorators are a powerful and useful tool in Python that allows you to modify the behavior of a function or class.
# A decorator is essentially a function that takes another function as an argument and extends or alters its behavior.

# 2. Creating a Simple Decorator
def simple_decorator(func):
    """A simple decorator that prints 'Before' and 'After' the function call."""
    def wrapper():
        print("Before the function call")
        func()  # Call the original function
        print("After the function call")
    return wrapper

# 3. Using the Simple Decorator
@simple_decorator
def say_hello():
    """A simple function that prints 'Hello!'."""
    print("Hello!")

print("Using Simple Decorator:")
say_hello()
# Output:
# Before the function call
# Hello!
# After the function call

# 4. Decorators with Arguments
# To create a decorator that accepts arguments, we need to nest functions.
def repeat_decorator(num_times):
    """A decorator that repeats the function call a specified number of times."""
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)  # Call the original function
        return wrapper
    return decorator_repeat

# 5. Using the Decorator with Arguments
@repeat_decorator(3)
def greet(name):
    """A function that greets a person."""
    print(f"Hello, {name}!")

print("Using Repeat Decorator:")
greet("Alice")
# Output:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!

# 6. Decorators for Timing Functions
import time

def timer_decorator(func):
    """A decorator that measures the execution time of a function."""
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.4f} seconds")
        return result
    return wrapper

# 7. Using the Timer Decorator
@timer_decorator
def long_running_function():
    """A function that simulates a long-running task."""
    time.sleep(2)  # Sleep for 2 seconds

print("Using Timer Decorator:")
long_running_function()
# Output:
# Execution time: 2.0001 seconds

# 8. Chaining Decorators
# You can apply multiple decorators to a single function by stacking them.
@timer_decorator
@repeat_decorator(2)
def say_goodbye(name):
    """A function that says goodbye."""
    print(f"Goodbye, {name}!")

print("Using Chained Decorators:")
say_goodbye("Bob")
# Output (execution time may vary):
# Execution time: 4.0001 seconds
# Goodbye, Bob!
# Goodbye, Bob!

# 9. Decorators for Class Methods
# Decorators can also be applied to class methods.
class MyClass:
    def __init__(self, name):
        self.name = name

    @timer_decorator
    def greet(self):
        """A method that greets the class instance."""
        print(f"Hello, {self.name}!")

# 10. Using Decorators in Classes
print("Using Decorator in Class:")
obj = MyClass("Charlie")
obj.greet()
# Output (execution time may vary):
# Execution time: 0.0001 seconds
# Hello, Charlie!

# 11. Conclusion
print("Decorators are a versatile feature in Python that enhance the functionality of functions and methods.")
