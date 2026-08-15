#Section 4.1.1: Why do we need functions?

# function is transforming a repeating part of a code into a function.

# We can now define the first condition which can help you decide when to
#  start writing your own functions: if a particular fragment of the code 
# begins to appear in more than one place, consider the possibility of 
# isolating it in the form of a function invoked from the points where 
# the original code was placed before.


# This considerably simplifies the work of the program, because each piece of 
# code can be encoded separately, and tested separately. The process described 
# here is often called decomposition.


# We can now state the second condition: if a piece of code becomes so large that 
# reading and understating it may cause a problem, consider dividing it into separate, 
# smaller problems, and implement each of them in the form of a separate function.


# This decomposition continues until you get a set of short functions, easy to
#  understand and test.








#Section 4.1.2: Decomposition














# 4.1.3 Where do the functions come from?

# Print is an integral part of python, we call them "built in function" 

# Modules are - useful functionsused less often that "built in function"  or "bif" 
# availble in modeules installed in py.

# You can write your own functions directly from your code and use them freely







# 4.1.4 Your first function

print("Enter a value: ")
a = int(input())

print("Enter a value: ")
b = int(input())

print("Enter a value: ")
c = int(input())




# Fixing it:
# def = define 
# message = function name

def message():
    print("Enter a value: ")



def message():
    print("Enter a value: ")

print("We start here.")
print("We end here.")




def message():
    print("Enter a value: ")

print("We start here.")
message()
print("We end here.")







# 4.1.5 How functions work

def message():
    print("Enter a value: ")

message()
a = int(input())
message()
b = int(input())
message()
c = int(input())







# 4.1.6 SECTION SUMMARY





#===============================================================

# 4.2 Section 2 – How functions communicate with their environment
# 4.2.1 Parameterized functions

# def = define 
# message = function name
# number = parameter.  -----> parameters are inputs the function receives
#                      -----> number is just a variable that exists inside the function

def message(number):
    print("Enter a number:", number)



#This looks better, for sure:
def message(number):
    print("Enter a number:", number)

message()




def message(number):
    print("Enter a number:", number)

number = 1234
message(1)
print(number)





def hello(name): # defining a function, function name hello, argument is name
    print("Hello,", name) # body of the function
 
 
name = input("Enter your name: ")
 
hello(name)  # calling the function








def message(what, number):
    print("Enter", what, "number", number)

message("telephone", 11)
message("price", 5)
message("number", "number")



# My own:
def message(what, name):
    print(what, name)
message("FirstName: ", "Brittani")
message("MiddleName: ", "Nicole")
message("LastName: ", "Hinson")




# 4.2.2 Positional parameter passing

def my_function(a, b, c):
    print(a, b, c)

my_function(1, 2, 3)


# My own
def my_function(a, b, c):
    print(a, b, c)

my_function("Name, ", "Age, ", "DOB.")







def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")




def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")



def message(what, number):
    print("Enter", what, "number", number)

message("telephone", 11)
message("price", 5)
message("Age", 35)






# 4.2.3 Keyword argument passing

def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")




def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction(surname="Skywalker", first_name="Luke") # It'll throw an error here - a non existing parameter "surname"





# 4.2.4 Mixing positional and keyword arguments

def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)
adding(1, 2, 3)
adding(c = 1, a = 2, b = 3)
adding(3, c = 1, b = 2)
adding(3, a = 1, b = 2) # error; a = 3 and a = 1, so a is twice. FALSE
adding(4, 3, c = 2)




# 4.2.5 Parametrized functions – more details

def introduction(first_name, last_name="Smith"):
     print("Hello, my name is", first_name, last_name)
introduction("James", "Doe")
introduction("Henry")
introduction(first_name="William")




def introduction(first_name="John", last_name="Smith"):
    print("Hello, my name is", first_name, last_name)
introduction()
introduction(last_name="Hopkins")









# 4.2.6 SECTION SUMMARY

def hi(name):
    print("Hi,", name)
hi("Greg")



def hi_all(name_1, name_2):
    print("Hi,", name_2)
    print("Hi,", name_1)
hi_all("Sebastian", "Konrad")



def address(street, city, postal_code):
    print("Your address is:", street, "St.,", city, postal_code)
s = input("Street: ")
p_c = input("Postal Code: ")
c = input("City: ")
address(s, c, p_c)



# Ex. 1
def subtra(a, b):
    print(a - b)
subtra(5, 2)    # outputs: 3
subtra(2, 5)    # outputs: -3


# Ex. 2
def subtra(a, b):
    print(a - b)
subtra(a=5, b=2)    # outputs: 3
subtra(b=2, a=5)    # outputs: 3

# Ex. 3
def subtra(a, b):
    print(a - b)
subtra(5, b=2)    # outputs: 3
subtra(5, 2)    # outputs: 3






def subtra(a, b):
    print(a - b)
subtra(5, b=2)    # outputs: 3
# subtra(a=5, 2)    # Syntax Error




def name(first_name, last_name="Smith"):
    print(first_name, last_name)

name("Andy")    # outputs: Andy Smith
name("Betty", "Johnson")    # outputs: Betty Johnson (the keyword argument replaced by "Johnson")





# 4.2.7 SECTION QUIZ

def intro(a="James Bond", b="Bond"):
    print("My name is", b + ".", a + ".")
intro()



def intro(a="James Bond", b="Bond"):
    print("My name is", b + ".", a + ".")
intro(b="Sean Connery")


def intro(a, b="Bond"):
    print("My name is", b + ".", a + ".")
intro("Susan")


# def add_numbers(a, b=2, c):
#     print(a + b + c)
# add_numbers(a=1, c=3)

# SyntaxError - a non-default argument (c) follows a default argument (b=2).







#===============================================================
# 4.3 Section 3 – Returning a result from a function  

# 4.3.1 Effects and results: the return instruction

def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return

    print("Happy New Year!")






def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return

    print("Happy New Year!")
happy_new_year()
happy_new_year(False)






def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return

    print("Happy New Year!")
happy_new_year()
happy_new_year()
happy_new_year(None)
happy_new_year()
happy_new_year(True)
happy_new_year()
happy_new_year()
happy_new_year(False)





def boring_function():
    print("'Boredom Mode' ON.")
    return 123

print("This lesson is interesting!")
boring_function()
print("This lesson is boring...")



# 4.3.2 A few words about None

print(None + 2) # TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

value = None
if value is None:
    print("Sorry, you don't carry any value")



def strange_function(n):
    if(n % 2 == 0):
        return True
print(strange_function(2))
print(strange_function(1))




def evenTest(num):
    if (num%2==0):
        return True
print(evenTest(6))
print(evenTest(2))
print(evenTest(5))
print(evenTest(9))
print(evenTest(8))









# 4.3.3 Effects and results: lists and functions

def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem # It means  ------->  s = s + elem

    return s

print(list_sum([5, 4, 3]))  # Your first call works: because [5, 4, 3] is a list.

# Step by step operation:

# Step 1:

# s = s + 5
# s = 0 + 5
# s = 5

# Step 2;

# s = s + 4
# s = 5 + 4
# s = 9

# Step 3:

# s = s + 3
# s = 9 + 3
# s = 12

# Final: s = 12



print(list_sum([0,7,-49,90])) # 0+0+7-49+90




print(list_sum(5))    # But this causes an error: because 5 is an integer, not a list.










def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))




# 4.3.4   LAB   A leap year: writing your own functions


















#===============================================================


# Quick OOP:

class travelTicket:
    def __init__(self, source, destination, date, price):
        self._source = source
        self._date = date
        self._price = price
        self._destination = destination

    def get_source(self):
        return self._source
    
    def set_source(self, source):
        self._source = source

    def get_destination(self):
        return self._destination
    
    def set_destination(self, destination):
        self._destination = destination

    def get_date(self):
        return self._date
    
    def set_date(self, date):
        self._date = date

    def get_price(self):
        return self._price
    
    def set_price(self, price):
        self._price = price

# Creting an object
ticket1 = travelTicket("NY", "Saigon", "2024-05-15", 1100)

# Access the current values
print("Origin: ", ticket1.get_source())
print("Destination: ", ticket1.get_destination())
print("Date: ", ticket1.get_date())
print("Price: ", ticket1.get_price())

#Edit our encapsulated attributes using out setter methods
ticket1.set_price(800)
ticket1.set_destintion("Hong Kong")

# Access updated values
print("Modified destinatiom: ", ticket1.get_destintion())
print("Modified price: ", ticket1.get_price())











# ==============================================================================
#https://www.youtube.com/watch?v=rLyYb7BFgQI


class Microwave: 
    def __init__(self, brand: str, power_rating: str) -> None:
        self.brand = brand
        self.power_rating = power_rating

smeg: Microwave = Microwave(brand='Smeg', power_rating='B')
print(smeg)
print(smeg.brand)
print(smeg.power_rating)

bosh: Microwave = Microwave(brand='Bosh', power_rating='C')
print(bosh)
print(bosh.brand)
print(bosh.power_rating)

# ==============================================================================

class Microwave: 
    def __init__(self, brand: str, power_rating: str) -> None:
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on: bool = False

    def tun_on(self) -> None:
        if self.turned_on: 
            print(f'Microwave ({self.brand}) is already turned on.')
        else:
            self.turned_on = True
            print(f'Microwave ({self.brand}) is now turned on.')

    # def turn_off(self) -> None:
    #     if self.turned_on: 
    #         self.turned_on = False
    #         print(f'Microwave ({self.brand}) is now turned on.')
    #     else:
    #         # self.turned_on = True
    #         print(f'Microwave ({self.brand}) is already turned off.')

    def turn_off(self) -> None:
        if self.turned_on:
            self.turned_on = False
            print(f'Microwave ({self.brand}) is now turned off.')
        else:
            print(f'Microwave ({self.brand}) is already turned off.')

    def run(self, seconds: int) -> None:
        if self.turned_on:
            print(f'Running ({self.brand}) for {seconds} seconds')
        else:
            print(f'A mystical force whispers: "Turn on your Microwave first.')

smeg: Microwave = Microwave(brand='Smeg', power_rating='B')
smeg.tun_on()
smeg.run(30)
smeg.turn_off()
smeg.run(10)




# print(smeg)
# print(smeg.brand)
# print(smeg.power_rating)

# bosh: Microwave = Microwave(brand='Bosh', power_rating='C')
# print(bosh)
# print(bosh.brand)
# print(bosh.power_rating)
