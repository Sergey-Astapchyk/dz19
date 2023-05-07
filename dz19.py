def add(a, b):          # Функция отвечающая за операцию сложения
    return a + b


def subtract(a, b):     # Функция отвечающая за операцию вычитания
    return a - b


def multiply(a, b):     # Функция отвечающая за операцию умножения
    return a * b


def divide(a, b):       # Функция отвечающая за операцию деления
    try:                # Обработка ошибки деления на ноль
        return a / b
    except ZeroDivisionError:
        return 'Деление на 0'


while True:
    c = input('Введите операцию +,-,*,/: ')
    if c == '0':        # При вводе ноль программа завершается
        break
    a = int(input('Введите число: '))
    b = int(input('Введите число: '))
    if c == '+':
        print(add(a, b))
    elif c == '-':
        print(subtract(a, b))
    elif c == '*':
        print(multiply(a, b))
    elif c == '/':
        print(divide(a, b))
