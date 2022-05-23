'''
This program was used to learn debugging techniques
'''

def divisors(num):
    divisors = []

    for i in range(1, num + 1):
        if num % i == 1: # Intentional error
            divisors.append(i)

    return divisors

def run():
    num = int(input('Write one number: '))
    print(divisors(num))
    print('End successful')


if __name__ == '__main__':
    run()