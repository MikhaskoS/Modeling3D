# Пример простейшей функции
def HelloWorld():
    name = input("имя:")
    print("привет", name)

# деление с остатком


def DivMod(a, b):
    print(divmod(a, b))
    print(a, ':', b, '=', a//b, '+', a % b)

# преобразование типов


def Sum(a, b):
    print('a =', a, 'b =', b)
    print('1)', a + b)
    print('2)', str(a) + str(b))
    print('3)', int(a) + int(b))
    print('4)', float(a) + float(b))
# ---------------------------------------------------------------------------------
# работа со строками  https://docs.python.org/3/library/stdtypes.html#string-methods
# --------------------------------------------------------------------------------


def StringSample():
    str = 'abcdefghiklm'
    print('str =', str)
    print('str[0] =', str[0])
    print('str[1] =', str[1])
    print('str[-1] =', str[-1])
    # по индексу нельзя менять символ
    str2 = str.replace('a', 'A')
    print('str =', str)
    print('str2 =', str2)

    # [start:end:step]         [start:end) - вырезать часть строки
    str3 = '0123456789'
    print(str3[:])  # 0123456789
    print(str3[5:])  # 56789
    print(str3[2:5])  # 234
    print(str3[-3:])  # 789
    print(str3[5:-3])  # 56
    print(str3[::3])  # 0369
    print(str3[::-3])  # 9630

    print(len(str3))  # 10  длина строки

    str4 = '123.25 125.00 125.58'
    # ['123', '25 125', '00 125', '58']   - разделить строку
    s = str4.split('.')
    print(s)
    s = str4.split()  # ['123.25', '125.00', '125.58']
    print(s)

    print(str4.startswith('12'))  # True начинается ли с '12'
    print(str4.endswith('58'))  # True заканчивается ли на '58'
    print(str4.find('58'))  # 18 положение '58'
    print(str4.count('12'))  # 3 сколько раз встречается '12'

    print(str3.isalnum())  # True   - все символы буквы или цифры
    print(str4.isalnum())  # False

    chars = ['f', 's', 'x', 'j', 'm', 'x', 'u']
    qq = '-'.join(chars)
    print(qq)  # x-x-u-s-m-j-f      - построение строки из списка (рьъединение строк)

    str5 = 'привет, друг...'
    print(str5.strip('.'))  # привет, друг
    print(str5.capitalize())  # Привет, друг...
    print(str5.title())  # Привет, Друг...
    print(str5.upper())  # ПРИВЕТ, ДРУГ...

    str6 = 'ПриВет, ДруГ!'
    print(str6.lower())  # привет, друг!
    print(str6.swapcase())  # пРИвЕТ, дРУг!

    s = str6.replace('Вет', 'шел')  # Пришел, ДруГ!
    print(s)

# HelloWorld()


DivMod(10, 3)

Sum(5, 6)

Sum(2.36, 6.54)

StringSample()
