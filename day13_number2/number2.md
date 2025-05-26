**Q1: Write a Python program to print numbers from 1 to 5 using a while loop.**

**Objective:**
Write a Python program that uses a while loop to print numbers from 1 to 5.

**Background:**
The while loop executes a block of code repeatedly as long as a specified condition is true. It’s ideal for controlled repetition with dynamic conditions.

This problem helps beginners understand how to:
* Use while loops
* Manage loop variables
* Control iteration with conditions

Sample Program:

```
i = 1
while i <= 5:
    print(i)
    i += 1
```

**Q2: Write a Python program that uses a for loop to iterate over a string and print each character.**

**Objective:**
Write a Python program that prints each character in a string using a for loop.

**Background:**
Strings in Python are iterable sequences, and a for loop can be used to access each character one by one.

This problem helps beginners understand how to:
* Use for loops with sequences
* Iterate through strings
* Print characters individually

Sample Program:

```
text = "Python"
for char in text:
    print(char)
```

**Q3: Write a Python program that uses a while loop to sum numbers from 1 to 10.**

**Objective:**
Write a Python program to calculate the sum of numbers from 1 to 10 using a while loop.

**Background:**
Looping with a counter variable allows accumulating values in iterations, such as computing a sum.

This problem helps beginners understand how to:
* Use loop counters
* Add numbers cumulatively
* Combine loops with arithmetic

Sample Program:

```
i = 1
total = 0
while i <= 10:
    total += i
    i += 1
print("Sum from 1 to 10 is:", total)
```

**Q4: Write a Python program that demonstrates the use of nested if inside a for loop to check if numbers are both even and divisible by 5.**

**Objective:**
Write a Python program to iterate through numbers and print those that are both even and divisible by 5 using nested if statements.

**Background:**
Nested conditionals allow combining multiple checks. When used inside loops, they help filter values based on complex logic.

This problem helps beginners understand how to:
* Combine for loops with nested if statements
* Check multiple conditions
* Filter numbers based on rules

Sample Program:

```
for num in range(1, 51):
    if num % 2 == 0:
        if num % 5 == 0:
            print(num, "is even and divisible by 5")
```

**Q5: Write a Python program to calculate the factorial of a number using a while loop.**

**Objective:**
Write a Python program that calculates the factorial of a number using a while loop.

**Background:**
Factorial of a number n is the product of all positive integers less than or equal to n. It is often used in mathematics and recursion problems.

This problem helps beginners understand how to:
* Use loops for multiplication
* Apply decrementing logic
* Work with mathematical formulas

Sample Program:

```
n = int(input("Enter a number: "))
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print("Factorial of", n, "is", factorial)
```

**Q6: Write a Python program to print each character of a string using a for loop.**

**Objective:**
Write a Python program to iterate through each character of a string and print it using a for loop.

**Background:**
Strings are iterable in Python, making them compatible with for loops for element-wise access.

This problem helps beginners understand how to:
* Access elements in a string
* Use loop structures
* Format character-wise output

Sample Program:

```
text = "Looping"
for ch in text:
    print(ch)
```

**Q7: Write a Python program to find the largest number in a list using a for loop.**

**Objective:**
Write a Python program to find the maximum value in a list using a for loop.

**Background:**
Finding the maximum value involves iterating through a list and comparing elements sequentially.

This problem helps beginners understand how to:
* Traverse a list with loops
* Compare and update maximum values
* Use variables to track conditions
Sample Program:

```
numbers = [12, 45, 7, 89, 33]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print("The largest number is:", max_num)
```

**Q8: Write a Python program that uses nested if statements to check whether a number is positive, even, and divisible by 3.**

**Objective:**
Write a Python program to check if a number is positive, and then whether it is even and divisible by 3 using nested if statements.

**Background:**
Using nested logic helps verify multiple related conditions in a structured way.

This problem helps beginners understand how to:
* Use nested conditionals
* Apply logical combinations
* Validate numeric properties

Sample Program:

```
num = int(input("Enter a number: "))
if num > 0:
    if num % 2 == 0:
        if num % 3 == 0:
            print("Number is positive, even, and divisible by 3.")
        else:
            print("Number is positive and even but not divisible by 3.")
    else:
        print("Number is positive but not even.")
else:
    print("Number is not positive.")
```
