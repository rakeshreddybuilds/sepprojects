# Variables
  #  it is a name that points to a value stored in memory.
# so python is dynamically typed language. python figures out the type.
# we have four types mainly they are
# int for Whole numbers, float for decimal point numbers,
# strings for characters, and booleans for true or false
# complex for numbers with a real and imaginary part for example:- a + bj
# None for no value or nothing here.

# age = 19
# price = 22.33
# name = "Rakesh"
# is_animelover = True

# print(age)

# Operators +, -, *,/, //, %, **.
# / gives a float value and // gives a floor division.

# Problems:
# 1.Take a temperature in Celsius as input, convert and print it in Fahrenheit. Formula: F = C * 9/5 + 32
# temperature = int(input("Enter the temperature(Celsius): "))
# Fahrenheit = temperature * 9/5 + 32
# print(f"{Fahrenheit} degree F")
# two mistakes i have done here 
# 1.what happens if a person enters float values 
# 2. variable name F should in small case letters because only classes are reserved for capitalizedcase
# temperature = float(input("Enter the temperature(Celsius): "))
# fahrenheit = temperature * 9/5 + 32
# print(f"{fahrenheit} degree F")


# Strings and String methods 
# a string is a sequence of characters(', "", """)
# Indexing and Slicing
# p = "Monkey D. Luffy"
# print(p[0]) = M
# print(p[8]) = .
# print(p[-1]) = y
# p.strip()
# s = p.replace("Luffy", "Dragon")
# print(s)
# string methods .upper(), .lower(), 
# Note: string is immutable so you cant change a string until you create a new string to a existing one to replace it.

# Take a full name as input and print the initials (e.g., "Alex John Smith" → "A.J.S.").
# full_name = "Monkey Luffy"
# words = full_name.split()
# print(words)
# print(words[0][0])
# print(words[1][0])
# initials = f"{words[0][0]}.{words[1][0]}"
# print(initials)


# Conditionals(if, elif, else)
# Take a number as input and print whether it's positive, negative, or zero.
# number = int(input("Enter your number bro: "))
# if number > 0:
#   print("Your number is positive brother")
# elif number < 0:
#   print("Your number is negative brother")
# else:
#   print("Your number is zero")

