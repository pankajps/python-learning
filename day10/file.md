**Q1: Write a Python program to open a file in write mode ('w') and write some text into it.**

**Objective:**
Write a Python program to create or overwrite a file and write text to it using write mode 'w'.

**Background:**
In Python, opening a file with 'w' mode allows writing to the file. If the file doesn't exist, it is created. If it exists, the content is overwritten.

This problem helps beginners understand how to:
* Open files in write mode
* Use the write() function
* Work with file objects

Sample Program:

```
with open("example.txt", "w") as file:
    file.write("Hello, this is a test file.\nWelcome to Python file handling.")
```

**Q2: Write a Python program to read the contents of a file.**

**Objective:**
Write a Python program to read the entire content of a file using the read() method.

**Background:**
The read() method reads all characters from a file and returns them as a single string. The file must be opened in 'r' (read) mode.

This problem helps beginners understand how to:
* Open a file for reading
* Use the read() method
* Display file content

Sample Program:

```
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

**Q3: Write a Python program to append text to an existing file.**

**Objective:**
Write a Python program to open an existing file and add new text at the end without erasing previous content.

**Background:**
The append mode 'a' allows you to add new data to a file without overwriting its existing content.

This problem helps beginners understand how to:
* Open a file in append mode
* Use the write() method to add data
* Preserve file content

Sample Program:

```
with open("example.txt", "a") as file:
    file.write("\nThis line is appended to the file.")
```

**Q4: Write a Python program to check if a file exists using Python.**

**Objective:**
Write a Python program to check whether a specific file exists in the system using os.path.exists().

**Background:**
The os.path.exists() function from the os module checks if a given path refers to an existing file or directory.

This problem helps beginners understand how to:
* Use the os module
* Check file availability before operations
* Avoid file-not-found errors

Sample Program:

```
import os

if os.path.exists("example.txt"):
    print("File exists.")
else:
    print("File does not exist.")
```

**Q5: Write a Python program to write multiple lines to a file using writelines().**

**Objective:**
Write a Python program to write a list of strings as separate lines to a file using the writelines() method.

**Background:**
The writelines() function writes a sequence of strings to a file. You must include newline characters (\n) explicitly if needed.

This problem helps beginners understand how to:
* Work with sequences and files
* Use writelines() effectively
* Write multiple lines at once

Sample Program:

```
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]

with open("example.txt", "w") as file:
    file.writelines(lines)
```

**Q6: Write a Python program to read the contents of a file line by line using readline().**

**Objective:**
Write a Python program to read a file line by line using the readline() method.

**Background:**
The readline() method reads one line at a time, which is useful for processing large files without loading everything into memory.

This problem helps beginners understand how to:
* Use readline() for line-by-line reading
* Implement loops for file reading
* Manage memory efficiently

Sample Program:

```
with open("example.txt", "r") as file:
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()
```

**Q7: Write a Python program to open a file in read mode ('r') and print the content.**

**Objective:**
Write a Python program to open a file using 'r' mode and print all its contents.

**Background:**
Reading a file in 'r' mode is the standard way to retrieve content from a file. This mode does not modify the file.

This problem helps beginners understand how to:
* Open and read files securely
* Use the read() method
* Display file data

Sample Program:

```
with open("example.txt", "r") as file:
    data = file.read()
    print(data)
```

**Q8: Write a Python program to demonstrate the use of seek() to move the file pointer.**

**Objective:**
Write a Python program to reposition the file pointer to a specific location using the seek() method and read from there.

**Background:**
The seek() method allows manual control over the file pointer, helping in re-reading or skipping parts of a file.

This problem helps beginners understand how to:
* Move file pointers with seek()
* Read from specific positions
* Control file reading flow

Sample Program:

```
with open("example.txt", "r") as file:
    file.seek(7)
    print("Content from position 7:", file.read())
```
