'''
This program generates a dict using dict comprehensions
'''

import math


def run():

    # Create a dict with keys: first 100 natural numbers and values: first 100 natural numbers cubed

    print('Without dict comprehensions')
    my_dict = {}

    for i in range(1, 101):
        if i % 3 != 0:  # Not divisible by three
            my_dict[i] = i**3
    
    print(my_dict)

    print('With dict comprehensions')
    dict_comp = {i : i**3 for i in range(1, 101) if i % 3 != 0}

    print(dict_comp)

    # Challenge: create a dictionary comprehension with keys: first 1000 natural numbers and values: square roots
    dict_challenge = {i : round(math.sqrt(i), 2) for i in range(1, 1001)}

    print(dict_challenge)


if __name__ == '__main__':
    run()