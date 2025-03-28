#1.1.5  Importing a module: continued
import math
print(math.sin(math.pi/2))



#===============================================
import math
def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

pi = 3.14

print(sin(pi/2))
print(math.sin(math.pi/2))


# What Happens?
# Custom sin(x) Function:

# You define a function sin(x) that checks if 2 * x == pi. If true, it returns 0.99999999, otherwise, it returns None.

# Note: This function does not actually compute the sine function.

# Variable pi = 3.14:

# You redefine pi as 3.14, which is not exactly equal to math.pi (3.141592653589793).

# Calling sin(pi/2):

# pi / 2 is 3.14 / 2 = 1.57.

# 2 * 1.57 equals 3.14, which matches your condition (2 * x == pi).

# So, sin(1.57) returns 0.99999999.

# Calling math.sin(math.pi/2):

# math.pi / 2 is 1.57079632679.

# math.sin(math.pi/2) correctly computes the sine of 90 degrees.

# This returns 1.0.

pi = 3.14


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


print(sin(pi / 2))

from math import sin, pi

print(sin(pi / 2))


#===============================================


from math import sin, pi

print(sin(pi/2))















#===============================================
#1.1.6 Importing a module: *
from module import *   #Such an instruction imports all entities from the indicated module.




#===============================================
#1.1.7 The as keyword

import module as alias


#===============================================
#1.1.8 Aliasing
import math as m
    
print(m.sin(m.pi/2))


#===

from math import pi as PI, sin as sine
  
print(sine(PI/2))


#===

from module import n as a, m as b, o as c
  


#===============================================
#1.2.1 Working with standard modules
#you can run the following code to print the names of all entities within the math module:

import math

for name in dir(math):
  print(name, end="∖t")

#===============================================

import math
dir(math)



#===============================================
#1.2.2 Selected functions from the math module

from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)

#===

from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))


#===

from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))

#===============================================
#1.2.3 Is there real randomness in computers?
#Another module worth mentioning is the one named random.




#1.2.4 Selected functions from the random module
from random import random

for i in range(5):
    print(random())


#===

from random import random, seed

seed(0)

for i in range(5):
    print(random())


#===

from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))

#===

from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))


#===============================================
#1.2.5 How to know where you are?

print("       /\\")
print("      /  \\")
print("     / My \\")
print("    / Code \\")
print("   /________\\")
print("  /    py    \\")
print(" /    thon    \\")
print("/______________\\")
print("/               \\")
print("/     os         \\")
print("/                 \\")
print("/__________________\\")
print("/                   \\")
print("/     hard           \\")
print("/     ware            \\")
print("/                      \\")
print("/__________________     \\")


# This means than some of your 
# (or rather your program's) 
# actions have to travel a long 
# way to be successfully performed 
# - imagine that:

# Your code wants to create a file, 
# so it invokes one of Python's functions;


# Python accepts the order, 
# rearranges it to meet local OS requirements 
# (it's like putting the stamp "approved" on 
# your request) and sends it down (this may 
# remind you of a chain of command)


# The OS checks if the request is 
# reasonable and valid (e.g., whether 
# the file name conforms to some syntax rules)
#  and tries to create the file; such an operation,
#  seemingly very simple, isn't atomic - it 
# consists of many minor steps taken by...



# The hardware, which is responsible 
# for activating storage devices 
# (hard disk, solid state devices, etc.) 
# to satisfy the OS's needs.



#===============================================
















#===============================================


















#===============================================

















#===============================================


















#===============================================
















#===============================================


















#===============================================






