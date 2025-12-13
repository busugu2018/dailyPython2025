import random

def guessPlay():
    # Pick a random integer (Python’s randint needs a range, so we’ll pick a big one)
    # This creates a random number between 1 and 1,000,000 for example
    mySecret = random.randint(1, 1_000_000)

    print("\n" * 50)
    print("🎯 Try to guess the secret number! (Hint: it's somewhere between 1 and 1,000,000 😏)")

    attempts = 0

    while True:     
        try:
            guess = int(input("Your guess: "))
            attempts += 1  

            if guess == mySecret:
                print(f"🎉 Correct! You guessed the secret number {mySecret} in {attempts} attempts!")
                break
            elif guess == "x":
                print("Thanks for playing. Bye!")
                break 
            elif guess < mySecret:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

if __name__ == "__main__":
    guessPlay()