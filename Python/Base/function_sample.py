def empty():
    'Функция, которая ничего не делает'
    pass


def sample1(a, b, c):
    return {'a': a, 'b': b, 'c': c}


print(sample1(1, 2, 3))  # {'a': 1, 'b': 2, 'c': 3}


def sample2(a='a', b='b', c='c'):
    return {'a': a, 'b': b, 'c': c}


print(sample2(1, 2, 3))  # {'a': 1, 'b': 2, 'c': 3}


def sample3(*args):  # любое число аргументов (кортеж)
    print(args)


sample3(1, 2, 'Hello')  # (1, 2, 'Hello')


def sample4(**kwargs):  # группировка аргументов в словарь
    print(kwargs)


sample4(a='one', b='two', c='three')  # {'a': 'one', 'b': 'two', 'c': 'three'}


def sample5(a, b):
    'Это строка документации'
    return int(a) + int(b)


def sample6(a, b):
    '''
    Расширенная документация.
    Пояснение к функции.
    '''
    return int(a) + int(b)


help(sample6)  # вывод на экран строки документации
# ----------------------------


def buggy(a, p=[]):
    p.append(a)
    print(p)


def nobuggyA(a, p=[]):
    p = []
    p.append(a)
    print(p)


def nobuggyB(a, p=None):
    if p is None:
        p = []
    p.append(a)
    print(p)


buggy(1)  # [1]
buggy(2)  # [1, 2]
nobuggyB(1)  # [1]
nobuggyB(2)  # [2]
# ----------------------------
# Замыкания. Замкание это функция, которая
# динамически генерируется внутри другой функции
# и может использовать параметры, определенные вне функции
# ----------------------------


def func1(name):
    def func2():
        return "My name: '%s'" % name
    return func2
# ----------------------------


a = func1('Вася')
b = func1('Петя')
print(a)  # <function func1.<locals>.func2 at 0x00000273711D70D0>
print(b)  # <function func1.<locals>.func2 at 0x0000027371D180D0>
print(a())  # My name: 'Вася'
print(b())  # My name: 'Петя'
