'''
This program was used to learn assert statements
'''

def palindrome(string):
    assert len(string) > 0, 'You cannot enter an empty string'
    return string == string[::-1]


def run():
    try:
        word = input('Write one word: ')
        print(palindrome(word))
    
    except TypeError:
        print('Write only strings')


if __name__ == '__main__':
    run()