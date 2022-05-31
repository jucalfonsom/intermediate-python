'''
This program is the final project of the course. It consists of the hangman game with spanish words
'''

import os
import random


def clear():
    os.system('cls')
    os.system('clear')

def get_word(words):
    random_word = random.randint(0, len(words)-1)
    word = words[random_word]
    return word

def read_data():
    words = []
    with open('./data.txt', 'r') as f:
        for line in f:
            words.append(line.strip())
    word = get_word(words)
    print(word)
    return word

def validate_letter(word, letter, lives):
    new_lives = lives - 1
    if new_lives > 0:
        if letter in word:
            print('nes')
        else:
            new_lives -= 1
            clear()
            print(f'New lives: {new_lives}')

    else:
        print('GAME OVER!!!!')

    

def run():
    try:
        clear()
        message = []
        lives = 10
        word = read_data()
        if word == None:
            raise 
        message = list('_' * len(word))

        print(message)
        letter = input('Write one letter: ')
    except FileNotFoundError as fe:
        print(f'Error trying to read file. Error: {fe}')
    except KeyboardInterrupt:
        print('User ended the game')



if __name__ == '__main__':
    run()