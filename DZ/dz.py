

# Dz 29 -

class Clock:
    DAY = 86400

    def __init__(self, sec):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        self.sec = sec % self.DAY

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f'{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}'

    @staticmethod
    def get_form(x):
        return str(x) if x > 9 else '0' + str(x)

    @staticmethod
    def check(other):
        """Исключение для Перегрузки операторов. \n
           Служит для проверки правого операнда, что он является типом класса Clock."""
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом класса Clock")

    def __add__(self, other):
        self.check(other)
        return Clock(self.sec + other.sec)

    def __sub__(self, other):
        self.check(other)
        return Clock(self.sec - other.sec)

    def __mul__(self, other):
        self.check(other)
        return Clock(self.sec * other.sec)

    def __floordiv__(self, other):
        self.check(other)
        return Clock(self.sec // other.sec)

    def __mod__(self, other):
        self.check(other)
        return Clock(self.sec % other.sec)


c1 = Clock(100)
c2 = Clock(200)
print(c1.get_format_time())
print(c2.get_format_time())

c3 = c1 + c2
c4 = c1 - c2
c5 = c1 * c2
c6 = c1 // c2
c7 = c1 % c2

print()
print(f'{c3.get_format_time()} (x + y)')
print(f'{c4.get_format_time()} (x - y)')
print(f'{c5.get_format_time()} (x * y)')
print(f'{c6.get_format_time()} (x // y)')
print(f'{c7.get_format_time()} (x % y)')

# Dz 28 - класс студент

# class Studen:
#     def __init__(self,name):
#         self.name = name
#         self.comp = self.comp()  # доступ к классу комп
#
#     def infa(self):  # метод распечатывающий инфу
#         print(f'{self.name}', '=>',end=' ')
#         print(f'{self.comp.model}', end=' ')
#         print(f'{self.comp.cpu}',end=' ')
#         print(f'{self.comp.gpu}')
#
#
#
#     class comp():  # класс с инфой о компе
#         def __init__(self):
#             self.model = 'hp'
#             self.cpu = 'i7'
#             self.gpu = '16'
#
#
#
# roman = Studen('roman')
# roman.infa()
# vladimir =Studen('vladimir')
# vladimir.infa()




# Dz 28 - создать класс стол и дочерние классы
# import math
#
#
# class Table:
#
#     def __init__(self, width, length, radius):
#         self._width = width
#         self._length = length
#         self._radius = radius
#
#     def info_square_table(self):
#         raise NotImplementedError("В классе должен метод square_table()")
#
#
# class TableRectangular(Table):
#     def square_table(self):
#         return self._width * self._length
#
#     def set_square_table(self, width=None, length=None):
#         if width is None:
#             if length:
#                 self._length = length
#
#         elif length is None:
#             if width:
#                 self._width = width
#
#         else:
#             if width and length:
#                 self._width = width
#                 self._length = length
#
#     def info_square_table(self):
#         print(f"Площадь прямоугольного стола: {self.square_table()}")
#
#
# class TableRound(Table):
#     def square_table(self):
#         return round(math.pi * (self._radius ** 2), 2)
#
#     def info_square_table(self):
#         print(f"Площадь круглого стола: {self.square_table()}")
#
#
# rec = TableRectangular(20, 10, 0)
# rec.info_square_table()
# rec.set_square_table(length=20)
# rec.info_square_table()
# ro = TableRound(0, 0, 20)
# ro.info_square_table()





# Dz 27 - доработать  класс аккаунт

# import re
#
#
# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     SUFFIX_RUB = 'RUB'
#     SUFFIX_USD = 'USD'
#     SUFFIX_EUR = 'EUR'
#
#     def __init__(self, surname, num, percent, value=0):
#         self.surname = self.set_surname(surname)
#         self.num = num
#         self.percent = percent
#         self.value = value
#         print(f'Счёт №{self.num} принадлежащий {self.surname} был открыт.')
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счёт №{self.num} принадлежащий {self.surname} был закрыт.')
#
#     @classmethod
#     def set_rate_usd(cls, new_rate):
#         cls.rate_usd = new_rate
#
#     @classmethod
#     def set_rate_eur(cls, new_rate):
#         cls.rate_eur = new_rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @property
#     def value(self):
#         return self.__value
#
#     @value.setter
#     def value(self, new_value):
#         if not isinstance(new_value, (int | float)):
#             raise TypeError('Убедитесь что введено цифровое значение для баланса')
#         if new_value < 0:
#             raise ValueError('Отрицательное значение баланса не допустимо.')
#         self.__value = round(float(new_value), 2)
#
#     def get_surname(self):
#         return self.surname
#
#     def set_surname(self, new_surname: str):
#         if not isinstance(new_surname, str):
#             raise TypeError('Фамилия должна быть строкой')
#         elif re.findall(r'[^а-яё-]', new_surname, re.IGNORECASE):
#             raise ValueError('Допустимы только буквы А-я и -')
#         self.surname = new_surname
#
#     def add_money(self, amount):
#         self.value += amount
#         print(f'{amount} {Account.SUFFIX_RUB} успешно добавлено!')
#         self.print_balance()
#
#     def convert_to_usd(self):
#         usd_value = self.convert(self.value, self.rate_usd)
#         print(f'Состояние счёта: {usd_value} {Account.SUFFIX_USD}')
#
#     def convert_to_eur(self):
#         eur_value = self.convert(self.value, self.rate_eur)
#         print(f'Состояние счёта: {eur_value} {Account.SUFFIX_EUR}')
#
#     def add_percent(self):
#         self.value += self.value * self.percent
#         print(f'Проценты были успешно начислены!')
#         self.print_balance()
#
#     def withdraw_money(self, amount):
#         if amount > self.value:
#             print(f'К сожалению у вас нет {amount} {Account.SUFFIX_RUB}')
#         else:
#             self.value -= amount
#             print(f'{amount} {Account.SUFFIX_RUB} было успешно снято!')
#         self.print_balance()
#
#     def print_balance(self):
#         print(f'Текущий баланс: {self.value} {Account.SUFFIX_RUB}.')
#
#     def print_info(self):
#         print('Информация о счете:')
#         print('-' * 20)
#         print(f'№{self.num}')
#         print(f'Владелец: {self.surname}')
#         self.print_balance()
#         print(f'Проценты: {self.percent:.0%}')
#         print('-' * 20)
#
#
# if __name__ == '__main__':
#     acc = Account('Долгих', '12345', 0.03, 5000)
#     acc.print_info()
#     acc.convert_to_usd()
#     acc.convert_to_eur()
#     Account.set_rate_usd(2)
#     Account.set_rate_eur(3)
#     print()
#     acc.convert_to_usd()
#     acc.convert_to_eur()
#     acc.set_surname('Дюма')
#     acc.print_info()
#     print()
#     acc.add_percent()
#     print()
#     acc.withdraw_money(100)
#     print()
#     acc.withdraw_money(3000)
#     print()
#     acc.add_money(5000)
#     print()
#     acc.withdraw_money(3000)
#     print()



# Dz 26 - Создать класс персон



# class Person:
#
#     def __init__(self, name: str, old: int):
#         __name = ''
#         __old = 0
#         self.name = name
#         self.old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, new_name):
#         if not isinstance(new_name, str):
#             raise TypeError('Имя задается строкой')
#         self.__name = new_name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, new_old):
#         if not isinstance(new_old, int):
#             raise TypeError('Возраст задаётся цифрами')
#         self.__old = new_old
#
#     @old.deleter
#     def old(self):
#         del self.__old
#
#
# person = Person(name='Irina', old=26)
# print(person.__dict__)
# person.name = 'Igor'
# print(person.name)
# person.old = 31
# print(person.old)
#
# del person.name
# print(person.__dict__)








#
# # Dz 25 Создать класс прямоугольник
#
# from math import sqrt
#
#
# class Rectangle:
#     def __init__(self, length, height):
#         self.length = length
#         self.height = height
#         self.area = self.length * self.height
#         self.perimeter = 2 * (self.length + self.height)
#         self.diagonal = round(sqrt(self.length ** 2 + self.height ** 2), 2)
#
#     def get_length(self):
#         return f'Длина прямоугольника: {self.length}'
#
#     def get_height(self):
#         return f'Ширина прямоугольника: {self.height}'
#
#     def get_area(self):
#         return f'Площадь прямоугольника: {self.area}'
#
#     def get_perimeter(self):
#         return f'Периметр прямоугольника: {self.perimeter}'
#
#     def get_diagonal(self):
#         return f'Гипотенуза прямоугольника: {self.diagonal}'
#
#     def __str__(self):
#         graphic = ''
#         for i in range(self.length):
#             if i == 0 or i == self.length - 1:
#                 graphic += '* ' * self.height + '\n'
#             else:
#                 graphic += '* ' + '  ' * (self.height - 10) + '*' + '\n'
#         return graphic
#
#
# rectangle = Rectangle(3, 9)
# print(rectangle.get_length())
# print(rectangle.get_height())
# print(rectangle.get_area())
# print(rectangle.get_perimeter())
# print(rectangle.get_diagonal())
# print(rectangle)









# Dz 24 Создать класс автомобиль

#
# class Car:
#
#     def __init__(
#             self, model, year_of_issue, manufacturer, engine_power, color, price, ):
#         self.model = model
#         self.year_of_issue = year_of_issue
#         self.manufacturer = manufacturer
#         self.engine_power = engine_power
#         self.color = color
#         self.price = price
#
#     def __str__(self):
#         a = 'данные атомобиля '
#         b = f'\nНазвание модели: {self.model}\n' \
#             f'Год выпуска: {self.year_of_issue}\n' \
#             f'Производитель: {self.manufacturer}\n' \
#             f'Мощность двигателя: {self.engine_power} л.с.\n' \
#             f'Цвет машины: {self.color}\n' \
#             f'Цена: {self.price}\n'
#
#         return a + b
#
#     def set_model(self, model):
#         self.model = model
#
#     def get_model(self):
#         return self.model
#
#     def set_year_of_issue(self, year_of_issue):
#         self.year_of_issue = year_of_issue
#
#     def get_year_of_issue(self):
#         return self.year_of_issue
#
#     def set_manufacturer(self, manufacturer):
#         self.manufacturer = manufacturer
#
#     def get_manufacturer(self):
#         return self.manufacturer
#
#     def set_engine_power(self, engine_power):
#         self.engine_power = engine_power
#
#     def get_engine_power(self):
#         return self.engine_power
#
#     def set_color(self, color):
#         self.color = color
#
#     def get_color(self):
#         return self.color
#
#     def set_price(self, price):
#         self.price = price
#
#     def get_price(self):
#         return self.price
#
#
# if __name__ == '__main__':
#     car = Car(
#         model='X7 M50i',
#         year_of_issue='2021',
#         manufacturer='BMW',
#         engine_power=530,
#         color='white',
#         price=10790000
#     )
#
#     print(car)

# DZ 23 - просканировать директорию и вывести размер и название файлов и папок
# import os
# import time
#
# file_path = r'test\folder1\file.txt'
# if os.path.exists(file_path):
#     dirs, name = os.path.split(file_path)
#     print(f'{name} - {os.path.getsize(file_path)} bytes ')
#     print(f'{dirs} - dir ')
# else:
#     print(f'Файл {file_path} не существует')


# DZ 22 - Обмен местами двух строк в файле

# # Создадим файли закоментируем его
# f = open('text2.txt','w')
# f.write('Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n')
# f.close()

# Считываем данные файла и записываем в переменную
# f = open("text2.txt", "r")
# rl = f.readlines()
# f.close()
#
# # Заменили по индексу вторую строку
# print(rl)
# rl[1] = rl[0] # 'Hello World\n'
# print(rl)
#
# pos = int(input('Введите индекс для замены: '))
# if 0 <= pos < len(rl):
#     rl.pop(pos)
# else:
#     print('Индекс введен не верно')
#
#
# # Только тут перезапишем в самом файле нужный элемент
# f = open("text2.txt","w")
# f.writelines(rl)
# f.close()


# DZ 21 - Вычислить количество отрицательных чисел в массиве(списке)


# def count(lst):
#     if len(lst) == 1:
#         if lst[0] < 1:
#             return 1
#         else:
#             return 0
#     else:
#         if lst[0] < 1:
#             return 1 + count(lst[1:])
#         else:
#             return count(lst[1:])
#
#
# print("count ", count([-2, 3, 8, -11, -4, 6,]))


# DZ 20 - валидация номера телефона
# import re
# st = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 7 (499) 456-45-78'
# print(re.findall( r"(?:(?:8|\+7)[\- ]?)?(?:\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}", st))


# DZ 19 - Найти адрес электронной почты
# import re
# st = '123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru'
# print(re.findall( r"[\w._-]+@[\w._-]+\.[\w.]+", st))


# DZ 18 - дана строка в которой h встречается минимум два раза.
# Разверните последовательность символов,заключенную между первым и последним
# появлением буквы h в противоположном порядке

# s = 'I am lerning Python. hello, WORLD'
# # a = (s[s.find('h')+1:s.rfind('h')])
# # print(a[::-1])
#
#
# s1=s[:s.find('h')]
# s2=s[s.rfind('h'):s.find('h'):-1]
# s3=s[s.rfind('h'):]
# print(s1+s2+s3)


# DZ 17 - даны два числа a = 122, b = 97, где a и b - коды символов.Нужно вывести все символы,
# ASCII- коды которых лежат между
# a и b включительно, в порядке возрастания их кодов

# a = 122
# b = 97
# print(*(chr(x) for x in range(a, b + 1)) if a < b else (chr(x) for x in range(b, a + 1)))

# DZ 16 - Создать функцию,которая находит сумму чисел и декоратор,
# который находит среднее арифметическое этих чисел

# def an(num):
#     def wrap(*args):
#         c = num(*args) / len(args)
#         print('Среднее арифметическое', c)
#
#     return wrap
#
#
# @an
# def ms(*args):
#     a = sum(args)
#     print('Сумма чисел:', a)
#     return a
#
#
# ms(2, 3, 3, 4)

# DZ 15 - Создать лямбда-выражения для нахождения площадей фигур
#
# a = [
#     lambda x, y: x * y,
#     lambda x, y, c: (x + y) * c / 2,
#     lambda x,: 3.14 * x ** 2
#
# ]
#
# print('Прямоугольник', a[0](2, 5))
# print('Трапеция', a[1](7, 5, 3))
# print('Круг', a[2](2))

# DZ 14 - Пользователь вводит данные студентов нужно определить средний балл и вывести данные студентов


# <<<<<<< HEAD
# stu = {}
# n = int(input("Количество студентов: "))
# s = 0
# for i in range(n):
#     sname = input(str(i+1) + "-й студент: ")
#     poin = int(input("Балл: "))
#     stu[sname] = poin
#     s += poin
#
# avrg = s / n
# print("\nСредний балл: %.0f. Студенты с баллом выше среднего:" % avrg)
# for i in stu:
#     if stu[i] > avrg:
#         print(i)
#
#
#
#
# =======
# studs = {}
# n = int(input("Количество студентов: "))
# s = 0
# for i in range(n):
#     sname = input(str(i+1) + "-й студент: ")
#     point = int(input("Балл: "))
#     studs[sname] = point
#     s += point
#
# avrg = s / n
# print("\nСредний балл: %.0f. Студенты с баллом выше среднего:" % avrg)
# for i in studs:
#     if studs[i] > avrg:
#         print(i)
# >>>>>>> 14285a936aef2e2d90ffe640d0ef4f65bc662efe
#
#
# # DZ 13 Найти общую прибыль
# a = ['January', 'February', 'March']
# b = [52000.00, 51000.00, 48000.00]
# c = [46800.00, 45900.00, 43200.00]
# for s, k, m in zip(b, c, a):
#     p = s - k
#     print('прибыль в', m, '=', p)


# DZ 12 Создать новый словарь с именем и зарплатой
# и удалить их из исходного словаря


# a = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# a.clear()
# print(a)

# a = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# d = list(a.items())[1]
# print(d)
# b = a.pop('name')
# c = a.pop('salary')
# print(a)
# a = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
#
# del a['age']
# del a['city']
#
# print(a)


# DZ 11 Посчитать количество гласных букв

# s = input("Введите строку:")
# count = 0
# a = set("а, я, у, ю, о, е, ё, э, и, ы")
# for i in s:
#     if i in a:
#         count += 1
# print('Количество гласных равно:', count)

# DZ 10 выведите статистику частности символов в кортеже - 253523651
# b = input('= ')
# a = tuple(b)
# for x in set(a):
#     print(f'{x} - {a.count(x)}')


# DZ 9 - Заполните один кортеж десятью случайными числами от 0 до 5 включительно.
# Так же заполните второй кортеж числами от -5 до 0.
# Для заполнения кортежей числами напишите одну функцию.
# Объедените два кортежа с помощью +,создав третий кортеж.
# С помощью метода кортежа count() определите в нем кол-во. нулей.
# Выведите на экран третий кортеж и количество нулей в нем

# from random import randint
#
# def slicer():
#     s = tuple(randint(0, 5) for i in range(10))
#     c = tuple(randint(-5, 0) for i in range(10))
#     a = s + c
#     # return a
#     print(a.count(0))
#     return a
#
# print(slicer())


# # DZ 8 функция площади фигур
# from math import sqrt, pi
#
# print("1-прямоугольник, 2-треугольник, 3-круг")
# figure = input("Выберите фигуру: ")
#
# if figure == '1':
#     print("Длины сторон прямоугольника:")
#     a = float(input("a = "))
#     b = float(input("b = "))
#     print("Площадь: %.2f" % (a * b))
# elif figure == '2':
#     print("Длины сторон треугольника:")
#     a = float(input("a = "))
#     b = float(input("b = "))
#     c = float(input("c = "))
#     p = (a + b + c) / 2
#     s = sqrt(p * (p - a) * (p - b) * (p - c))
#     print("Площадь: %.2f" % s)
# elif figure == '3':
#     r = float(input("Радиус круга R = "))
#     print("Площадь: %.2f" % (pi * r ** 2))
# else:
#     print("Ошибка ввода")


# # DZ 7 Заполнить список случайными числами
# import random
#
#
# nums = list(range(10))
#
# random.shuffle(nums)
# print(nums[0:10])


# DZ 6 дан список .
# выведите те его элементы которые встречаются в списке только один
# раз.элементы нужно выводить в том порядке в котором они
# встречаются в списке

# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# for i in range(len(a)):
#     for j in range(len(a)):
#         if i != j and a[i] == a[j]:
#             break
#     else:
#         print(a[i], end=' ')


# # DZ 5 Найти среднее арифметическое всех ненулевых элементов введенного списка
# a = [int(input("->")) for i in range(int(input("Введите количество элементов списка: n = ")))]
# print(a)
# sa = 0
# c = 0
# for i in range(len(a)):
#     if a[i] > 0:
#         c += 1
#         sa += a[i]
#
#
# print(sa / c)


# DZ 4
# a = 5
#
# count = 0
#
# while 0 < a <= 100:
#     user = int(input("Введите число: "))
#     print(user)
#     count += 1
#     if user == a or user == 0:
#         print("Угадали\nколичество попыток", count)
#         if user == 0:
#             print("Конец")
#         break
#
#     elif user > a:
#         print("Число меньше")
#     elif user < a:
#         print("Число больше")


# DZ 3 (18.11.23)
# a = int(input("Число символов: "))
# b = input("Тип символов: ")
# c = int(input("Ориентация строки 0 или 1: "))
# i = 0
# while i < a:
#     if c == 0:
#         print(b, end=" ")
#         i += 1
#     else:
#         print(b, end="\n")
#         i += 1


# DZ 2
# a = 5
# b = 7
# c = 3
# d = a+b+c
# e = a*b*c
# x = (a+b+c)/3
# print("Среднее арифметическое", x)
# print("Произвеление чисел", e)
# print("Сумма чисел", d)
