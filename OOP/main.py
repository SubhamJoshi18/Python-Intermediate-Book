# Python Object-Oriented Programming Documentation Example

# 1. Introduction to OOP
# Object-Oriented Programming (OOP) is a programming paradigm that uses objects to represent data and methods.
# OOP allows for code reusability, encapsulation, inheritance, and polymorphism.

# 2. Defining a Class
# A class is a blueprint for creating objects. It can contain attributes (data) and methods (functions).

class Animal:
    """A class to represent an animal."""

    def __init__(self, name, species):
        """Initialize the animal with a name and species."""
        self.name = name        # Attribute: name of the animal
        self.species = species  # Attribute: species of the animal

    def speak(self):
        """Method to make the animal speak."""
        raise NotImplementedError("Subclasses must implement this method.")

# 3. Creating Objects
# Objects are instances of classes. You can create multiple objects from a class.

dog = Animal("Buddy", "Dog")  # Create an Animal object
print(f"{dog.name} is a {dog.species}.")  # Output: Buddy is a Dog.

# 4. Inheritance
# Inheritance allows a class (child) to inherit attributes and methods from another class (parent).

class Dog(Animal):
    """A class to represent a dog, inheriting from Animal."""

    def speak(self):
        """Override the speak method for dogs."""
        return "Woof!"

class Cat(Animal):
    """A class to represent a cat, inheriting from Animal."""

    def speak(self):
        """Override the speak method for cats."""
        return "Meow!"

# 5. Using Inherited Classes
# You can create objects of the derived classes and use their methods.

my_dog = Dog("Rex", "Dog")
print(f"{my_dog.name} says: {my_dog.speak()}")  # Output: Rex says: Woof!

my_cat = Cat("Whiskers", "Cat")
print(f"{my_cat.name} says: {my_cat.speak()}")  # Output: Whiskers says: Meow!

# 6. Encapsulation
# Encapsulation restricts access to certain attributes or methods to protect data.
# You can use private attributes by prefixing with an underscore (_).

class BankAccount:
    """A class to represent a bank account."""

    def __init__(self, owner, balance=0):
        """Initialize the account with an owner and a balance."""
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        """Method to deposit money into the account."""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Method to withdraw money from the account."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance.")

    def get_balance(self):
        """Method to get the current balance."""
        return self.__balance

# 7. Using Encapsulated Class
account = BankAccount("Alice")
account.deposit(1000)  # Output: Deposited: 1000
account.withdraw(500)   # Output: Withdrew: 500
print(f"Current Balance: {account.get_balance()}")  # Output: Current Balance: 500

# 8. Polymorphism
# Polymorphism allows methods to be used in different ways based on the object type.

def animal_sound(animal):
    """Function to print the sound made by an animal."""
    print(animal.speak())

# 9. Using Polymorphism
animal_sound(my_dog)  # Output: Woof!
animal_sound(my_cat)  # Output: Meow!

# 10. Conclusion
print("Object-Oriented Programming in Python promotes code reusability and organization through classes and objects.")
