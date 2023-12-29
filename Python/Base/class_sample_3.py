# --------------------------------
#  Типы методов
# --------------------------------
class A():
    count = 0

    def __init__(self):
        A.count += 1

    def SayHello(self):     # метод экземпляра
        print('Hello!')

    @classmethod
    def Bingo(cls):         # метод класса
        print('Класс А:', cls.count)

    @staticmethod
    def IDClass():          # статический метод
        print('BUGAGA!')


smpl1 = A()
smpl2 = A()
smpl3 = A()

smpl1.SayHello()
A.Bingo()
A.IDClass()
