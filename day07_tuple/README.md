**Q1: Write a Python program to create a tuple and access its elements using indices.**

**Objective:**
Write a Python program to create a tuple and access individual elements using indexing.

**Background:**
Tuples are ordered, immutable sequences in Python. They are similar to lists, but their elements cannot be changed. Elements can be accessed using indices.
This problem helps beginners understand how to:
* Define a tuple
* Use indexing to access tuple elements
* Print specific items from a tuple

Sample Program:

```
my_tuple = ("apple", "banana", "cherry")
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])
```

**Q2: Write a Python program to add an item to a tuple.**

**Objective:**
Write a Python program to demonstrate how to add an item to a tuple using tuple concatenation.

**Background:**
Tuples are immutable, which means elements cannot be added directly. However, you can create a new tuple by concatenating the original with another tuple.

This problem helps beginners understand how to:
* Work with immutable data structures
* Perform tuple concatenation
* Display the updated result

Sample Program:

```
my_tuple = (1, 2, 3)
new_tuple = my_tuple + (4,)
print("Updated tuple:", new_tuple)
```

**Q3: Write a Python program to demonstrate the immutability of a tuple.**

**Objective:**
Write a Python program to show that once created, elements of a tuple cannot be modified.

**Background:**
Unlike lists, tuples do not allow changes to their items after creation. Any attempt to assign a new value to a tuple index will raise a TypeError.

This problem helps beginners understand how to:
* Work with immutable data types
* Understand runtime errors
* Distinguish between tuples and lists

Sample Program:

```
my_tuple = (10, 20, 30)
# Uncommenting the next line will cause an error
# my_tuple[1] = 25
print("Tuples are immutable. You cannot change elements.")
```

**Q4: Write a Python program to check if an element exists in a tuple.**

**Objective:**
Write a Python program to test whether a specified element exists in a tuple.

**Background:**
The in operator in Python can be used to check for membership in data structures like tuples, lists, sets, etc.

This problem helps beginners understand how to:
* Use membership operators
* Work with conditional logic
* Check values inside tuples

Sample Program:

```
my_tuple = ("a", "b", "c")
print("b" in my_tuple)  # Output: True
```

**Q5: Write a Python program to create a set and add elements to it.**

**Objective:**
Write a Python program to create a set and use the add() method to insert elements.

**Background:**
Sets are unordered collections of unique items. Elements can be added using the add() method. Duplicates are automatically ignored.

This problem helps beginners understand how to:
* Create and use sets
* Add unique elements
* Display updated sets

Sample Program:

```
my_set = set()
my_set.add(10)
my_set.add(20)
print("Set after additions:", my_set)
```

**Q6: Write a Python program to remove an element from a set.**

**Objective:**
Write a Python program to remove a specific element from a set using remove().

**Background:**
The remove() method deletes an element from a set. If the element is not present, it raises a KeyError.

This problem helps beginners understand how to:
* Modify sets
* Remove elements safely
* Work with error-prone operations

Sample Program:

```
my_set = {1, 2, 3, 4}
my_set.remove(3)
print("Set after removal:", my_set)
```

**Q7: Write a Python program to perform set operations (union, intersection, difference) on two sets.**

**Objective:**
Write a Python program to perform and display union, intersection, and difference between two sets.

**Background:**
Python sets support standard mathematical set operations like union (|), intersection (&), and difference (-).

This problem helps beginners understand how to:
* Combine sets
* Find common or unique elements
* Use set operators for computation

Sample Program:

```
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
```

**Q8: Write a Python program to create a set from a list and print it.**

**Objective:**
Write a Python program to convert a list into a set and print the resulting set.

**Background:**
You can convert a list to a set using the set() function. This automatically removes any duplicate values.

This problem helps beginners understand how to:
* Convert data types
* Remove duplicates from lists
* Print unique items

Sample Program:

```
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(my_list)
print("Set from list:", unique_set)
```
