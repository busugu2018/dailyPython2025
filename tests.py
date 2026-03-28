year = int(input("Enter  year: "))
if year%400 == 0 and year%100 == 0:
    print(str(year) + " is a leap year.")
elif year%4 == 0 and year%100 != 0:
    print(str(year) + " is a leap year.")
else:
    print(str(year) + " is a NOT a leap year.")