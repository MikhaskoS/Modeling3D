from string import ascii_letters

# Различные способы генерации списков

# --------------------------------------------
# Использование циклов
# --------------------------------------------

s = []  # Создаем пустой список
for i in range(10):  # Осуществляем 10 итераций - от 0 до 9
    s.append(i ** 3)  # Добавляем к списку куб каждого числа
print(s)  # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

# Так как строка является итерируемым объектом, то по ней можно пройтись в цикле.
word = 'Парашют'  # Начальное слово
s = []  # Создаем пустой список
for i in word.upper():  # Проходимся по каждой букве в слове
    s.append(i)  # Приводим все буквы к верхнему регистру
print(s)  # ['П', 'А', 'Р', 'А', 'Ш', 'Ю', 'Т']

# --------------------------------------------
# Использование map(), возвращающей итератор
# --------------------------------------------


def mod5(x):      # Создаем функцию, которая возвращает
    return x % 5  # остаток от деления на 5


s = [5, 7, 11, 20]  # Исходный список
print(list(map(mod5, s)))  # [0, 2, 1, 0] - список остатков

s = [7, 22, 49, 701]  # Исходный список чисел
n = list(map(lambda x: x // 7, s))  # Новый список целочисленного деления на 7
print(n)  # [1, 3, 7, 100]

# --------------------------------------------
# включения списков
# --------------------------------------------
# +++++++++++++++++++++++++++++++
# новый_список = [«операция» for «элемент списка» in «список»]
# +++++++++++++++++++++++++++++++

old_prices = [120, 550, 410, 990]
discount = 0.15  # Скидка в 15 %
# Вычисляем новые цены (без учета копеек)
new_prices = [int(product * (1 - discount)) for product in old_prices]
print(new_prices)  # [102, 467, 348, 841]

# +++++++++++++++++++++++++++++++
# новый_список = [«операция» for «элемент списка» in «список» if «условие»]
# +++++++++++++++++++++++++++++++

numbers = [121, 544, 111, 99, 77]
# Выбираем только те числа, которые делятся на 11
number11 = [num for num in numbers if num % 11 == 0]
print(number11)  # [121, 99, 77]

# +++++++++++++++++++++++++++++++
# новый_список = [«операция» if «условие» for «элемент списка» in «список»]
# +++++++++++++++++++++++++++++++

letters = 'hыtφтrцзqπ'  # набор букв из разных алфавитов

# Разграничиваем буквы на английские и не английские
# ascii_letters - объект, содержащий только буквы английского алфавита
is_eng = [
    f'{letter}-ДА' if letter in ascii_letters else f'{letter}-НЕТ' for letter in letters]
print(is_eng)
# ['h-ДА', 'ы-НЕТ', 't-ДА', 'φ-НЕТ', 'т-НЕТ', 'r-ДА', 'ц-НЕТ', 'з-НЕТ', 'q-ДА', 'π-НЕТ']

# --------------------------------------------
# Примеры сложных запросов
# --------------------------------------------

words = ['Я', 'изучаю', 'Python']  # Список слов
# Двойная итерация: по словам и по буквам
letters = [letter for word in words for letter in word]
# ['Я', 'и', 'з', 'у', 'ч', 'а', 'ю', 'P', 'y', 't', 'h', 'o', 'n']
print(letters)

table = [[x * y for x in range(1, 6)] for y in range(1, 6)]
print(table)
# [[1, 2, 3, 4, 5],
#  [2, 4, 6, 8, 10],
#  [3, 6, 9, 12, 15],
#  [4, 8, 12, 16, 20],
#  [5, 10, 15, 20, 25]]
