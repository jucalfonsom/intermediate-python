'''
This program was used to learn assert statements
'''

def divisors(num):
    divisors = []

    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)

    return divisors

def run():
    num = input('Write one number: ')
    assert num.isnumeric(), 'Write only positive numbers.'

    print(divisors(int(num)))
    print('End successful')


if __name__ == '__main__':
    run()