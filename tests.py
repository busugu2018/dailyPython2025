# def happy_new_year(wishes = True):
#     print("Three...")
#     print("Two...")
#     print("One...")
#     if not wishes:
#         return

#     print("Happy New Year!")
# happy_new_year()
# happy_new_year(False)



n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))
n3 = int(input("Enter n3: "))

largestNumber = n1

if n2 > largestNumber:
    largestNumber = n2

if n3 > largestNumber:
    largestNumber = n3
print("The largest number is: " + str(largestNumber))




