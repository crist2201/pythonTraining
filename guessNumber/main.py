import random

# Random number between 1 and 100
def generate_number():
    return random.randint(1,100)

# Choose a difficulty it has to be hard or easy
def difficulty():
    dif = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if dif == 'easy':
        attempts = 10
    elif dif == 'hard':
        attempts = 5
    return attempts

# Make guess
def guess_number():
    guess = int(input("Make a guess: "))
    return guess

# Compare the guess with the random number
def compare(number,attempts):
    while(attempts > 0):
        guess = guess_number()
        if number > guess:
            attempts = attempts-1
            print("Too low.")
            print("Guess again")
            print(f"You have {attempts} attempts remaining to guess the number")
        elif number < guess:
            attempts = attempts - 1
            print("Too high.")
            print("Guess again")
            print(f"You have {attempts} attempts remaining to guess the number")
        else:
            print(f"You got it! The answer was {number}")
            break
    print("Do you want to try again?")


# Main flow

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
number = generate_number()
attempts = difficulty()
print(f"You have {attempts} attempts remaining to guess the number")
compare(number,attempts)