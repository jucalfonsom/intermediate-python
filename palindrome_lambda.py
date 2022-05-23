'''
This program detects if a string is a palindrome using lambda functions
'''


def run():
    palindrome = lambda string: string == string[::-1]


    word = input('Write a word: ')
    is_palindrome = palindrome(word)
    if is_palindrome:
        print(f'The word "{word}" is a palindrome')
    else:
        print(f'The word "{word}" is not a palindrome')


if __name__ == '__main__':
    run()