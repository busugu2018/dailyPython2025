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

print(2//4)

print(1//2*3)


n = int(input("Enter the number: "))
print("True")














#3.1.6   LAB   Variables ‒ Questions and answers




















while true:
    user_word = input("Enter a word: ")
    if user_word == user_word.upper():
        print