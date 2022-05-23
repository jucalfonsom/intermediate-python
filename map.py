'''
This program prints the squares of a list using map
'''


def run():
    my_list = [1, 2, 3, 4, 5]

    # Using list comprehension
    squares = [i**2 for i in my_list]

    print(squares)

    #Using map
    squares = list(map(lambda x: x**2, my_list))

    print(squares)


if __name__ == '__main__':
    run()