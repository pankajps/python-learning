**Q1: Write a Python program to open a file in write mode ('w') and write a string to it.**

**Objective:**
Write a Python program to open a file in write mode and write a single string to it.

**Background:**
Opening a file with 'w' mode will create the file if it doesn’t exist or overwrite it if it does. The write() function adds text to the file.

This problem helps beginners understand how to:
* Open a file in write mode
* Use the write() function
* Create or overwrite a file

Sample Program:

```
with open("demo.txt", "w") as file:
    file.write("This is a new file with some text.")
```

**Q2: Write a Python program to append data to an existing file.**

**Objective:**
Write a Python program to open a file in append mode and add new text without overwriting existing content.

**Background:**
Using the 'a' mode opens a file for appending data. Existing content remains unchanged, and new data is added at the end.

This problem helps beginners understand how to:
* Append data to a file
* Avoid data loss from overwriting
* Use file modes effectively

Sample Program:

```
with open("demo.txt", "a") as file:
    file.write("\nThis line is added at the end of the file.")
```

**Q3: Write a Python program that demonstrates the use of the with keyword for opening files.**

**Objective:**
Write a Python program that shows how the with keyword is used for handling files safely and efficiently.

**Background:**
The with statement automatically closes the file after the block is executed, even if an error occurs, promoting safe resource handling.

This problem helps beginners understand how to:
* Use context managers with with
* Open and handle files safely
* Write cleaner, error-safe file code

Sample Program:

```
with open("sample.txt", "w") as file:
    file.write("Using 'with' ensures the file is properly closed.")
```

**Q4: Write a Python program to read the contents of a file after appending to it.**

**Objective:**
Write a Python program to append text to a file and then read and display its updated content.

**Background:**
Combining 'a' mode with 'r' allows content to be added and then reviewed. You need to reopen the file in 'r' mode for reading.

This problem helps beginners understand how to:
* Perform write and read operations sequentially
* Work with different file modes
* Read updated file content

Sample Program:

```
# Append data
with open("demo.txt", "a") as file:
    file.write("\nAppended line for testing.")

# Read data
with open("demo.txt", "r") as file:
    content = file.read()
    print(content)
```

**Q5: Write a Python program to check if a file is empty and then write to it.**

**Objective:**
Write a Python program that checks whether a file is empty and writes data only if it is.

**Background:**
To determine if a file is empty, you can check its size using os.stat() or read its content and test if it’s an empty string.

This problem helps beginners understand how to:
* Check file size or content
* Prevent overwriting data in non-empty files
* Conditionally write to files

Sample Program:

```
import os

file_path = "check.txt"
if not os.path.exists(file_path) or os.stat(file_path).st_size == 0:
    with open(file_path, "w") as file:
        file.write("File was empty. Now it has content.")
else:
    print("File is not empty.")
```

**Q6: Write a Python program to open a file, add some data to it, and then read the data back.**

**Objective:**
Write a Python program that opens a file, writes new data, closes it, then reads and prints the full content.

**Background:**
This sequence ensures that the written data is saved and then accurately read back for verification or further processing.

This problem helps beginners understand how to:
* Write and read files sequentially
* Manage file state with mode changes
* Handle input/output with files

Sample Program:

```
with open("data.txt", "w") as file:
    file.write("This is some new data.\n")

with open("data.txt", "r") as file:
    print("Content after writing:")
    print(file.read())
```

**Q7: Write a Python program to append multiple lines to a file.**

**Objective:**
Write a Python program that appends several lines to a file using a list and the writelines() method.

**Background:**
writelines() can write a list of strings into a file. When appending, open the file in 'a' mode to preserve previous content.

This problem helps beginners understand how to:
* Write multiple lines using a list
* Use writelines() method
* Append content safely

Sample Program:

```
lines_to_add = ["\nLine 1", "\nLine 2", "\nLine 3"]

with open("demo.txt", "a") as file:
    file.writelines(lines_to_add)
```

**Q8: Write a Python program to overwrite an existing file with new content.**

**Objective:**
Write a Python program to completely replace the content of a file with new text using 'w' mode.

**Background:**
Opening a file in 'w' mode erases all existing data before writing the new content. This is used when content needs to be replaced.

This problem helps beginners understand how to:
* Safely overwrite file content
* Use write() for replacement
* Understand file mode behavior

Sample Program:

```
with open("overwrite.txt", "w") as file:
    file.write("This content overwrites the previous file content.")
```
