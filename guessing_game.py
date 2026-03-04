
TOTAL_GUESSES = 5


def ask_guess():
    guess = input("Enter any number between 1 to 100: ")
    return guess


def check_guess(target):
    guess_count = 0
    guess = ask_guess()
    while (guess_count < TOTAL_GUESSES):
        if guess == target:
            return 1
        if guess < target:
            print("Too Low!")
            guess_count += 1
        if guess > target:
            print("Too high!")
            guess_count += 1
        guess = ask_guess()


def main():
    check_guess()
