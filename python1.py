#2.1 - Hello, World!
print("Hello, World!")









#2.1.8
#     \n   as a 
print("The itsy bitsy spider\nclimbed up the waterspout.")
print()
print("Down came the rain\nand washed the spider out.")


#2.1.9 Multiple arguments

print("The itsy bitsy spider" , "climbed up" , "the waterspout.")


#2.1.10 Positional arguments
print("My name is", "Python.")
print("Monty Python.")


#2.1.11 Keyword arguments
print("My name is", "Python.", end=" ")
print("Monty Python.")


print("My", "name", "is", "Monty", "Python.", sep="-")
# Answer: My-name-is-Monty-Python.



print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
#My_name_is*Monty*Python.*


print("Programming","Essentials","in: ")
print("Python")


#2.1.13 LAB 
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")


#2.1.15
print('Greg\'s book.')
print("'Greg's book.'")
print('"Greg\'s book."')
print("Greg\'s book.")





#2.2 - Literals
#2.2.1 Literals – the data in itself
print("2")
print(2)

#2.2.2 Integers
print(111111111111)



#Octal and hexadecimal numbers
print(0o123)




#2.2.3 Floats




#2.2.4 Strings

print("I like \"Monty Python\"");
print("I like 'Monty Python'");
print('I like \'Monty Python\'');
print('I like \"Monty Python\"');
print('I\'m Monty Python.');
print("I\'m Monty Python.");



#2.2.5 Boolean values
print(True > False)
print(True < False)



#2.2.6   LAB   Python literals - strings

print("I'm", "\"Learning\"", "\"\"Python\"\"")

print("\"I'm\"")
print("\"\"Learning\"\"")
print("\"\"\"Python\"\"\"")




#2.3: Operators - data manipulation tools 
#2.3.1: python as a calculator:
print(2+2);



#2.3.2 Basic operators

#exponential
print(2 ** 3); 
print(2 ** 3.);
print(2. ** 3);
print(2. ** 3.);


#multiplication
print(2 * 3); 
print(2 * 3.);
print(2. * 3);
print(2. * 3.);

#Division
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)

#Integer division (floor division) jhfy
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

print(6 // 4)
print(6. // 4)

print(-6 // 4)
print(6. // -4)

#Remainder (modulo)
print(14 % 4)




#2.3.3 Operators and their priorities

#Operators and their bindings
print(9 % 6 % 2);

print(2 ** 2 ** 3);

print(-3 ** 2);
print(-2 ** 3);
print(-(3 ** 2));

#List of priorities
print(2 * 3 % 5);

#Operators and parentheses
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

print(6. // -4)

print(2**4)
print(2*4.)
print(2//4)
print(-2//4) #math.floor


#2.4.1 Variables – data-shaped boxes












#2.4.2 Variable names

# If you want to give a name to a variable, you must follow some strict rules:

# the name of the variable must be composed of upper-case or lower-case letters, digits, and the character _ (underscore)
# the name of the variable must begin with a letter;
# the underscore character is a letter;
# upper- and lower-case letters are treated as different (a little differently than in the real world – Alice and ALICE are the same first names, but in Python they are two different variable names, and consequently, two different variables);
# the name of the variable must not be any of Python's reserved words (the keywords – we'll explain more about this soon).


# Here are some correct, but not always convenient variable names:

# MyVariable
# i
# l
# t34
# Exchange_Rate
# counter
# days_to_christmas
# TheNameIsTooLongAndHardlyReadable
# _


# These variable names are also correct:

# Adiós_Señora
# sûr_la_mer
# Einbahnstraße
# переменная




# And now for some incorrect names:

# 10t (does not begin with a letter)
# !important (does not begin with a letter)
# exchange rate (contains a space)






#2.4.3 How to create a variable

var = 1
print(var)


#2.4.4 How to use a variable
var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var)


#2.4.5  How to assign a new value to an already 
# existing variable

var = 1
print(var)
var = var + 1
print(var)


var = 100
var = 200 + 300
print(var)



#2.4.6 Solving simple mathematical problems
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)



#2.4.7   LAB   Variables



# Here is a short story:

# Once upon a time in Appleland, John had three apples, Mary had five apples, and Adam had six apples. They were all very happy and lived for a long time. End of story.

# Your task is to:

# create the variables: john, mary, and adam;
# assign values to the variables. The values must be equal to the numbers of fruit possessed by John, Mary, and Adam respectively;
# having stored the numbers in the variables, print the variables on one line, and separate each of them with a comma;
# now create a new variable named total_apples equal to the addition of the three previous variables.
# print the value stored in total_apples to the console;
# experiment with your code: create new variables, assign different values to them, and perform various arithmetic operations on them (e.g., +, -, *, /, //, etc.). Try to print a string and an integer together on one line, e.g., "Total number of apples:" and total_apples.

John = 3
Mary = 5
Adam = 6
print(John, Mary, Adam, sep=',')
totalApples = John + Mary + Adam
print(totalApples)











#2.4.8 Shortcut operators













# 2.4.9   LAB   Variables ‒ a simple converter


# Scenario

# Miles and kilometers are units of length or distance.

# Bearing in mind that 1 mile is equal to approximately 1.61 kilometers, complete the program in the editor so that it converts:

# miles to kilometers;
# kilometers to miles.
# Do not change anything in the existing code. Write your code in the places indicated by ###. Test your program with the data we've provided in the source code.

# Pay particular attention to what is going on inside the print() function. Analyze how we provide multiple arguments to the function, and how we output the expected data.

# Note that some of the arguments inside the print() function are strings (e.g., "miles is", whereas some other are variables (e.g., miles).

#   Tip  
# There's one more interesting thing happening there. Can you see another function inside the print() function? It's the round() function. Its job is to round the outputted result to the number of decimal places specified in the parentheses, and return a float (inside the round() function you can find the variable name, a comma, and the number of decimal places we're aiming for). We're going to talk about functions very soon, so don't worry that everything may not be fully clear yet. We just want to spark your curiosity.

# After completing the lab, open the Sandbox, and experiment some more. Try to write different converters, e.g., a USD to EUR converter, a temperature converter, etc. ‒ let your imagination fly! Try to output the results by combining strings and variables. Try to use and experiment with the round() function to round your results to one, two, or three decimal places. Check out what happens if you don't provide any number of digits. Remember to test your programs.

# Experiment, draw conclusions, and learn. Be curious.














#2.6.3 The result of the input() function


name = input("What's your name?: ")
age = input("How old are you?: ")
print("My name is " + name + ", I am " + age + " years old.")



# #2.6.4 The input() function – prohibited operations
# # Testing a TypeError message.
# anything = input("Enter a number: ")
# something = anything ** 2.0
# print(anything, "to the power of 2 is", something)

#correction
anything = int(input("Enter a number: "));
something = anything ** 2.0;
print(anything, "to the power of 2 is", str(something));

# ///////////////////
# using string within print...
age1 = int(input("How old are you again?: "))
new_age = age1+1
print("I am actually " + str(new_age) + " years old.")



#Fixing Input issue on Sublime text
#Sublime Text-->TOOLS-->bUILD sYSTEM-->nEW bUILD-->Paste it.

# anything = float(input("Enter a number: "))
# something = anything ** float(2.0)
# print(anything, "to the power of 2 is", something)


#correction
anything = float(input("Enter a number: "))
something = anything ** float(2.0)
print(anything, "to the power of 2 is", something)









































#{
#     "target": "run_existing_window_command", 
#     "id": "repl_python_run",
#     "file": "config/Python/Main.sublime-menu"
# }



