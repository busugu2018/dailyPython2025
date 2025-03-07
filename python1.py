print(123);
print("I like \"Monty Python\"");
print("I like 'Monty Python'");
print('I like \'Monty Python\'');
print('I like \"Monty Python\"');
print('I\'m Monty Python.');
print("I\'m Monty Python.");

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



