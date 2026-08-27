primeNum = 0
notPrimeNum = 0

num = int(input("Enter a number: "))

while num != 0:
    if num <= 1:
        prime = False
    else:
        for i in range(2, num):
            if num % i == 0:
                prime = True
                break
        else:
            print("Prime")