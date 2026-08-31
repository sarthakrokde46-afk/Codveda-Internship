import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Maximum number of attempts
max_attempts = 5

print("Welcome to Number Guessing Game!")
print("Guess a number between 1 and 100.")
print("You have", max_attempts, "attempts.")

for attempt in range(max_attempts):

    try:
        guess = int(input("\nEnter your guess: "))

    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess == number:
        print("Congratulations! You guessed the correct number.")
        break

    elif guess < number:
        print("Too low!")

    else:
        print("Too high!")

else:
    print("\nGame Over!")
    print("The correct number was:", number)