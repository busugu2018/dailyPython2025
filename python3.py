#3.1 Boolean values, Conditional execution, loops, lists and 
# list processing, logical bitwise operations

weather = 'bad';
if (weather == 'good'):
    print("Le's go walk.")
else:
    print("Let's just stay home and watch a movie.")







weather1 = int(input("What temperature is it?: "))
if (weather1 >= 75):
    print("The weather is " + str(weather1) + ", go enjoy the sun.")
elif ((weather1 < 75) and (weather1 > 60)):
    print("The weather is " + str(weather1) + ", I'll stay home.")
else:
    print("It's freezing, I'll stay my a** home.")








#The if-elif-else statement, e.g.:
x = 10
 
if x == 10: # True
    print("x == 10")
 
if x > 15: # False
    print("x > 15")
 
elif x > 10: # False
    print("x > 10")
 
elif x > 5: # True
    print("x > 5")
 
else:
    print("else will not be executed")



x = '1'
print(int(x))




number = 4
print("Even" if number%2 == 0 else "Odd")



#3.1.6   LAB   Variables ‒ Questions and answers

#Nested if-else statements
if the_weather_is_good:
    if nice_restaurant_is_found:
        have_lunch()
    else:
        eat_a_sandwich()
else:
    if tickets_are_available:
        go_to_the_theater()
    else:
        go_shopping()

#More Nested if-else...





#Elif Statement
if the_weather_is_good:
    go_for_a_walk()
elif tickets_are_available:
    go_to_the_theater()
elif table_is_available:
    go_for_lunch()
else:
    play_chess_at_home()



#3.1.8 Analyzing code samples

# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
 
# Choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2
 
# Print the result
print("The larger number is:", larger_number)



# ==============================================================# ==============================================================




#A sales company is making a sales performance analysis to determine who are the Top-performing sales representatives
#on a specific team. Who are the top 3 salesmen out of the 20

table_data = [
        {"Name": "Alice", "Age": 30, "City": "New York", "salesRevenue": 5000},
        {"Name": "Bob", "Age": 25, "City": "Los Angeles", "salesRevenue": 24000},
        {"Name": "Boldan", "Age": 30, "City": "Dallas", "salesRevenue": 22378},
        {"Name": "Charlie", "Age": 31, "City": "Chicago", "salesRevenue": 6000},
        {"Name": "Matt", "Age": 25, "City": "Joburg", "salesRevenue": 8000},
        {"Name": "Hank", "Age": 19, "City": "Libreville", "salesRevenue": 20385},
        {"Name": "Charles", "Age": 45, "City": "Dallas", "salesRevenue": 19000},
        {"Name": "Carl", "Age": 55, "City": "Houston", "salesRevenue": 5500},
        {"Name": "Martin", "Age": 65, "City": "Rohd-Island", "salesRevenue": 8790},
        {"Name": "Manning", "Age": 33, "City": "Lubbock", "salesRevenue": 17890},
        {"Name": "Brock", "Age": 38, "City": "Tchibanga", "salesRevenue": 7458},
        {"Name": "Bell", "Age": 23, "City": "Mayes", "salesRevenue": 18988},
        {"Name": "Dexter", "Age": 29, "City": "Poryland", "salesRevenue": 24889},
        {"Name": "Ronald", "Age": 20, "City": "Portland", "salesRevenue": 9058},
        {"Name": "Sho", "Age": 38, "City": "Minneapolis", "salesRevenue": 6890},
        {"Name": "Kojo", "Age": 25, "City": "Chicago", "salesRevenue": 12394},
        {"Name": "Dewango", "Age": 35, "City": "Houston", "salesRevenue": 15678},
        {"Name": "Welembi", "Age": 25, "City": "Austin", "salesRevenue": 23654},
        {"Name": "Epeka", "Age": 27, "City": "Chicago", "salesRevenue": 22928},
        {"Name": "Nzali", "Age": 37, "City": "Plano", "salesRevenue": 7495},
        {"Name": "Vanelevan", "Age": 31, "City": "New York", "salesRevenue": 10293},
        {"Name": "Uwarriss", "Age": 46, "City": "New Jersey", "salesRevenue": 11345},
        {"Name": "Tchibinda", "Age": 18, "City": "Louisiana", "salesRevenue": 9857},
        {"Name": "Mbadinga", "Age": 45, "City": "Chicago", "salesRevenue": 9485}
    ]
for row in table_data:
    print(row["salesRevenue"])



#Learn pandas package from Python
# import random
# import pandas as pd

# # Sample names and cities
# names = ["John Smith", "Jane Doe", "Michael Johnson", "Emily Davis", "Chris Brown", "Jessica Wilson", "David Martinez", "Ashley Anderson", "James Thomas", "Sarah White",
#          "Brian Harris", "Olivia Martin", "Daniel Lewis", "Sophia Lee", "Matthew Walker", "Emma Hall", "Ethan Young", "Isabella King", "Alexander Scott", "Mia Adams"]

# cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
#           "Austin", "Jacksonville", "San Francisco", "Columbus", "Indianapolis", "Fort Worth", "Charlotte", "Seattle", "Denver", "Washington"]

# # Generate random sales revenue between 5000 and 25000
# sales_revenue = [random.randint(5000, 25000) for _ in range(20)]

# # Create a DataFrame
# data = {
#     "Name": names,
#     "City": cities,
#     "Sales Revenue": sales_revenue
# }

# df = pd.DataFrame(data)

# # Display the table
# print(df)

# ==============================================================# ==============================================================

# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
 
# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1
 
# We check if the second number is larger than the current largest_number
# and update the largest_number if needed.
if number2 > largest_number:
    largest_number = number2
 
# We check if the third number is larger than the current largest_number
# and update the largest_number if needed.
if number3 > largest_number:
    largest_number = number3
 
# Print the result
print("The largest number is:", largest_number)







n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))
n3 = int(input("Enter n3: "))

largestNumber = n1

if n2 > n1:
    largestNumber = n2;
if n3 > n2:
    largestNumber = n3;
print("The largest number is: " + str(largestNumber))



# ==============================================================# ==============================================================

#3.1.9 Pseudocode and introduction to loops


largest_number = -999999999
number = int(input())
if number == -1:
    print(largest_number)
    exit()
if number > largest_number:
    largest_number = number
# Go to line 02





# ==============================================================# ==============================================================

#3.1.10   LAB   Comparison operators and conditional execution

# n1 = input("Enter input: ")
# if n1 == "spathiphyllum":
#     print("No, I want a big Spathiphyllum!")
# n2 = input("Enter input: ")
# if n2 == "pelargonium":
#     print("Spathiphyllum! Not pelargonium!")
# n3 = input("Enter input: ")
# if n3 == "Spathiphyllum":
#     print("Yes - Spathiphyllum is the best plant ever!")




#Actual Answer
name = input("Enter flower name: ")
if name == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif name == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not", name + "!")
















# ==============================================================# ==============================================================
#3.2.2 An infinite loop
# while True:
#     print("I'm stuck inside a loop.")





#3.2.2 An infinite loop
#That example is confusing
# Store the current largest number here.
largest_number = -999999999
 
# Input the first value.
number = int(input("Enter a number or type -1 to stop: "))
 
# If the number is not equal to -1, continue.
while number != -1:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))
 
# Print the largest number.
print("The largest number is:", largest_number)




largest_number = -999999999
number = int(input("Enter a number or type -1 to stop: "))
while number != -1:
    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to stop: "))
print("The largest number is:", largest_number)


#smallest Number
smallest_number = 999999999
number = int(input("Enter a number or type 1 to stop: "))
while number != 1:
    if number < smallest_number:
        smallest_number = number
    number = int(input("Enter a number or type 1 to stop: "))
print("The smallest number is: ", smallest_number)












# ==============================================================# ==============================================================


#3.2.3 The while loop: more examples


# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.
 
odd_numbers = 0
even_numbers = 0
 
# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))
 
# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))
 
# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)




#Better version
oddNumbers = 0 
evenNumbers = 0 
number = int(input("Enter a number or type 0 to stop: "))

while number != 0:
    if number % 2 == 1:
        oddNumbers += 1
    else:
        evenNumbers += 1
    number = int(input("Enter a number or type 0 to stop: "))
print("Odd numbers count:", oddNumbers)
print("Even numbers count:", evenNumbers)



#counter:
counter = 5
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)





#3.2.5 Looping your code with for
#counter:
for i in range(10):
    print("The value of i is currently", i)

for i in range(50):
    print("The value of i is currently", i)


for i in range(2, 8):
    print("The value of i is currently", i)

for counter in range(2, 12):
    print("Inside the loop.", counter)

for counter in range(2, 8):
    print("Inside the loop.", counter)


# ==============================================================# ==============================================================


#3.2.8 The break and continue statements

# break - example
print("The break instruction: ")
for i in range(1, 16):
    if i == 13:
        break
    print("Inside the loop. ", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction: ")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop. ", i)
print("Outside the loop. ")



















# ==============================================================# ==============================================================

#3.2.10   LAB   The continue statement – the Ugly Vowel Eater


























# ==============================================================# ==============================================================


























# ==============================================================# ==============================================================

#3.3.2 Logical expressions





















# ==============================================================# ==============================================================
#3.3.3 Logical values vs. single bits#

i = 1
j = not not i
print(j)


























# ==============================================================# ==============================================================
#3.3.4 Bitwise operators



i	            #00000000000000000000000000001111
j	            #00000000000000000000000000010110
bit = i & j	    #00000000000000000000000000000110
bit = i | j     #000000000000000000000000000
~i
~j









# Operators in Python are special symbols or keywords used to perform operations on operands (values or variables). They enable various functionalities, from basic arithmetic to complex logical comparisons and data manipulation. Here's an overview of common Python operators:
# Arithmetic Operators:


# Used for mathematical calculations.
# +: Addition (e.g., x + y)
# -: Subtraction (e.g., x - y)
# *: Multiplication (e.g., x * y)
# /: Division (e.g., x / y)


# %: Modulus (remainder of division, e.g., x % y)
# **: Exponentiation (e.g., x ** y)
# //: Floor division (division that rounds down to the nearest integer, e.g., x // y)
# Assignment Operators:
# Used to assign values to variables.
# =: Assign (e.g., x = 5)
# +=: Add and assign (e.g., x += 3 is equivalent to x = x + 3)
# -=: Subtract and assign (e.g., x -= 3 is equivalent to x = x - 3)
# *=, /=, %=, **=, //= : Similar to += and -=, but for other arithmetic operations.
# Comparison Operators:
# Used to compare two values.
# ==: Equal to (e.g., x == y)
# !=: Not equal to (e.g., x != y)
# >: Greater than (e.g., x > y)
# <: Less than (e.g., x < y)
# >=: Greater than or equal to (e.g., x >= y)
# <=: Less than or equal to (e.g., x <= y)
# Logical Operators:
# Used to combine conditional statements.
# and: Returns True if both operands are True
# or: Returns True if at least one operand is True
# not: Returns True if the operand is False, and vice versa
# Bitwise Operators:
# Used to perform operations on individual bits of data.
# &: AND
# |: OR
# ^: XOR
# ~: NOT
# <<: Left shift
# >>: Right shift
# Membership Operators:
# Used to test if a sequence is present in an object.
# in: Returns True if a sequence is found in the object
# not in: Returns True if a sequence is not found in the object
# Identity Operators:
# Used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.
# is: Returns True if both variables are the same object
# is not: Returns True if both variables are not the same object
# It's important to understand operator precedence, which determines the order in which operations are performed. Parentheses can be used to override the default precedence.
# Introduction to Python. What is Python Programming Language? | by ...
# We cannot use a keyword as a variable name, function name or any other identifier. They are used to define the syntax and structur...







# ==============================================================# ==============================================================

























# ==============================================================# ==============================================================
#3.3.6 Binary left shift and binary right shift

var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)

# Note:

# 17 >> 1 → 17 // 2 (17 floor-divided by 2 to the power of 1) → 8 
# (shifting to the right by one bit is the same as integer division by two)

# 17 << 2 → 17 * 4 (17 multiplied by 2 to the power of 2) → 68 
# (shifting to the left by two bits is the same as integer multiplication
#  by four)





# Priority	Operator	
# 1	        ~, +, -	unary
# 2	        **	
# 3	        *, /, //, %	
# 4	        +, -	binary
# 5	        <<, >>	
# 6	        <, <=, >, >=	
# 7	        ==, !=	
# 8	        &	
# 9	        |	
# 10	    =, +=, -=, *=, /=, %=, &=, ^=, |=, >>=, <<=	






# ==============================================================# ==============================================================
# 3.3.7 SECTION SUMMARY
# 1. Python supports the following logical operators:

# and → if both operands are true, the condition is true, e.g., (True and True) is True,
# or → if any of the operands are true, the condition is true, e.g., (True or False) is True,
# not → returns false if the result is true, and returns true if the result is false, e.g., not True is False.
# 2. You can use bitwise operators to manipulate single bits of data. The following sample data:

# x = 15, which is 0000 1111 in binary,
# y = 16, which is 0001 0000 in binary.
# will be used to illustrate the meaning of bitwise operators in Python. Analyze the examples below:

# & does a bitwise and, e.g., x & y = 0, which is 0000 0000 in binary,
# | does a bitwise or, e.g., x | y = 31, which is 0001 1111 in binary,
# ˜  does a bitwise not, e.g., ˜ x = 240*, which is 1111 0000 in binary,
# ^ does a bitwise xor, e.g., x ^ y = 31, which is 0001 1111 in binary,
# >> does a bitwise right shift, e.g., y >> 1 = 8, which is 0000 1000 in binary,
# << does a bitwise left shift, e.g., y << 3 = 128, which is 1000 0000 in binary.
# * -16 (decimal from signed 2's complement) -- read more about the Two's complement operation.
























# ==============================================================# ==============================================================
#3.3.8 SECTION QUIZ

x = 1
y = 0
 
z = ((x == y) and (x == y)) or not(x == y)
print(not(z))






x = 4
y = 1
 
a = x & y
b = x | y
c = ~x  # tricky!
d = x ^ 5
e = x >> 2
f = x << 2
 
print(a, b, c, d, e, f)







# ==============================================================# ==============================================================
#3.4 Section 4 – Lists
#3.4.1 Why do we need lists?
lst = [1, [2, 3], 4]
print(lst[1]) #---> [2, 3]
print(len(lst)) #---> 3





#3.4.2 Indexing lists

numbers = [10, 5, 7, 2, 1]
print("Original list contents:", numbers)  # Printing original list contents.
 
numbers[0] = 111
numbers[3] = 67
numbers[4] = 12
print("New list contents: ", numbers) 

#3.4.3 Accessing list content
print("\nList length:", len(numbers)) 


#3.4.4 Removing elements from a list
del numbers[1]
print(len(numbers))
print(numbers)

print(numbers[4]) #------> Error message cause the 
                #list went from [111, 5, 7, 67, 12] to [111, 7, 67, 12]
numbers[4] = 1


#3.4.5 Negative indices are legal
numbers = [111, 7, 2, 1]
print(numbers[-1])
print(numbers[-2])
print(numbers[-3])
print(numbers[-4])
print(numbers[-5]) #-----> doesnt exist


#3.4.6   LAB   The basics of lists

hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in  
                            #the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.

hat_list[2] = int(input("Enter number: "))
print("New list is " + str(hat_list))

# Step 2: write a line of code that removes the last element from the list.
del hat_list[-1]



# Step 3: write a line of code that prints the length of the existing list.
print(len(hat_list))
print(hat_list)














# ==============================================================# ==============================================================

#3.4.7 Functions vs. methods

# A method is a specific kind of function ‒ it behaves like a function and looks like a function, but differs in the way in which it acts, and in its invocation style.

# A function doesn't belong to any data ‒ it gets data, it may create new data and it (generally) produces a result.

# A method does all these things, but is also able to change the state of a selected entity.

# A method is owned by the data it works for, while a function is owned by the whole code.

# This also means that invoking a method requires some specification of the data from which the method is invoked.

# It may sound puzzling here, but we'll deal with it in depth when we delve into object-oriented programming.






#3.4.8 Adding elements to a list: append() and insert()

numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)
print(len(numbers))
print(numbers)

numbers.append(10)
print(len(numbers))
print(numbers)

numbers.append(7689)
print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

numbers.insert(7, 0)
print(len(numbers))
print(numbers)








#I'm confused here
my_list = []  # Creating an empty list.
for i in range(5):
    my_list.append(i + 1)
print(my_list)


my_list = []  # Creating an empty list. 
for i in range(5):
    my_list.insert(0, i + 1) 
print(my_list)





# ==============================================================# ==============================================================

#3.4.9 Making use of lists
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)




my_list = [10, 1, 8, 3, 5]
total = 0
for i in range(len(my_list)):
    total += my_list[i]
print(total)




my_list = [10, 1, 8, 3, 5]
total = 10
for i in range(len(my_list)):
    total += my_list[i]
print(total)




my_list = [10, 1, 8, 3, 5]
total = 20
for i in range(len(my_list)):
    total += my_list[i]
print(total)












# ==============================================================# ==============================================================


# 3.4.10 Lists in action

variable_1 = 1
variable_2 = 2
 
variable_2 = variable_1
variable_1 = variable_2



my_list = [10, 1, 8, 3, 5]
 
my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]
 
print(my_list)
 



my_list = [5, 3, 8, 1, 10]
for i in range(len(my_list) // 2):
    my_list[i], my_list[len(my_list) - i - 1] = my_list[len(my_list) - i - 1], my_list[i]
print(my_list)








# ==============================================================# ==============================================================




# ==============================================================# ==============================================================


squares = [x ** 2 for x in range(10)]

squares2 = []

for i in range(10):
    i = i**2
    squares2.append(i)
    print(i)
    print(squares2)
print(squares2)




squares = [x ** 2 for x in range(10)]

squares2 = []

for i in range(10):
    i = i**2
    squares2.append(i)
    print(i)
    print(squares2)
print(squares2)

odds = [x for x in squares if x % 2 != 0 ]
print(odds)

even = []
for x in squares:
    if x % 2 == 0:
        even.append(x)
print(even)









squares = [x ** 2 for x in range(10), [1, 1, 1]] #-------> Can't do that

squares2 = []

for i in range(10):
    i = i**2
    squares2.append(i)
    print(i)
    print(squares2)
print(squares2)

odds = [x for x in squares if x % 2 != 0 ]
print(odds)

even = []
for x in squares:
    if x % 2 == 0:
        even.append(x)
print(even)



board = []
 
for x in range(4):
    row = [i for i in range(4)]
    board.append(row)
    print(board)
print(board)






# ==============================================================# ==============================================================

























# ==============================================================# ==============================================================

























# ==============================================================# ==============================================================

# ==============================================================# ==============================================================

























# ==============================================================# ==============================================================

# ==============================================================# ==============================================================

























# ==============================================================# ==============================================================

# ==============================================================# ==============================================================

























# ==============================================================# ==============================================================

# ==============================================================# ==============================================================

























# ==============================================================# ==============================================================

# ==============================================================# ==============================================================

























# ==============================================================# ==============================================================

# ==============================================================# ==============================================================

























# ==============================================================# ==============================================================

# ==============================================================# ==============================================================

























# ==============================================================# ==============================================================

# ==============================================================# ==============================================================

























# ==============================================================# ==============================================================

# ==============================================================# ==============================================================

























# ==============================================================# ==============================================================























while true:
    user_word = input("Enter a word: ")
    if user_word == user_word.upper():
        print