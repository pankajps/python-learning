**Q1:** Write a Python program to slice a string and print a portion of it.

**Objective:**
Write a Python program to extract a specific portion of a string using slicing and display it.

**Background:**
String slicing in Python allows access to a part of the string by specifying a range of indices using the syntax string[start:end]. This is useful when we want to extract substrings.

This problem helps beginners understand how to:
* Use indexing and slicing with strings
* Access portions of strings
* Display substrings using the print() function

Sample Program:

```
text = "Hello, World!"
sliced_text = text[0:5]
print("Sliced string:", sliced_text)
```

**Q2:** Write a Python program that uses strip() to remove leading and trailing whitespaces from a string.

**Objective:**
Write a Python program to remove leading and trailing spaces from a string using the strip() method.

**Background:**
The strip() method in Python removes any leading (spaces at the beginning) and trailing (spaces at the end) characters, commonly whitespaces. This is helpful in data cleaning.

This problem helps beginners understand how to:
* Use string methods in Python
* Clean input or formatted data
* Use print() to view changes in string formatting

Sample Program:

```
text = "   Hello, Python!   "
clean_text = text.strip()
print("Text after strip():", clean_text)
```

**Q3:** Write a Python program to count occurrences of a character in a string.

**Objective:**
Write a Python program to count how many times a specific character appears in a string.

**Background:**
The count() method returns the number of times a specified value appears in the string. It is useful for analyzing frequency of characters or substrings.

This problem helps beginners understand how to:
* Use built-in string methods
* Analyze strings for specific content
* Display results using print()

Sample Program:

```
text = "banana"
count_a = text.count('a')
print("Occurrences of 'a':", count_a)
```

**Q4:** Write a Python program that demonstrates the use of replace() method in strings.

**Objective:**
Write a Python program to replace a part of a string with another string using the replace() method.

**Background:**
The replace(old, new) method replaces all occurrences of a substring with another. It's commonly used in text processing and formatting.

This problem helps beginners understand how to:
* Modify string content dynamically
* Use the replace() method effectively
* Print updated strings

Sample Program:

```
text = "I like Java"
new_text = text.replace("Java", "Python")
print("Updated string:", new_text)
```

**Q5: **Write a Python program to demonstrate the len() method for strings.

**Objective:**
Write a Python program to find and print the length of a string using the len() function.

**Background:**
The len() function returns the number of characters in a string, including spaces and special characters. It’s useful for string analysis and validation.

This problem helps beginners understand how to:
* Use the len() function
* Work with string lengths for validation
* Output results using print()

Sample Program:

```
text = "Hello, World!"
length = len(text)
print("Length of the string:", length)
```

**Q6:** Write a Python program that concatenates two strings using + operator.

**Objective:**
Write a Python program to combine two strings into one using the + operator.

**Background:**
String concatenation joins two or more strings together. The + operator is a simple and common way to concatenate strings in Python.

This problem helps beginners understand how to:
* Combine strings
* Use the + operator with strings
* Display concatenated results

Sample Program:

```
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print("Concatenated string:", result)
```

**Q7:** Write a Python program to convert a string into a list of words.

**Objective:**
Write a Python program to split a string into a list of words using the split() method.

**Background:**
The split() method breaks a string into a list where each word is a list item, using space as the default delimiter. It is widely used in parsing and processing text.

This problem helps beginners understand how to:
* Use split() to tokenize strings
* Convert strings into lists
* Work with list data type in Python

Sample Program:

```
text = "Python is fun"
words = text.split()
print("List of words:", words)
```

**Q8:** Write a Python program to check if a string starts with a specified prefix.

**Objective:**
Write a Python program to check whether a given string starts with a specific prefix using startswith() method.

**Background:**
The startswith() method returns True if the string starts with the specified value. It is commonly used for validation and filtering text.

This problem helps beginners understand how to:
* Perform conditional checks on strings
* Use startswith() method
* Display boolean results in Python

Sample Program:

```
text = "OpenAI develops AI"
result = text.startswith("OpenAI")
print("Starts with 'OpenAI':", result)
```
