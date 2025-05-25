**Q1: Write a Python program to convert a string into an integer and add 10 to it.**

**Objective:**
Write a Python program to convert a string that contains a numeric value into an integer and perform addition.

**Background:**
In Python, type conversion is done using functions like int(). This allows converting a string containing digits into an integer for mathematical operations.
This problem helps beginners understand how to:
* Convert string data types to integers using int()
* Perform arithmetic operations
* Display numerical results with print()

Sample Program:

```
number_str = "25"
number = int(number_str)
result = number + 10
print("Result after adding 10:", result)
```

**Q2: Write a Python program to check if a number is True or False based on Boolean logic.**

**Objective:**
Write a Python program to evaluate a number in a Boolean context and print whether it is True or False.

**Background:**
In Python, any non-zero number is considered True and 0 is False when evaluated as a Boolean. This is useful in conditional logic.

This problem helps beginners understand how to:
* Use bool() to evaluate values
* Understand truthy and falsy concepts in Python
* Print Boolean results

Sample Program:

```
number = 5
print("Boolean value of number:", bool(number))
```

**Q3: Write a Python program to create a list of numbers and print the first and last element.**
**Objective:**
Write a Python program to define a list of numbers and access the first and last items using indexing.

**Background:**
Lists are ordered collections in Python. Elements are accessed using their indices, where index 0 is the first and -1 is the last.

This problem helps beginners understand how to:
* Create and use lists
* Access elements using positive and negative indices
* Display specific elements using print()

Sample Program:

```
numbers = [10, 20, 30, 40, 50]
print("First element:", numbers[0])
print("Last element:", numbers[-1])
```

**Q4: Write a Python program that appends an item to an existing list.**

**Objective:**
Write a Python program to add a new element to the end of a list using the append() method.

**Background:**
The append() method is used to insert a new item at the end of an existing list. This is a common operation in dynamic list building.

This problem helps beginners understand how to:
* Modify lists using methods
* Use append() to grow a list
* Print updated lists

Sample Program:

```
fruits = ["apple", "banana"]
fruits.append("cherry")
print("Updated list:", fruits)
```

**Q5: Write a Python program to access an element from a list using an index.**
**Objective:**
Write a Python program to access and print an item from a list using its index value.

**Background:**
In Python, lists are indexed starting from 0. You can retrieve any element by referencing its position with square brackets.

This problem helps beginners understand how to:
* Work with list indexing
* Access specific list elements
* Use print() to show the retrieved value

Sample Program:

```
colors = ["red", "green", "blue"]
print("Element at index 1:", colors[1])

**Q6: Write a Python program to calculate the sum of all elements in a list.**

**Objective:**
Write a Python program to compute the total sum of numerical elements in a list using sum().

**Background:**
The sum() function in Python takes an iterable like a list and returns the sum of its elements. It’s efficient for numeric list operations.

This problem helps beginners understand how to:
* Use built-in functions
* Operate on list contents
* Display calculated results

Sample Program:

```
numbers = [5, 10, 15, 20]
total = sum(numbers)
print("Sum of elements:", total)
```

**Q7: Write a Python program to demonstrate slicing in lists.**

**Objective:**
Write a Python program to extract a portion of a list using slicing and print the result.

**Background:**
List slicing allows selecting a range of elements from a list using the syntax list[start:end]. It’s helpful for accessing sublists.
* This problem helps beginners understand how to:
* Slice lists using index ranges
* Access subsets of list data
* Use slicing syntax effectively

Sample Program:

```
numbers = [10, 20, 30, 40, 50]
sub_list = numbers[1:4]
print("Sliced list:", sub_list)
```

**Q8: Write a Python program to create a Boolean variable and print its value.**

**Objective:**
Write a Python program to declare a Boolean variable and print its value.

**Background:**
Boolean variables hold True or False values. They are used in control flow, condition checks, and logic building in Python.
* This problem helps beginners understand how to:
* Declare Boolean variables
* Work with Boolean values
* Output Boolean results with print()

Sample Program:

```
is_active = True
print("Boolean value:", is_active)
```
