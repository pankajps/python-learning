**Q1: Write a Python program to print "Hello, World!" using a user-defined function.**

**Objective:**
Write a Python program that defines and calls a user-defined function to print "Hello, World!".

**Background:**
Functions are reusable blocks of code that perform specific tasks. A basic function can be used to encapsulate logic like printing messages.

This problem helps beginners understand how to:
* Define a simple function
* Call a function
* Use print() within a function

Sample Program:

```
def greet():
    print("Hello, World!")

greet()
```

**Q2: Write a function that takes no arguments and prints "Welcome to Python!".**

**Objective:**
Define a function with no parameters that prints a welcome message.

**Background:**
Functions without arguments are useful when the task doesn’t depend on external inputs.

This problem helps beginners understand how to:
* Create parameterless functions
* Use print statements in functions
* Call functions for simple output

Sample Program:

```
def welcome():
    print("Welcome to Python!")

welcome()
```

**Q3: Define a function that takes two numbers as arguments and prints their sum.**

**Objective:**
Write a Python function that accepts two arguments and prints the result of their addition.

**Background:**
Functions can take parameters to perform operations on external values, making them flexible and reusable.

This problem helps beginners understand how to:
* Use function parameters
* Perform arithmetic inside functions
* Print calculated results

Sample Program:

```
def add_numbers(a, b):
    print("Sum:", a + b)

add_numbers(5, 7)
```

**Q4: Write a function that accepts a number and returns its square.**

**Objective:**
Write a function that takes a number as input and returns its square value.

**Background:**
Functions that return values can be used in expressions or further computations.

This problem helps beginners understand how to:
* Use return statements
* Perform mathematical operations
* Store and reuse function results

Sample Program:

```
def square(num):
    return num * num

result = square(4)
print("Square:", result)
```

**Q5: Create a function that takes no arguments but returns the string "Goodbye!".**

**Objective:**
Write a Python function that takes no inputs and returns a string value.

**Background:**
A return statement can be used in a function to send back data, which can be used or printed outside the function.

This problem helps beginners understand how to:
* Return values from functions
* Work with strings
* Use functions in variable assignments

Sample Program:

```
def farewell():
    return "Goodbye!"

print(farewell())
```

**Q6: Define a function that returns the result of multiplying two numbers passed as arguments.**

**Objective:**
Write a Python function that accepts two numbers and returns their product.

**Background:**
Functions can return the result of computations for use in expressions or other logic.

This problem helps beginners understand how to:
* Multiply numbers in a function
* Return values using return
* Reuse returned results

Sample Program:

```
def multiply(x, y):
    return x * y

product = multiply(3, 4)
print("Product:", product)
```

**Q7: Write a function with default arguments where the default value of a name is "User" and print "Hello, User!".**

**Objective:**
Define a Python function with a default parameter and print a greeting message.

**Background:**
Default arguments allow functions to be called with or without arguments, providing flexibility and fallback behavior.

This problem helps beginners understand how to:
* Use default parameters
* Handle optional function arguments
* Format strings in output

Sample Program:

```
def greet(name="User"):
    print(f"Hello, {name}!")

greet()
greet("Alice")
```

**Q8: Write a function that accepts two numbers and prints whether the first is greater than the second.**

**Objective:**
Write a Python function to compare two input values and print a message based on the comparison.

**Background:**
Conditional logic inside functions allows dynamic decision-making based on input values.

This problem helps beginners understand how to:
* Use conditional statements in functions
* Compare function arguments
* Output logical results

Sample Program:

```
def compare(a, b):
    if a > b:
        print("First number is greater than the second.")
    else:
        print("First number is not greater than the second.")

compare(10, 5)
compare(3, 8)
```
