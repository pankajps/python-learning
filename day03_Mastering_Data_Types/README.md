**Q1: Write a Python program to demonstrate data types.**

**Objective:**
Write a Python program to declare variables of different data types and print their values and types.

**Background:**
Python supports various built-in data types like int, float, str, bool, and complex. Understanding data types is fundamental to Python programming.

This problem helps beginners understand how to:
* Declare variables of different data types
* Use the type() function
* Identify Python data types

Sample Program:

```
a = 10             # int
b = 3.14           # float
c = "Python"       # string
d = True           # boolean
e = 2 + 3j         # complex

print(type(a), type(b), type(c), type(d), type(e))
```

**Q2: Write a Python program to convert an integer to a string and print its type.**

**Objective:**
Write a Python program to convert an integer into a string using str() and display its type.

**Background:**
Type conversion allows changing a variable's data type. The str() function converts integers, floats, or other types into string representations.

This problem helps beginners understand how to:
* Perform type conversion
* Use the str() function
* Check data type with type()

Sample Program:

```
num = 100
converted = str(num)
print("Value:", converted)
print("Type after conversion:", type(converted))
```

**Q3: Write a Python program that checks the data type of a variable using type().**

**Objective:**
Write a Python program that determines and prints the type of a given variable using the type() function.

**Background:**
The type() function is used to inspect the data type of any object or variable.

This problem helps beginners understand how to:
* Check variable types
* Use introspection with built-in functions
* Verify data handling in programs

Sample Program:

```
x = [1, 2, 3]
print("Data type of x is:", type(x))
```

**Q4: Write a Python program that performs basic arithmetic operations on integers and floats.**

**Objective:**
Write a Python program to perform addition, subtraction, multiplication, and division with integers and floats.

**Background:**
Arithmetic operations like +, -, *, and / work on numeric types and are core to programming logic.

This problem helps beginners understand how to:
* Perform arithmetic with different numeric types
* Display results clearly
* Combine integers and floats in expressions

Sample Program:

```
a = 10
b = 3.5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
```

**Q5: Write a Python program that demonstrates the use of Boolean values.**

**Objective:**
Write a Python program to define Boolean variables and use them in a conditional statement.

**Background:**
Boolean values True and False are used for decision-making in programs and are results of comparison operations.

This problem helps beginners understand how to:
* Declare and use Boolean variables
* Apply Boolean logic in conditionals
* Work with if statements

Sample Program:

```
is_active = True
if is_active:
    print("The user is active.")
else:
    print("The user is inactive.")
```

**Q6: Write a Python program to add two floating-point numbers.**

**Objective:**
Write a Python program to perform addition of two float values and display the result.

**Background:**
Floating-point numbers represent decimal values and are often used in scientific and financial calculations.

This problem helps beginners understand how to:
* Declare float variables
* Perform arithmetic operations
* Print formatted float results

Sample Program:

```
x = 2.5
y = 4.75
sum_result = x + y
print("Sum of floats:", sum_result)
```

**Q7: Write a Python program to display a complex number and its type.**

**Objective:**
Write a Python program to define a complex number and print its value and data type.

**Background:**
Complex numbers are in the form a + bj, and Python supports complex number operations natively.

This problem helps beginners understand how to:
* Define complex numbers
* Use type() to inspect complex data
* Work with mathematical types

Sample Program:

```
z = 3 + 4j
print("Complex number:", z)
print("Type:", type(z))
```

**Q8: Write a Python program to demonstrate string manipulation (concatenate and length).**

**Objective:**
Write a Python program to concatenate two strings and find the length of the resulting string.

**Background:**
Strings can be combined using +, and their length is measured using len().

This problem helps beginners understand how to:
* Concatenate strings
* Measure string length
* Work with text in Python

Sample Program:

```
str1 = "Hello"
str2 = "World"
combined = str1 + " " + str2
print("Concatenated String:", combined)
print("Length:", len(combined))
```
