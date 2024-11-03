# Python Strings Documentation Example

# 1. Introduction to Strings
# Strings in Python are sequences of characters enclosed in single quotes (' ') or double quotes (" ").
# They are immutable, meaning once a string is created, it cannot be modified.

# 2. Creating Strings
string1 = "Hello, World!"
string2 = 'Python is fun!'

print("Created Strings:")
print(string1)  # Output: Hello, World!
print(string2)  # Output: Python is fun!

# 3. String Length
# The length of a string can be obtained using the len() function.
length_string1 = len(string1)
print("Length of string1:", length_string1)  # Output: 13

# 4. String Indexing and Slicing
# Strings can be indexed and sliced to access individual characters or substrings.
first_character = string1[0]
substring = string1[0:5]  # Slicing from index 0 to 4

print("First character:", first_character)  # Output: H
print("Substring (first 5 characters):", substring)  # Output: Hello

# 5. String Methods
# Python provides various built-in methods for string manipulation.

# 5.1. Changing Case
upper_case = string2.upper()  # Convert to uppercase
lower_case = string2.lower()  # Convert to lowercase
title_case = string2.title()  # Convert to title case

print("Uppercase:", upper_case)  # Output: PYTHON IS FUN!
print("Lowercase:", lower_case)  # Output: python is fun!
print("Title case:", title_case)  # Output: Python Is Fun!

# 5.2. Stripping Whitespace
string_with_spaces = "   Hello, Python!   "
stripped_string = string_with_spaces.strip()  # Remove leading and trailing spaces

print("Stripped string:", stripped_string)  # Output: Hello, Python!

# 5.3. Finding Substrings
index_of_python = string2.find("Python")  # Find the index of the substring "Python"
not_found_index = string2.find("Java")  # Substring not found returns -1

print("Index of 'Python':", index_of_python)  # Output: 0
print("Index of 'Java':", not_found_index)  # Output: -1

# 5.4. Replacing Substrings
replaced_string = string2.replace("fun", "awesome")  # Replace 'fun' with 'awesome'

print("Replaced string:", replaced_string)  # Output: Python is awesome!

# 5.5. Splitting and Joining Strings
sentence = "This is a string."
words = sentence.split()  # Split the string into a list of words
joined_string = " ".join(words)  # Join the list back into a string

print("Words in the sentence:", words)  # Output: ['This', 'is', 'a', 'string.']
print("Joined string:", joined_string)  # Output: This is a string.

# 6. String Formatting
# Python provides several ways to format strings.

# 6.1. Old-style formatting
name = "Shubham"
greeting_old = "Hello, %s!" % name
print("Old-style formatting:", greeting_old)  # Output: Hello, Shubham!

# 6.2. str.format() method
greeting_new = "Hello, {}!".format(name)
print("str.format() method:", greeting_new)  # Output: Hello, Shubham!

# 6.3. f-strings (Python 3.6+)
greeting_fstring = f"Hello, {name}!"
print("f-string formatting:", greeting_fstring)  # Output: Hello, Shubham!

# 7. Multiline Strings
# Multiline strings can be created using triple quotes (''' or """).
multiline_string = """This is a string
that spans multiple
lines."""
print("Multiline string:")
print(multiline_string)
# Output:
# This is a string
# that spans multiple
# lines.

# 8. Checking String Properties
# You can check various properties of strings using methods like isalpha(), isdigit(), isspace(), etc.
alpha_string = "Hello"
digit_string = "12345"
space_string = "   "

print("Is alpha:", alpha_string.isalpha())  # Output: True
print("Is digit:", digit_string.isdigit())  # Output: True
print("Is space:", space_string.isspace())  # Output: True

# 9. Conclusion
print("Strings in Python are versatile and offer many built-in methods for manipulation and formatting.")
