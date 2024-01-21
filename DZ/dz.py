# DZ 18 - дана строка в которой h встречается минимум два раза.
# Разверните последовательность символов,заключенную между первым и последним
# появлением буквы h в противоположном порядке




# DZ 17 - даны два числа a = 122, b = 97, где a и b - коды символов.Нужно вывести все символы,
# ASCII- коды которых лежат между
# a и b включительно, в порядке возрастания их кодов

a = 122
b = 97
print(*(chr(x) for x in range(a, b + 1)) if a < b else (chr(x) for x in range(b, a + 1)))

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
