# --------------------------------
#  Свойства
# --------------------------------
class Duck():
    def __init__(self, input_name):
        # так автоматически определена переменная hidden_name, к которой отовсюду есть доступ
        self.hidden_name = input_name

    # чтобы ограничить к ней доступ, следует исказить имя на __hidden_name  (см далее)
    def get_name(self):
        print('inside the getter')
        return self.hidden_name

    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
    # методы get_name, set_name определены как свойства аттрибута name
    name = property(get_name, set_name)


# так можно задать имя
iam = Duck('Люся')
iam.hidden_name = 'Боб'
iam.set_name('Вася')
iam.name = 'Жорик'

# получить имя можно так
print(iam.hidden_name)
print(iam.get_name())
print(iam.name)


# --------------------------------
#  Свойства c помощью декораторов
# --------------------------------
class Fuck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name

    @name.setter  # если не указать сеттер, то изменить свойство извне не получится
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name


# так можно задать имя
iam = Fuck('Люся')
iam.hidden_name = 'Боб'
iam.name = 'Жорик'

# получить имя можно так
print(iam.hidden_name)
print(iam.name)

# --------------------------------
# запрет на изменение свойства
# --------------------------------


class Circle():
    def __init__(self, radius):
        self.radius = radius

    @property
    def diametr(self):
        return 2*self.radius


crc = Circle(5)
print('радиус = ', crc.radius, 'диаметр = ', crc.diametr)
# поскольку для diametr не указан сеттер, это свойство нельзя изменить
# crc.diametr = 30  !!!!!

# --------------------------------
#  Искажение имени
# --------------------------------


class Puck():
    def __init__(self, input_name):
        self.__hidden_name = input_name  # теперь iam.__hidden_name выдаст ошибку

    @property
    def name(self):
        print('inside the getter')
        return self.__hidden_name

    @name.setter  # если не указать сеттер, то изменить свойство извне не получится
    def name(self, input_name):
        print('inside the setter')
        self.__hidden_name = input_name


# так можно задать имя
iam = Puck('Люся')
iam.name = 'Жорик'

# получить имя можно так
print(iam.name)

# этот способ не убирает возможность получить значение.
# Он лишь предотвращает случайное изменение имени. Его косвенно можно извлечь так
print(iam._Puck__hidden_name)
