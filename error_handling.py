'''
This program was used to learn error handling
'''

def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError('You cannot enter an empty string')
        
        return string == string[::-1]
    
    except ValueError as ve:
        print(ve)
        
        return False


def run():
    try:
        word = input('Write one word: ')
        print(palindrome(word))
    
    except TypeError:
        print('Write only strings')


if __name__ == '__main__':
    run()