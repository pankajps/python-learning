**Q1: Write a Python program to take input from the user and display it using print().**

**Objective:**
Write a Python program to accept input from the user and display the entered value using print().

**Background:**
The input() function is used to take input from users in string format. This is essential for interactive programs.

This problem helps beginners understand how to:
* Use input() to take user input
* Store input in a variable
* Display values using print()

Sample Program:

```
name = input("Enter your name: ")
print("Hello,", name)
```

**Q2: Write a Python program that uses input() to take two numbers and prints their sum.**

**Objective:**
Write a Python program to accept two numeric inputs from the user, convert them to integers, and display their sum.

**Background:**
By default, input() returns a string. To perform arithmetic, we must convert the input to numeric types using int() or float().

This problem helps beginners understand how to:
* Accept multiple inputs
* Convert strings to numbers
* Perform arithmetic operations

Sample Program:

```
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
total = num1 + num2
print("Sum:", total)
```

**Q3: Write a Python program to evaluate an expression entered by the user using eval().**

**Objective:**
Write a Python program that accepts a mathematical expression from the user and evaluates it using eval().

**Background:**
The eval() function executes a string expression as Python code. It can be used to dynamically compute input from users.

This problem helps beginners understand how to:
* Accept string input
* Use eval() to evaluate expressions
* Display computed results

Sample Program:

```
expr = input("Enter an expression (e.g., 10 + 5): ")
result = eval(expr)
print("Result:", result)
```

**Q4: Write a Python program that prints variables using the format() method.**

**Objective:**
Write a Python program to display variable values in a formatted string using the format() method.

**Background:**
The format() method allows insertion of values into strings using curly braces {}. It's useful for clean, readable output.

This problem helps beginners understand how to:
* Use the format() method
* Insert variables into strings
* Format output effectively

Sample Program:

```
name = "Alice"
age = 30
print("Name: {}, Age: {}".format(name, age))
```

**Q5: Write a Python program to concatenate two strings using the + operator.**

**Objective:**
Write a Python program to join two string variables using the + operator and print the result.

**Background:**
String concatenation combines strings using the + operator. It's one of the basic string operations in Python.

This problem helps beginners understand how to:
* Declare string variables
* Use + to concatenate
* Print the result

Sample Program:

```
first = "Hello"
second = "World"
result = first + " " + second
print("Concatenated string:", result)
```

**Q6: Write a Python program to repeat a string multiple times using the * operator.**

**Objective:**
Write a Python program to repeat a given string a specified number of times using the * operator.

**Background:**
In Python, the * operator can be used to repeat a string multiple times. It’s commonly used for formatting or pattern generation.

This problem helps beginners understand how to:
* Use the * operator with strings
* Control repetition of content
* Display repeated output

Sample Program:

```
word = "Hi! "
print(word * 3)
```

**Q7: Write a Python program that uses print() with the sep argument to print a list.**

**Objective:**
Write a Python program to print values separated by a custom delimiter using the sep parameter in print().

**Background:**
The sep argument in print() defines what string separates the printed items. This is useful for formatting output.

This problem helps beginners understand how to:
* Use multiple arguments in print()
* Customize separators using sep
* Control formatting in output

Sample Program:

```
items = ["apple", "banana", "cherry"]
print(*items, sep=", ")
```

**Q8: Write a Python program that asks for multiple inputs using split().**

**Objective:**
Write a Python program to take multiple space-separated inputs from the user and store them in separate variables or a list.

**Background:**
The split() method divides a string into a list using whitespace (by default). It's useful for collecting multiple values in a single line.

This problem helps beginners understand how to:
* Accept multiple values via input()
* Use split() to separate inputs
* Assign values to variables or store in lists

Sample Program:

```
x, y = input("Enter two numbers separated by space: ").split()
print("First number:", x)
print("Second number:", y)
```
