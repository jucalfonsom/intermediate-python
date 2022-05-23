'''
This program prints the multiplication of all the elements of a list.
'''

from functools import reduce


def run():
    my_list = [2, 2, 2, 2, 2]

    # Using for
    print('Using for')
    total_multiplication = 1
    for i in my_list:
        total_multiplication = total_multiplication * i

    print(f'{total_multiplication}')   

    #Using map
    print('Using reduce')
    total_multiplication_2 = reduce(lambda x, y: x*y, my_list)

    print(f'{total_multiplication_2}')   


if __name__ == '__main__':
    run()