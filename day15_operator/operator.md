**Q1: Write a Python program that uses the and operator to check if a number is both greater than 5 and less than 10.**

**Objective:**
Write a Python program to evaluate a number using the and logical operator and print a message if the condition is true.

**Background:**
The and operator returns True only if both conditions are true. It’s commonly used for range checking.

This problem helps beginners understand how to:
* Use logical and in conditionals
* Evaluate compound conditions
* Apply range-based logic

Sample Program:

```
num = 7
if num > 5 and num < 10:
    print("The number is greater than 5 and less than 10.")
```

**Q2: Write a Python program that uses the or operator to check if a number is either less than 10 or greater than 20.**

**Objective:**
Write a Python program that checks if a number satisfies either of two conditions using the or operator.

**Background:**
The or operator returns True if at least one condition is true.

This problem helps beginners understand how to:
* Use or in conditional logic
* Handle multiple branches of evaluation
* Interpret flexible comparisons

Sample Program:

```
num = 25
if num < 10 or num > 20:
    print("The number is either less than 10 or greater than 20.")
```

**Q3: Write a Python program that uses the not operator to check if a number is not equal to 0.**

**Objective:**
Write a Python program to evaluate a condition using the not operator and act when the value is not zero.

**Background:**
The not operator inverts a Boolean expression. It is used to check the opposite of a condition.

This problem helps beginners understand how to:
* Use not to negate conditions
* Work with simple logic inversions
* Prevent zero-value operations

Sample Program:

```
num = 5
if not num == 0:
    print("The number is not zero.")
```

**Q4: Write a Python program to perform a bitwise AND operation between 6 and 3 and print the result.**

**Objective:**
Write a Python program to demonstrate bitwise operations using & between two integers.

**Background:**
The & operator compares each bit of two numbers and returns a number whose bits are 1 only when both bits are 1.

This problem helps beginners understand how to:
* Apply bitwise operators
* Understand binary representations
* Use & for low-level logical operations

Sample Program:

```
a = 6  # 110
b = 3  # 011
result = a & b  # 010 -> 2
print("Bitwise AND of 6 and 3 is:", result)
```

**Q5: Write a Python program to check if the number 4 is divisible by 2 and 4 using the bitwise AND (&) operator.**

**Objective:**
Write a Python program to check divisibility of 4 by 2 and 4 using bitwise operations.

**Background:**
For powers of two, bitwise AND with (number - 1) can be used to determine if a number is a power of 2. Alternatively, modulus checks can be done with logic combined using &.

This problem helps beginners understand how to:
* Use bitwise logic in conditionals
* Combine conditions using logical and
* Understand binary divisibility

Sample Program:

```
num = 4
if num & 1 == 0 and num & 3 == 0:
    print("4 is divisible by both 2 and 4.")
else:
    print("4 is not divisible by both 2 and 4.")
Note: This is a bitwise expression example, but for clarity and correctness, regular modulus % is typically preferred for divisibility.
```

**Q6: Write a Python program that checks if the string "Python" is in a list of strings.**

**Objective:**
Write a Python program to check the presence of a specific string within a list using the in operator.

**Background:**
The in operator checks for membership and returns True if an item exists in a sequence.

This problem helps beginners understand how to:
* Use the in operator
* Work with lists and strings
* Check membership conditions

Sample Program:

```
languages = ["Java", "C++", "Python", "JavaScript"]
if "Python" in languages:
    print("Python is in the list.")
```

**Q7: Write a Python program to check if the value 10 is not in a list of numbers.**

**Objective:**
Write a Python program that uses the not in operator to verify a number’s absence from a list.

**Background:**
The not in operator is the negated form of in, useful for ensuring certain values are excluded.

This problem helps beginners understand how to:
* Use not in for exclusion checks
* Work with lists and conditionals
* Make decisions based on data absence

Sample Program:

```
numbers = [1, 2, 3, 4, 5]
if 10 not in numbers:
    print("10 is not in the list.")
```

**Q8: Write a Python program to compare two lists with identical content using the is operator.**

**Objective:**
Write a Python program to compare whether two lists are the same object in memory using the is operator.

**Background:**
The is operator checks identity, not equality. Even if two lists have the same content, they may not refer to the same object.

This problem helps beginners understand how to:
* Use is vs ==
* Understand object identity
* Compare memory references

Sample Program:

```
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print("list1 is list2:", list1 is list2)  # Output: False
```
