n = int(input("Enter a number: "))

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and n in range(2,5):
    print("Not Weird")
elif n % 2 == 0 and n in range(6,20):
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Weird")



if __name__ == '__main__':
n = int(input().strip())

if n % 2 != 0:  # Odd
    print("Weird")
elif 2 <= n <= 5:  # Even, 2 to 5
    print("Not Weird")
elif 6 <= n <= 20:  # Even, 6 to 20
    print("Weird")
elif n > 20:  # Even, > 20
    print("Not Weird")