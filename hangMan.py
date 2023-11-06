import random


def run_game():
    word = random.choice(["apple", "banana", "pizza", "burger"])
    user_name = input('Enter your name: ')
    print(f'Welcome to Hangman, {user_name}')

    # Setup
    guessed = ''
    tries = 3

    while tries > 0:
        blanks = 0

        print('Word: ', end='')
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('_', end='')
                blanks += 1

        print()  # Adds a new line

        if blanks == 0:
            print('You got it right!')
            break

        guess = input('Enter a letter: ')

        if guess[0] in guessed:
            print('You already guessed the letter, try again.')
            continue

        guessed += guess[0]

        if guess not in word:
            tries -= 1
            print(f'Sorry that was wrong... {tries} tries remaining.')
            if tries == 0:
                print('L, you lost.')
                break


if __name__ == "__main__":
    run_game()
