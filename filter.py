'''
This program prints odd numbers from one list using filter
'''


def run():
    my_list = [1, 4, 5, 6, 9, 13, 19, 21]

    # Using list comprehension
    odd = [i for i in my_list if i % 2 != 0]
    
    print(odd)

    # Using filter
    odd_filter = list(filter(lambda x: x%2 != 0, my_list))

    print(odd_filter)


if __name__ == '__main__':
    run()