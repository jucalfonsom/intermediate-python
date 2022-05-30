'''
This program was used to learn debugging techniques
'''

def divisors(num):
    divisors = []

    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)

    return divisors

def run():
    try:    
        num = int(input('Write one number: '))
        if num < 0:
            raise ValueError('Please write a positive number')
        print(divisors(num))
        print('End successful')
    
    except ValueError as ve:
        print(f'Write only numbers. Error: {ve}')


if __name__ == '__main__':
    run()