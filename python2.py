print(12)
print(23, 45, "jo")


#int and floats
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", str(hypo))

#strings
fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")





#2.4 Section 4 -Variables

keywords = ['False', 'None', 'True', 'and', 'as', 'assert', 
            'break', 'class', 'continue', 'def', 'del', 'elif', 
            'else', 'except', 'finally', 'for', 'from', 'global', 
            'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 
            'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 
            'yield']

            # HOW NOT TO WRITE: MyVariable, Adiós_Señora, sûr_la_mer, Einbahnstraße
            #
            # HOW NOT TO WRITE: 10t, !important, exchange rate 
            #
            #

var1 = 1
print(var1)

var2 = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var2, account_balance, client_name)
print(var2)






var3 = "3.8.5"
print("Python version: " + var3)






var4 = 1
print(var4)
var = var4 + 1
print(var4)






var5 = 100
var5 = 200 + 300
print(var5)






a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)






john = 3
mary = 5
adam = 6
total_apples = john + mary + adam
print(john, mary, adam)
print(total_apples)






kilometers = 12.25
miles = 7.38
miles_to_kilometers = kilometers * 1.60934
kilometers_to_miles = miles * 0.621371
print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")




#2.5 Section 5 – Comments
#2.5.1 Comments – why, when, and how?

# This program evaluates the hypotenuse c.
# a and b are the lengths of the legs.
a1 = 3.0
b1 = 4.0
c1= (a1 ** 2 + b1 ** 2) ** 0.5  # We use ** instead of a square root.
print("c1 =", c1)



#2.5.2 Marking fragments of code

# This is a test program.
x1 = 1
y1 = 2
# y1 = y1 + x1
print(x1 + y1)




#2.5.3   LAB   Comments

#Quizzes:

print(2//4)



x2 = input()
y2 = int(input())
print(x2 * y2)


z3 = y3 = x3 = 1
print(x, y, z, sep='*')


y4 = 2 + 3 * 5.
print(Y4)



x4 = 1 / 2 + 3 // 3 + 4 ** 2
print(x4)



x5 = int(input())
y5 = int(input())
print(x5 + y5)



x6 = int(input())
y6 = int(input())
x6 = x6 % y6
x6 = x6 % y6
y6 = y6 % x6
print(y6) #  11 and 4 ----> answer is 1



x7 = int(input())
y7 = int(input())
x7 = x7 / y7
y7 = y7 / x7
print(y7) # 2 and 4 answer is 8



x8 = 1
y8 = 2
z8 = x
x8 = y
y8 = z
print(x8, y8) # 2 1



