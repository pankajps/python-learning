**Q1: Write a Python program that prints "Hello, World!" and stops the program immediately using the break statement.**

**Objective:**
Write a Python program that prints a message and immediately terminates a loop using break.

**Background:**
The break statement is used to exit a loop prematurely, regardless of the loop condition.

This problem helps beginners understand how to:
* Use break to control loop flow
* Exit loops on specific conditions
* Understand loop termination

Sample Program:

```
while True:
    print("Hello, World!")
    break
```

**Q2: Write a Python program to print numbers from 1 to 10, but skip the number 5 using the continue statement.**

**Objective:**
Write a Python program that uses continue to skip a specific number while iterating through a range.

**Background:**
The continue statement skips the current iteration and moves to the next one in a loop.

This problem helps beginners understand how to:
* Use continue for skipping
* Filter out values in loops
* Manage flow control in iterations

Sample Program:

```
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
```

**Q3: Write a Python program that demonstrates the use of the pass statement. The program should do nothing when executed.**

**Objective:**
Write a Python program that includes the pass statement and shows it does nothing during execution.

**Background:**
The pass statement acts as a placeholder when a statement is syntactically required but no action is needed.

This problem helps beginners understand how to:
* Use pass in block structures
* Create empty conditionals or loops
* Write syntactically correct code without logic

Sample Program:

```
if True:
    pass  # Does nothing

# Program ends without any output
```

**Q4: Write a Python program to print numbers from 1 to 10, but stop the loop when the number 6 is reached using break.**

**Objective:**
Write a Python program that terminates a loop when a certain condition (number 6) is met using break.

**Background:**
The break statement is often used for early termination based on specific criteria.

This problem helps beginners understand how to:
* Use conditional logic in loops
* Interrupt loops with break
* Control flow with decision points

Sample Program:

```
for i in range(1, 11):
    if i == 6:
        break
    print(i)
```

**Q5: Write a Python program to add two numbers and print the result using Arithmetic Operators (+).**

**Objective:**
Write a Python program to perform addition using the + operator and print the result.

**Background:**
Arithmetic operators are used for basic mathematical operations. The + operator is used to add values.

This problem helps beginners understand how to:
* Use the + operator
* Take inputs and convert types
* Perform and display calculations

Sample Program:

```
a = 7
b = 3
sum_result = a + b
print("Sum:", sum_result)
```

**Q6: Write a Python program to compare two numbers and print if the first one is greater than the second using Comparison Operators (>).**

**Objective:**
Write a Python program that compares two values using the > operator and prints a message based on the result.

**Background:**
Comparison operators are used to compare values and return a Boolean result (True or False).

This problem helps beginners understand how to:
* Use comparison operators
* Evaluate conditions
* Print messages based on comparisons

Sample Program:

```
x = 10
y = 5
if x > y:
    print("x is greater than y")
```

**Q7: Write a Python program that assigns a value to a variable and then modifies it using the Assignment Operator (+=).**

**Objective:**
Write a Python program that shows how to use compound assignment to update a variable.

**Background:**
The += operator is a shorthand for x = x + value, commonly used for counters and accumulations.

This problem helps beginners understand how to:
* Use assignment and compound operators
* Update variable values efficiently
* Write concise arithmetic logic

Sample Program:

```
counter = 10
counter += 5
print("Updated value:", counter)
```

**Q8: Write a Python program to calculate the sum of two numbers using the Arithmetic Operators (+).**

**Objective:**
Write a Python program to compute the sum of two numbers using the + operator.

**Background:**
Arithmetic operations are core to all programming tasks. Addition is one of the most fundamental operations.

This problem helps beginners understand how to:
* Use arithmetic operators
* Perform addition
* Store and print results

Sample Program:

```
num1 = 8
num2 = 4
total = num1 + num2
print("Sum of two numbers is:", total)
```
