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





#=================================================================================

#Section 4.1.2: Decomposition










# =================================================================================

# 4.1.3 Where do the functions come from?

# Print is an integral part of python, we call them "built in function" 

# Modules are - useful functionsused less often that "built in function"  or "bif" 
# availble in modeules installed in py.

# You can write your own functions directly from your code and use them freely


# =================================================================================

# 4.1.4 Your first function

print("Enter a value: ")
a = int(input())

print("Enter a value: ")
b = int(input())

print("Enter a value: ")
c = int(input())




# Fixing it:

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








# 4.2 Section 2 – How functions communicate with their environment
# 4.2.1 Parameterized functions

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



#===============================================================
#4.3 Section 3 – Returning a result from a function  






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