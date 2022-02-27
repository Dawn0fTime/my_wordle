# Wordle clone using a custom word list.
# Based on tutorial at https://replit.com/@JacobLower3/wordle-tutorial
import random
import sys
from termcolor import colored

with open('word_list.txt') as f:
    words = f.read().upper().splitlines()


def display_instructions():
    print("\nLet's play Wordle!")
    print("Type a 5 letter word and hit enter")
    print("Invalid words will be ignored.\n")


def play_game():
    display_instructions()
    word = random.choice(words)

    for attempt in range(1, 7):

        guess = ''
        while True:
            guess = input().upper()
            if guess in words:
                break
            else:
                move_cursor()

        move_cursor()

        for i in range(min(len(guess), 5)):
            if guess[i] == word[i]:
                print(colored(guess[i], 'green'), end='')
            elif guess[i] in word:
                print(colored(guess[i], 'yellow'), end='')
            else:
                print(guess[i], end='')
        print()

        if guess == word:
            print(colored(f'\nCongrats! You got the Wordle in {attempt} tries!\n', 'red'))
            break
        elif attempt == 6:
            print(colored(f'\nSorry, the Worldle is {word}.\n', 'red'))


def move_cursor():
    # Move the cursor back to the previous line and erase text
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')


if __name__ == '__main__':
    play_again = ''
    while play_again != 'q':
        play_game()
        play_again = input("Let's play again! Press enter or type q to quit: ")


# TODO: don't highlight duplicates
# you can easily just set a flag to true at the beginning of the attempt loop,
# and then set it to true in the one where we find it in the correct place.
# Then in the conditional where we check that it is in the word, but in the
# wrong place, we can also check if that flag is true. If it is false, then we
# can color it yellow otherwise we can leave it as normal text. Hope this makes
# sense, as I've implemented it and got it working
