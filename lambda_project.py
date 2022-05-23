'''
This program prints the multiplication of all the elements of a list.
'''

from concurrent.futures.thread import _worker
from functools import reduce
from xml.sax import make_parser
from data_filtering_db import DATA


def run():
        
    # List comprehensions

    # Get all python devs
    print('-' * 40)
    print('All python devs:')
    all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'python']

    for worker in all_python_devs:
        print(f'- {worker}')

    # Get all Platzi workers
    print('-' * 40)
    print('All Platzi workers:')
    all_platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']

    for worker in all_platzi_workers:
        print(f'- {worker}')
    
    # Filter and map

    # Get all adults
    print('-' * 40)
    print('All adults:')
    all_adults = list(filter(lambda worker: worker['age'] > 18, DATA))

    # Use map to get name
    all_adults = list(map(lambda worker: worker['name'], all_adults))

    for adult in all_adults:
        print(f'- {adult}')

    # Add a new key (old) to validate if the worker is older or younger than 70 years old.
    print('-' * 40)
    print('New key:')

    # | <- Join two dictionaries (python v3.9)
    # old_people = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA)) 
    # Python v3.8.10
    old_people = list(map(lambda worker: {**worker, **{"old": worker["age"] > 70}}, DATA)) 

    for people in old_people:
        print(f'- {people}')


    # Challenge: create all_python_devs and all_platzi_workers lists using filter and map
    print('-' * 40)
    print('Challenge 1:')

    # Get all python devs
    print('All python devs:')
    all_python_devs_2 = list(filter(lambda worker: worker['language'] == 'python', DATA))
    all_python_devs_2 = list(map(lambda worker: worker['name'], all_python_devs_2))

    for worker in all_python_devs_2:
        print(f'- {worker}')
    
    # Get all Platzi workers
    print('All Platzi workers:')
    all_platzi_workers_2 = list(filter(lambda worker: worker['organization'] == 'Platzi', DATA))
    all_platzi_workers_2 = list(map(lambda worker: worker['name'], all_platzi_workers_2))

    for worker in all_platzi_workers_2:
        print(f'- {worker}')

    # Challenge 2: create old_people list and adult lists using list comprehensions
    print('-' * 40)
    print('Challenge 2:')

    # Get all adults
    print('All adults:')
    all_adults_2 = [worker['name'] for worker in DATA if worker['age'] > 18]

    for adult in all_adults_2:
        print(f'- {adult}')
    
    # Add a new key (old) to validate if the worker is older or younger than 70 years old.
    print('Old people:')
    old_people_2 = [{**worker, **{'old': worker['age'] > 70}} for worker in DATA]

    for people in old_people_2:
        print(f'- {people}')


if __name__ == '__main__':
    run()