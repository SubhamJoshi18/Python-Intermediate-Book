# Python Logging Module Documentation Example

# 1. Introduction to Logging
# The logging module in Python is a standard module used to log messages from your application.
# It provides a flexible framework for emitting log messages from Python programs.

# 2. Importing the Logging Module
import logging

# 3. Basic Configuration
# The basicConfig() method is used to configure the logging system.
logging.basicConfig(level=logging.DEBUG,  # Set the logging level
                    format='%(asctime)s - %(levelname)s - %(message)s')  # Set the log message format

# 4. Logging Messages
# The logging module defines several levels of logging, in increasing order of severity.
# Here we demonstrate logging at different levels.

# 4.1. Logging Debug Messages
logging.debug("This is a debug message.")  # Debugging information, not for production use

# 4.2. Logging Info Messages
logging.info("This is an info message.")  # General information about program execution

# 4.3. Logging Warning Messages
logging.warning("This is a warning message.")  # Indication of a potential problem

# 4.4. Logging Error Messages
logging.error("This is an error message.")  # Indicates a failure in a function or operation

# 4.5. Logging Critical Messages
logging.critical("This is a critical message.")  # A serious error indicating that the program may not be able to continue

# 5. Logging Exceptions
# You can log exceptions with traceback information using the exception() method.
try:
    x = 1 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    logging.exception("An exception occurred: ")

# 6. Creating Custom Loggers
# You can create custom loggers for different parts of your application.

# 6.1. Creating a Logger
custom_logger = logging.getLogger("my_logger")
custom_logger.setLevel(logging.DEBUG)  # Set the log level for the custom logger

# 6.2. Adding a Console Handler
console_handler = logging.StreamHandler()  # Create a handler to output log messages to the console
console_handler.setLevel(logging.INFO)  # Set the log level for the handler

# 6.3. Setting a Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)  # Assign the formatter to the handler

# 6.4. Adding the Handler to the Logger
custom_logger.addHandler(console_handler)

# 7. Using the Custom Logger
custom_logger.debug("This debug message will not be shown in the console.")  # This will not appear because the console handler level is INFO
custom_logger.info("This is an info message from my_logger.")
custom_logger.warning("This is a warning message from my_logger.")
custom_logger.error("This is an error message from my_logger.")
custom_logger.critical("This is a critical message from my_logger.")

# 8. Logging to a File
# You can also log messages to a file by configuring a file handler.

# 8.1. Creating a File Handler
file_handler = logging.FileHandler('app.log')  # Log messages will be written to 'app.log'
file_handler.setLevel(logging.DEBUG)  # Set the log level for the file handler
file_handler.setFormatter(formatter)  # Use the same formatter as above

# 8.2. Adding the File Handler to the Custom Logger
custom_logger.addHandler(file_handler)

# 8.3. Log Messages to the File
custom_logger.info("This message will be logged to the file.")
custom_logger.error("This error message will also be logged to the file.")

# 9. Conclusion
print("Logging is an essential tool for tracking the execution of your programs and debugging.")
