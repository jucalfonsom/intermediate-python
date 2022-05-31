'''
This program was used to learn file management
'''


def read(): # Read file
    numbers = []
    with open('./files/files.txt', 'r', encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write(): # Write file
    names = ['Juan', 'Facundo', 'Miguel', 'Pepe', 'Christian', 'Rocío']
    with open('./files/names.txt', 'w', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')
    print('File created')

def run():
    # read()
    write()


if __name__ == '__main__':
    run()