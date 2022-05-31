'''
This program is the final project of the course. It consists of the hangman game with spanish words
'''


import os
from file_management import read_data, get_word, normalize


def clear():
    os.system('cls')
    os.system('clear')

def print_message(message):
    guess_message = ''.join(message)
    print(f'Word: {guess_message}')

def validate_letter(word_list, letter, lives, message):
    if letter in word_list:
        list_index = [index for index, element in enumerate(word_list) if element == letter]

        for i in list_index:
            message[i] = letter
    else:
        lives -= 1
    return message, lives

def run():
    try:
        clear()
        won = False
        path = './data.txt'
        # path = './hangman/data.txt'
        message = []
        lives = 10
        # Get data information
        words = read_data(path)
        if words == None:
            raise FileNotFoundError(f'Error with file in path {path}')
        
        # Get word
        word = get_word(words)
        if word == None:
            raise ValueError('Error getting word in data')
        message = list('_' * len(word))
        word_list = list(word)
        print(word_list)

        # Guess game
        while lives > 0 and won == False:
            clear()
            print(f'Lives:{lives}')
            print_message(message)
            letter = input('Guess one letter: ').upper()
            letter = normalize(letter)
            if len(letter) > 1:
                input('Please enter only one letter. Press enter to continue.')
                continue
            message, lives = validate_letter(word_list, letter, lives, message)
            if '_' in message:
                continue
            else:
                won = True
        
        if won:
            clear()
            print('YOU WON !!!!!')
            print(f'You guess the word: {word}')
        else:
            clear()
            print('GAME OVER !!!!')
            print(f'The word was: {word}')



    except FileNotFoundError as fe:
        print(f'Error trying to read file. Error: {fe}')
    except ValueError as ve:
        print(f'Error in execution. Error: {ve}')
    except KeyboardInterrupt:
        print('User ended the game')



if __name__ == '__main__':
    run()