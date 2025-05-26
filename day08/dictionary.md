**Q1: Write a Python program to create a dictionary and access its elements using keys.**

**Objective:**
Write a Python program to create a dictionary and retrieve values using specific keys.

**Background:**
A dictionary in Python is a collection of key-value pairs. Values are accessed using their corresponding keys with square brackets [] or the get() method.

This problem helps beginners understand how to:
* Define a dictionary
* Access elements using keys
* Display dictionary values

Sample Program:

```
person = {"name": "Alice", "age": 30, "city": "New York"}
print("Name:", person["name"])
print("Age:", person["age"])
```

**Q2: Write a Python program to add a new key-value pair to a dictionary.**

**Objective:**
Write a Python program to add new data to an existing dictionary by assigning a value to a new key.

**Background:**
Dictionaries are mutable, allowing insertion of new key-value pairs simply by assigning a value to a new key name.

This problem helps beginners understand how to:
* Update a dictionary
* Use keys to insert data
* Print modified dictionaries

Sample Program:

```
person = {"name": "Bob", "age": 25}
person["country"] = "USA"
print("Updated dictionary:", person)
```

**Q3: Write a Python program to delete a key-value pair from a dictionary.**

**Objective:**
Write a Python program to remove an entry from a dictionary using the del keyword.

**Background:**
To delete a specific key-value pair from a dictionary, you can use the del statement with the key name.

This problem helps beginners understand how to:
* Modify dictionary content
* Use the del statement
* Display updated dictionary data

Sample Program:

```
person = {"name": "Eve", "age": 28, "city": "Paris"}
del person["city"]
print("After deletion:", person)
```

**Q4: Write a Python program to find the length of a dictionary.**

**Objective:**
Write a Python program to count the number of key-value pairs in a dictionary using len().

**Background:**
The len() function, when applied to a dictionary, returns the number of items (key-value pairs) it contains.

This problem helps beginners understand how to:
* Use the len() function with dictionaries
* Count dictionary entries
* Display results with print()

Sample Program:

```
my_dict = {"a": 1, "b": 2, "c": 3}
print("Length of dictionary:", len(my_dict))
```

**Q5: Write a Python program to check if a key exists in a dictionary.**

**Objective:**
Write a Python program to verify whether a specific key is present in a dictionary using the in keyword.

**Background:**
The in operator checks if a specified key exists in a dictionary. It's often used in conditional statements for safe access.

This problem helps beginners understand how to:
* Perform membership checks on dictionaries
* Use conditional statements with dictionaries
* Prevent key access errors

Sample Program:

```
student = {"name": "Tom", "grade": "A"}
print("grade" in student)  # Output: True
print("age" in student)    # Output: False
```

**Q6: Write a Python program to iterate over a dictionary and print all keys and values.**

**Objective:**
Write a Python program to loop through a dictionary and display each key-value pair.

**Background:**
The items() method returns a view object of dictionary pairs, allowing iteration with a for loop to access both keys and values.

This problem helps beginners understand how to:
* Iterate over dictionaries
* Use the items() method
* Print formatted key-value pairs

Sample Program:

```
user = {"username": "john_doe", "email": "john@example.com"}
for key, value in user.items():
    print(f"{key}: {value}")
```

**Q7: Write a Python program that uses range() function to generate a range of numbers and print them.**

**Objective:**
Write a Python program to generate a sequence of numbers using the range() function and display them using a loop.

**Background:**
The range() function produces an immutable sequence of numbers and is commonly used in loops to repeat operations.

This problem helps beginners understand how to:
* Use the range() function
* Create loops in Python
* Print sequences of numbers

Sample Program:

```
for num in range(1, 6):
    print(num)
```

**Q8: Write a Python program that uses eval() to evaluate an arithmetic expression.**

**Objective:**
Write a Python program to evaluate a user-defined arithmetic expression using the eval() function.

**Background:**
The eval() function evaluates a string as a Python expression. It’s useful for dynamic evaluation but must be used carefully due to security risks.

This problem helps beginners understand how to:
* Take input as a string expression
* Evaluate it using eval()
* Handle dynamic expressions

Sample Program:

```
expression = "10 + 5 * 2"
result = eval(expression)
print("Result of expression:", result)
```
