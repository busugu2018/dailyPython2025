# def happy_new_year(wishes = True):
#     print("Three...")
#     print("Two...")
#     print("One...")
#     if not wishes:
#         return

#     print("Happy New Year!")
# happy_new_year()
# happy_new_year(False)


fullName = input("Enter your full name: ")
age = int(input("Enter your age: "))
address = input("Enter your address: ")
salary = int(input("Enter your salary: "))
print(fullName + " is " + str(age) + ", lives in " + address + ", and makes $" + str(salary) + ".")
print(f"{fullName} is {age}, lives in {address}, and makes ${salary}.")