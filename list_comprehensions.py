'''
This program generates a list using list comprehensions
'''


def run():

    print('Without list comprehensions')
    squares = []

    for i in range(1, 101):
        if i % 3 != 0:  # Not divisible by three
            squares.append(i**2)
    
    print(squares)

    print('With list comprehensions')
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]

    print(squares)

    # Challenge: create a list comprehension of all multiples of 4, which are multiples of 6 and 9, up to 5 digits
    
    print('Challenge')

    list_challenge = [i for i in range(1,100000) if i % 36 == 0]

    print(list_challenge)


if __name__ == '__main__':
    run()