def recursiveInput(size):
    number = input('Введите число: ')
    if size == 1:
        print(number, end = ' ')
    else:
        recursiveInput(size - 1)
        print(number, end = ' ')

inputSize = int(input('Введите размер: '))
recursiveInput(inputSize)