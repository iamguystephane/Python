
TOTAL_GUESSES = 5


def ask_guess():
    guess = input("Enter any number between 1 to 100: ")
    return int(guess)


def check_guess(target):
    guess_count = 0
    guess = ask_guess()
    while (guess_count < TOTAL_GUESSES - 1):
        guess_count += 1
        if guess == target:
            return guess_count
        if guess < target:
            print(f"Too Low! {guess_count} / {TOTAL_GUESSES} guesses used.")
        if guess > target:
            print(f"Too high! {guess_count} / {TOTAL_GUESSES} guesses used.")
        guess = ask_guess()
    return 0


def main():
    result = check_guess(44)
    if result == 0:
        print("You ran out of guesses. Run the program to try again.")
        return
    print(f"You guessed the number correctly in {result} number of guesses.")
    print("Well done.")


main()
