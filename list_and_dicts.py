'''
This program print nested list and dict 
'''


def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Juan", "lastname": "Alfonso"}

    super_list = [
        {"firstname": "Juan", "lastname": "Alfonso"},
        {"firstname": "Pedro", "lastname": "Perez"},
        {"firstname": "Susana", "lastname": "Martinez"},
        {"firstname": "José", "lastname": "García"},
        {"firstname": "Miguel", "lastname": "Torres"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    print('Super dict')

    for key, value in super_dict.items():
        print(f'{key} - {value}')

    print('Super list')

    for item in super_list:
        for key,value in item.items():
            print(f'{key} - {value}')


if __name__ == '__main__':
    run()