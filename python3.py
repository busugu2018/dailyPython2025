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






























































print(2//4)

print(1//2*3)


n = int(input("Enter the number: "))
print("True")

































while true:
    user_word = input("Enter a word: ")
    if user_word == user_word.upper():
        print