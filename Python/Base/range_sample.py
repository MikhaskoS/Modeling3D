def Iter():
    'пример встроенного генератора range()'
    numbers = [1, 2, 3, 4, 5, 6]
    dictnum = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    # генерация числовых последовательностей range(start, end, step)
    num1 = list(range(0, 10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(num1)
    num2 = list(range(0, 10, 2))  # [0, 2, 4, 6, 8]
    print(num2)
    num3 = list(range(10, 0, -1))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(num3)


Iter()

# генератор можно построить вручную, используя yeld


def my_range(first=0, last=10):
    number = first
    while number < last:
        yield number * number
        number += 1


ranger = list(my_range(2, 5))
print(ranger)  # [4, 9, 16]
# for i in ranger:
#     print(i)
