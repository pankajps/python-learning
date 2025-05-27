**Q1: Write a Python program that demonstrates string concatenation.**

**Objective:**
Write a Python program that combines two or more strings into one using concatenation.

**Background:**
String concatenation is done using the + operator in Python, which joins multiple strings into a single string.

This problem helps beginners understand how to:
* Concatenate strings
* Use the + operator with strings
* Display combined messages

Sample Program:

```
first = "Hello"
second = "World"
result = first + " " + second
print("Concatenated string:", result)
```

**Q2: Write a Python program to check if a string contains a specific character.**

**Objective:**
Write a Python program to search for a specific character in a string using the in operator.

**Background:**
The in operator checks for membership, and it can be used to determine if a character or substring is present.

This problem helps beginners understand how to:
* Use the in keyword
* Check character presence
* Implement simple conditional checks

Sample Program:

```
text = "Python Programming"
if "g" in text:
    print("Character 'g' found in the string.")
else:
    print("Character not found.")
```

**Q3: Write a Python program to replace a substring in a string with another string.**

**Objective:**
Write a Python program to replace part of a string with another substring using the replace() method.

**Background:**
The replace() method returns a new string where all occurrences of a specified value are replaced with another value.

This problem helps beginners understand how to:
* Use string methods
* Modify text dynamically
* Apply search-and-replace logic

Sample Program:

```
text = "I love Java"
updated = text.replace("Java", "Python")
print("Updated string:", updated)
```

**Q4: Write a Python program to find the length of a string.**

**Objective:**
Write a Python program to determine the number of characters in a string using the len() function.

**Background:**
The len() function returns the total number of characters in a string, including spaces and symbols.

This problem helps beginners understand how to:
* Use built-in functions
* Analyze string data
* Perform basic string operations

Sample Program:

```
message = "Hello, World!"
print("Length of string:", len(message))
```

**Q5: Write a Python program that extracts a substring from a string.**

**Objective:**
Write a Python program to extract a portion of a string using slicing.

**Background:**
Slicing allows you to extract specific ranges of characters from a string using index notation: string[start:end].

This problem helps beginners understand how to:
* Use slicing with strings
* Access specific parts of text
* Manipulate substrings

Sample Program:

```
text = "Python Programming"
substring = text[0:6]
print("Extracted substring:", substring)
```

**Q6: Write a Python program that converts a string into uppercase and lowercase.**

**Objective:**
Write a Python program that changes a string to both uppercase and lowercase using upper() and lower() methods.

**Background:**
Python provides built-in methods for case conversion, useful for formatting and standardizing input.

This problem helps beginners understand how to:
* Use string methods like upper() and lower()
* Handle text formatting
* Transform user input

Sample Program:

```
text = "Python"
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
```

**Q7: Write a Python program that checks if a string is palindrome.**

**Objective:**
Write a Python program to check if a string reads the same forwards and backwards.

**Background:**
A palindrome is a word or phrase that is the same when reversed. You can reverse a string using slicing [::-1].

This problem helps beginners understand how to:
* Reverse strings
* Compare strings
* Apply logic to check patterns

Sample Program:

```
word = "madam"
if word == word[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
```

**Q8: Write a Python program to compare two strings.**

**Objective:**
Write a Python program that compares two strings and prints whether they are equal or not.

**Background:**
String comparison can be done using ==, which returns True if the strings have the same content.

This problem helps beginners understand how to:
* Compare strings
* Use if statements with equality checks
* Handle user-defined input comparisons

Sample Program:

```
str1 = "Python"
str2 = "python"

if str1 == str2:
    print("The strings are equal.")
else:
    print("The strings are not equal.")
```
