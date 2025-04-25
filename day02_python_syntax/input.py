## Write a Python program that asks for the user's name and prints it using a multi-line statement.
a=input("What is your name ? ")
print("Hello {} \n Welcome onboard. \n Let us know if you need any support.".format(a))
## Write a Python program that prints a multi-line string.
print("This will print \n multiple \n lines, \n the same \n will be visible \n on screen.")
## Write a Python program to use input() function to take two inputs from the user and print them.
a= input("Please provide two input sperated with space: ")
b=a.split()
for i in b:
    print(i)
