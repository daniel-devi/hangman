import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print("\n \n ")
        print('You have', lives, 'lives left and you have used these letters below : ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(f"Your word is {len(word_letters)} long")
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        
        
        def get_hangman_stage(remaining_attempts):
            max_attempts = 6
            stages = ["""
                ------
                |    |
                |
                |
                |
                |
                |
            ------------
            """, """
                ------
                |    |
                |    O
                |
                |
                |
                |
            ------------
            """, """
                ------
                |    |
                |    O
                |    |
                |    |
                |
                |
            ------------
            """, """
                ------
                |    |
                |    O
                |    |
                |    |
                |   /
                |
            ------------
            """, """
                ------
                |    |
                |    O
                |    |
                |    |
                |   / \\
                |
            ------------
            """, """
                ------
                |    |
                |    O
                |  --|
                |    |
                |   / \\
                |
            ------------
            """, """
                ------
                |    |
                |    O
                |  --|--
                |    |
                |   / \\
                |
            ------------
            """]
            return print(stages[max_attempts - remaining_attempts])
        
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')
                get_hangman_stage(lives)

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        
        print('You died, sorry. The word was', word)
        get_hangman_stage(lives)
    else:
        print('YAY! You guessed the word', word, '!!')


if __name__ == '__main__':
    hangman()
