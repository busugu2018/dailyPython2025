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



