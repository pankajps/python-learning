**Q1: Write a Python program to check if a number is positive, negative, or zero using if-elif-else.**

**Objective:**
Write a Python program to determine whether a given number is positive, negative, or zero.

**Background:**
Conditional statements like if, elif, and else help control the flow of logic based on conditions in Python.

This problem helps beginners understand how to:
* Use conditional statements
* Compare numerical values
* Implement multi-branch decisions

Sample Program:

```
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
```

**Q2: Write a Python program to check if a student is passing or failing based on their score.**

**Objective:**
Write a Python program that checks if a student has passed or failed based on a threshold score.

**Background:**
A pass/fail evaluation is a basic use-case for if-else. Typically, a score of 40 or more is considered passing.

This problem helps beginners understand how to:
* Use conditional logic
* Compare values with thresholds
* Provide decision-based output

Sample Program:

```
score = int(input("Enter the student's score: "))
if score >= 40:
    print("The student is passing.")
else:
    print("The student is failing.")
```

**Q3: Write a Python program to find the largest of three numbers using if-elif-else.**

**Objective:**
Write a Python program to identify the largest number among three user inputs.

**Background:**
Using if-elif-else, you can compare multiple values to determine the maximum.

This problem helps beginners understand how to:
* Use comparison operators
* Chain multiple if-elif conditions
* Solve multi-condition logic

Sample Program:

```
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("The largest number is:", a)
elif b >= a and b >= c:
    print("The largest number is:", b)
else:
    print("The largest number is:", c)
```

**Q4: Write a Python program to check if a number is divisible by both 2 and 3 using nested if statements.**

**Objective:**
Write a Python program to verify if a number is divisible by both 2 and 3 using nested conditionals.

**Background:**
Nested if statements allow checking multiple conditions in a hierarchical manner.

This problem helps beginners understand how to:
* Use nested conditionals
* Apply modulo % operator
* Check multiple divisibility conditions

Sample Program:

```
num = int(input("Enter a number: "))
if num % 2 == 0:
    if num % 3 == 0:
        print("The number is divisible by both 2 and 3.")
    else:
        print("The number is divisible by 2 but not by 3.")
else:
    print("The number is not divisible by 2.")
```

**Q5: Write a Python program to check if a year is a leap year using if-else.**

**Objective:**
Write a Python program to determine whether a given year is a leap year.

**Background:**
A leap year is divisible by 4, but not by 100 unless also divisible by 400.

This problem helps beginners understand how to:
* Use compound conditions
* Understand real-world logic rules
* Apply mathematical rules in code

Sample Program:

```
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
```

**Q6: Write a Python program to check if a person is eligible to vote based on their age.**

**Objective:**
Write a Python program to determine if a person can vote, typically based on a minimum age of 18.

**Background:**
Basic condition checks like age verification are common in real-world applications and policies.

This problem helps beginners understand how to:
* Compare numeric input values
* Use boolean conditions
* Write interactive user-driven programs

Sample Program:

```
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```

**Q7: Write a Python program to determine the grade of a student based on their marks using if-elif-else.**

**Objective:**
Write a Python program to classify student performance using grade ranges based on marks.

**Background:**
Grading systems often use conditional blocks to assign letter grades based on numeric scores.

This problem helps beginners understand how to:
* Use if-elif-else chains
* Apply multiple condition checks
* Output customized results

Sample Program:

```
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: F")
```

**Q8: Write a Python program that checks whether a person is eligible for a senior citizen discount using nested if.**

**Objective:**
Write a Python program to determine eligibility for a senior citizen discount based on age and citizenship.

**Background:**
Eligibility systems often rely on nested logic, where one condition depends on another (e.g., age and region).

This problem helps beginners understand how to:
* Use nested if statements
* Handle multiple eligibility criteria
* Apply logical filtering

Sample Program:

```
age = int(input("Enter age: "))
citizenship = input("Are you a citizen? (yes/no): ")

if age >= 60:
    if citizenship.lower() == "yes":
        print("Eligible for senior citizen discount.")
    else:
        print("Not eligible due to citizenship status.")
else:
    print("Not eligible due to age.")
```
