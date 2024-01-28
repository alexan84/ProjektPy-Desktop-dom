# print("hello!!!!")
# print("Привет")
import random
import time

#  Урок 2

# 1 вариант
# num = 4325
# print("Исходное число:", num)
# a = num % 10
# print(a) # 5
# num //=10
# b = num % 10
# # print(num) # 432
# print(b)  # 2
# num //= 10
# # print(num)  # 43
# c = num % 10
# print(c)  # 3
# num //= 10
# # print(num)  # 4
# d = num % 10
# print(d)  # 4


# 2 вариант
# num = 4325
# print("Исходное число:", num)
# res = num % 10 * 1000
# print(res)
# num //= 10
# print(num)
# res += num % 10 * 100
# print(res)
# num //= 10
# print(num)
# res += num % 10 * 10
# print(res)
# num //= 10
# print(num)
# res += num % 10
# print(res)


# Конкатенация типов строк приводим либо к сумме или просто сложение строк
# num1 = "2"
# num2 = 3
# res = num1 + str(num2)  # 23
# print(res)
# res1 = int(num1) + num2  # 5
# print(res1)

# num1 = "2.3"
# num2 = 3
# res3 = float(num1) + num2  # 5.3
# print(res3)


# # Метод для чисел после точки
# print(int(3.8))
# print(round(3.895, 2))  # 3.9 потому что 5 округляется до нуля и нольне пишется адолжен
# print(type(round(3.891, 2)))  # class float


# Методы end,sep Именнованные параметры
# name = "Виктор"
# age = 28
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут", name, ".Мне", str(age), "лет.",sep="---", end="     ")
# print("Я учу питон")


# Функция ввода Input
# name = input("Введите имя: ")
# print(name)


# Просим ввести юзера число и преобразуем это число из строки в число
# num = int(input("Введите число:"))
# power = int(input("Введите степень: "))
# res = num ** power
# print("Число", num, "в степени", power, "равно", res)
# print(type(num))


# НЕ явное преобразование типов
# b1 = True
# b2 = False
# print(b1 + 5)  # 1 + 5
# print(b2 + 5)  # 0 + 5

# Явное преобразование типа
# False => "", 0, False, None

# Сравнения приводящие к булевым значениям
# print(7 ==7)
# print(2 + 5 == 7)
# print(7 != 10 - 7)
# print(8 > 5)
# print(8 < 5)
# print((9 <= 9))
# print(9 >= 9)
# print("привет" > "ПРИВЕТ")


# ЛОгические булевые значения
# print(2 < 4 < 9)  # => True && True
# print(2 * 5 > 7 >= 4 + 3)  # True && True => True
# print(3 * 3 <= 7 >= 2)  # False && True => False

# a = 10
# b = 5
# c = a == b
# print(a, b, c)  # 10 5 False


# ЛОгические операторы сравнения
# print(5 - 3 == 2 and 1 + 3 == 4)  # True (True:True)
# print(5 - 3 == 2 and 1 + 3 < 4)  # False (True:False)
# print(5 - 3 > 2 and 1 + 3 == 4)  # False (False:True)
# print(5 - 3 > 2 and 1 + 3 < 4)  # False

# print(5 - 3 == 2 or 1 + 3 == 4)  # True (True:True)
# print(5 - 3 == 2 or 1 + 3 < 4)  # True (True:False)
# print(5 - 3 > 2 or 1 + 3 == 4)  # True (False:True)
# print(5 - 3 > 2 or 1 + 3 < 4)  # False(False:False)

# print(9 - 7)  # 2
# print(not 9 - 7)  # False
# print(not 7 - 7)  # True

# Конструкция if если попадаем в условие то выводим переменную
# cnt = 5
# if cnt < 10:
#     cnt+= 2
#     print(cnt)


# Пример
# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")


# ПРимер
# a = 35
# b = 25
# if a > b:
#     print("a > b")
# elif a < b:
#     print("a < b")
# else:
#     print("a == b")


# Задача на уроке вывод какой получился треугольник

# a = input("Введите a = ")
# b = input("Введите b = ")
# c = input("Введите c = ")
# if a == b == c:
#     print("РАВНОСТОРОННИЙ")
# elif a == b or a == c or b == c:
#     print("Равнобедренный")
# else:
#     print("Разносторонний")


# Вложенные условия
# day = int(input("Введите день недели цифрой: "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5)
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("Понедельник")
#     if day == 2:
#         print("Вторник")
#     if day == 3:
#         print("Среда")
#     if day == 4:
#         print("Четверг")
#     if day == 5:
#         print("Пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("Суббота")
#     if day == 7:
#         print("Воскресенье")
# else:
#     print("Такого дня не существует")


# Урок 3

# * Задача на уроке

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", n ,end=" ")
#     if n == 1:
#         print("ворона")
#     elif 2 <= n <= 4:  # n == 2 or n ==3 or n == 4
#         print("вороны")
#     else:
#         print("ворон")
# else:
#     print("Ошибка ввода данных")

# * match и case, в примере подставляем значения в переменную сами
# password = "user"
#
# match password:
#     case 'admin':
#         print("Администратор")
#     case 'user':
#         print("Пользователь")
#     case _:
#         print("Логин не найден")


# * Пример кейсов на днях недели

# day = "среда"
# time = 15
#
#
# match day:
#     case "понедельник" |  "вторник" | "среда" | "четверг" | "пятница" if 9 <= time <= 16:
#         print("Рабочий день")
#     case "суббота" |  "воскресенье":
#         print("выходной день")
#     case _:
#         print("Такого дня недели не существует или не рабочее время")


# * Тернарные выражения

# a, b = 100, 20
# print(a if a < b else b)
#
# if a < b:
#     print(a)
# else:
#     print(b)


# * вложенный if
# a, b = 10, 10
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# * Задача на уроке - написать прогу деления на ноль

# a, b = 1, 0
# print("на ноль делить нельзя" if b == 0 else a / b)


# * Ошибки ( каждой ошибки соответствует кадое неправильно введеное значение целого числа) - попытаться выполнить код который находится в его блоке,с указанием исключения которое мы здесь обрабатываем
# try:
#     n = int(input("Введите целое число: "))
#     print(n + 2)
# except ValueError:
#     print("Что то пошло не так")
#
# print("Следующая строка")


# * Сразу несколько исключений
# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")


# Другой вариант более короткий
# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки илн Нельзя делить на ноль")
# else:  # когда в блоке try не возникло исключения
#     print("Все нормально вы ввели числа", n, "и", m)
# finally:  # выполнится в любом случае
#     print("Конец программы")


# * Задача на уроке, надо что бы происходила конканатенация и с число + строка и наоборот
# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
# try:
#     n = int(n)  # n = 5
#     m = int(m)  # m = 'два'
# except ValueError:
#     n = str(n)  # n = '5'
# finally:
#     print(n + m)  # '5' + 'два'


# * Циклы - While
#  Выводим от 1 до 5
# i = 0
# while i < 5:
#     print("i =", i)
#     i = i + 1  # i += 1
#
#  Выводим от 10 до 0
# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 1


#  * Задача на уроке, вывести только четные числа от 1 до 20
# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print("i =", i)
#     i += 1


#  * Задача на уроке,выводим количество звездочек указанных числом юзером
# n = int(input("Введите количество символов: "))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1

# Другой вариант задачи в одну строку
# n = int(input("Введите количество символов: "))
# print("*\n" * n)


#  * Задача на уроке, выводим сумму целых нечетных чисел 1 вариант
# a = int(input("Введите начало диапазона: "))  # 5
# b = int(input("Введите конец диапазона: "))  # 10
# res = 0
# while a <= b:  # 5 6 7 8 9 10
#     if a % 2:  # a % 2 != 0
#         res += a
#     a += 1
# print(res)


#  2 вариант
# a = int(input("Введите начало диапазона: "))  # 5
# b = int(input("Введите конец диапазона: "))  # 10
# if a % 2 == 0:  # 5
#     a += 1
# res = 0
# while a <= b:  # 5 < 10
#     print("a =", a)
#     res += a  # res = 0 + 5
#     a += 2  # a = a + 2
# print(res)


# Урок 4

# * Задача на уроке , просим юзера вводить целое число и если он вводит другое значение то создаем исключения
# n = input("Введите целое число: ")
# while type(n) != int:
#     try:
#         n = int(n)  # 7
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число")  # '7'
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")


# * Задача на уроке юзер вводит число  мы пишем четное или нечетное
# n = input("Введите целое число: ")
# while type(n) != int:
#     try:
#         n = int(n) # 7
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")  # 7
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# * Другой вариант задачи только вводим еще и вещественное число (4.2 например)
# n = input("Введите целое число: ")
# while type(n) != int and type(n) != float :
#     try:
#         n = int(n) # 7
#     except ValueError:
#         try:
#             n = float(n)
#         except ValueError:
#             print("Число не целое!")
#             n = input("Введите целое число: ")  # 7
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")


# * Пример Continue и Break
# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершон")


# Пример задаем сразу истину цикл принудительно завершается брейком
# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1


# Пример похожий прога запрашиваетввестибесконечно положительное число пока мы не введем отрицательное(условие выхода)
# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break


# * Задача на уроке- написать прогу поиска произведения последовательности положительных и отрицательных чисел вводимых склавиатуры пока юзер не введет 0
# a = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     a *= n
# print(a)


# ПРимер else в цикле
# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i, end=" ")
#     i += 1
# else:
#     print("\nЦикл окончен, i =, i")


# Вложенные циклы
# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1


# * Задача на уроке .Таблица умножения
# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1


# * Задача на уроке. Вывести прямоугольник из символов
# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("*", end="")
#         j += 1
#     print()
#     i += 1


# * Задача на уроке. Вывести прямоугольник из чередующихся символов
# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print("*", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1


# * Задача на уроке. Вывести диагональ из символов
# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("+")
#     i += 1

# Упрощенный вариант задачи
# i = 0
# while i < 5:
#     print(" " * i, "*")
#     i += 1

# DZ
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


# Цикл For

# * Задача на уроке - юзер вводит целое число - мы выводим всецелые числа на которое заданное число делится без остатка
# a = int(input("Введите целое число"))
# for i in range(1, a +1):
#     if a % i == 0:
#         print(i, end=" ")


# * Задача на уроке - вывести числа от 10 до 100 у которых есть две одинаковые цифры

# for i in range(10, 12):
#     if i % 10 == i // 10:
#         print(i)

# Урок 5

# *  Пример прерываем цикл и else не выполняется
# for i in range(3):
#     if i == 1:
#         break
# else:
#     print("done")


# Пример вложенного цикла for (вложенный постоянно одинаковый)
# for i in range(3):
#     print("*** i=", i)
#     for j in range(2,4):
#         print("--- j=", j)


# * Задача на уроке выводим прямоугольник из символов - ширину и высоту задает юзер
# w = 16
# h = 4
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


# Списки (list)
# nums = [8, 3, 9, 4,  1, "one"]
# print(nums)
# print (type(nums))
#
# print(nums[0])
# print(nums[2])
# # print(nums[6])  #IndexError
#
# nums[1] = 256
# print(nums)
# nums[3] += 100
# print(nums)


# Пример различных действий со списком
# nums = [8, 3, 9, 4,  1, "one"]
# print(nums)
# for i in range(len(nums)):
#     print(nums[i] * 2)


# Создание пустых списков - варианты
# s = []
# print(s)
#
# b = list("He  llo")
# print(b)


# Primer
# print(range(6))
# n = list(range(6))
# print(n)
#
# print(list(range(2, 10)))
# print(list(range(2, 10, 2)))


# Пример for внутри списка,сначало без переменной потом переменной
# a = [0 for _ in range(5)]
# print(a)

# n = 5
# b = [i for i in range(n)]
# print(b)


# юзуер вводит длину списка
# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("->"))
# print(a)


# Укороченный пример
# a = [input("->") for i in range(int(input("Введите количество элементов списка: n = ")))]
# print(a)


# * Primer посчитать в списке сумму всех отрицательных элементов(список вводит юзер)
# a = [int(input("->")) for i in range(int(input("Введите количество элементов списка: n = ")))]
# print(a)
# s = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         s += a[i]
# print("Сумма", s)


# Primer
# a = list(range(10, 100, 10))
# print(a)
#
# for i in range(len(a)):
#     print(a[i], end=" ")
# print()
#
# # другой вариант записи
# for i in a:
#     print(i, end=" ")


# * Задача на уроке - в списке на 20 элементов посчитать количество четных элементов и найти сумму нечетных элементов
# n = list(range(21, 41))
# print(n)
# s = k = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]
#
# print("sum нечетных элементов: ", s)
# print("count четных элементов: ", k)

# второй вариант задачи
# n = list(range(21, 41))
# print(n)
# s = k = 0
# for i in n:
#     if i % 2 == 0:
#         k += 1
#     else:
#         s += i
#
# print("sum нечетных элементов: ", s)
# print("count четных элементов: ", k)


# * Задача на уроке - дан список чиселювыведите все элементы списка которые больше предыдущего элемента
# a = [int(input("->")) for i in range(int(input("Введите количество элементов списка: n = ")))]  # 294635
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")

# Срезы
# замена местами индэксов в списке
# a = [7, 8, 2, 1, 17]
# print(a)
# a[0], a[1] = a[1], a[0]
# print(a)

# Primer срезов
# a = [0, 1, 2, 3, 4, 5]
# print(a[1:4])
# print(a[1:])
# print(a[:3])
# print(a[5:2:-1])
# b = a[10:20]
# print(b)


# Обозначение срезов
# a = list(range(1, 8))
# print(a)
# print(a[::-1])
# print(a[::2])
# print(a[1::2])
# print(a[:1])
# print(a[-1:])
# print(a[3:4])
# print(a[-3:])
# print(a[-3:1:-1])
# print(a[2:5])


# Пример -удаляем 1 и 2 индекси заменяем на 4 нуля
# s = [5, 9, 3, 7, 1, 8]
# print(s)
# s[1:3] = [0, 0, 0, 0]
# print(s)
# # Заменяем 1 индекс на 20
# s[1:2] = [20]
# print(s)
# # Очистим часть списка - удаляем 4.5.6.7 элементы
# s[4:] = []
# print(s)
# # Удаляем нули
# s[2:4] = []
# print(s)


# функция удаления del
# del s[1]
# print(s)


# # Методы списков
# s = [5, 9, 3, 7, 1, 8]
# print(s)
# s.append(99)  # Добавляет один элементв конец списка
# print(s)
# s.extend([1, 2, 3])  # Добавляет список элементов в конец списка
# print(s)
# s.extend('add')  # добавляет строку
# print(s)
# s.insert(1, 100)  # добавлят элемент в список в заданный индекс (не заменяет!)
# print(s)


# Пример юзер создает список
# s = []
# n = int(input("Кол-во элементов в списке: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     # s.append(x)
#     s.insert(0, x)  # меняет местамии последний элементс нулевым
# print(s)


# Задача на уроке юзер вводит число кратное 3
# s = []
# n = int(input("Кол-во элементов в списке: "))
# for num in range(n):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print("число не кратное 3: ")
# print(s)


# Пример найдем область пересечения в списках
# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)


# Другой ваиант задачи выше
# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for elements in a:
#     if elements in b and elements not in c:  # если поменять условия местами код ускорится
#         c.append(elements)
# print(c)


# Задача на уроке - написать функцию которая создает комбинацию двух списков таким образом плюсует элементы поочередно
# a = [1, 2, 3]
# b = [11, 22, 33, 44, 55]
# c = []
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)


# другой вариант - тут не имеет значение какой список длинее
# a = [1, 2, 3,]
# b = [11, 22, 33, 44, 55]
# c = []
# if len(a) > len(b):
#     a, b = b, a
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
# print(c)


# Методы удаления из списков
# s = [5, 9, 3, 7, 1, 9, 9, 8]
# print(s)
# s.remove(9)  # по значению только один элемент
# print(s)
# s.pop()  # удаляет последний элемент из списка
# print(s.pop(1))  # удаляет по индексу и выводит то что удалил
# print(s)
# s.clear()  # Очистка всех элементов списка
# print(s)


# Задача на уроке - дан список из чмсел ииндекс элемента в списке k .Удалите из списка элемент с индексом к сдвинув влево всет элементы стоящие правее от элемента с индексом к
# a = [int(input("->")) for i in range(int(input("Введите количество элементов списка: n = ")))]
# print(a)
# b = int(input("введите индекс для удаления: "))
# a.pop(b)
# print(a)

# Метод считающий количество элементов в списке
# s = [5, 9, 3, 7, 1, 9, 9, 8]
# print(s)
# num = s.count(9)  # выводит количество заданных значений в списке
# print(num)
#
# s = [5, 9, 3, 7, 1, 9, 9, 8]
# print(s)
# ind = s.index(9)  # возвращает номер индекса первого искомого элемента
# print(ind)
# ind = s.index(9, 2)  # начинает поиск нужного индекса с указанного номера индекса
# print(ind)

# s = 82 // 9
# print(s)
# a = 15 // (16 % 7)
# b = 34 % a * 5 - 29 % 5 * 2
# print(a + b)
# a = 82 // 3 ** 2 % 7
# print(a)

# b = 1
# q = 2
# n = 5
# bn = b * q ** (n - 1)
# print(bn)
# c = 12 // 2  #
# b = 12 % 3  # Остаток от деления
# print(c)
# print(b)
# Деление и отбрасывает десяцичную часть
# # Получаем целое число
# print(10 // 3)  # 10 / 3 = 3.33   = 3
# print(10 // 4)   # 10 / 4 = 2.5    = 2
# print(10 // 5)  # 10 / 5 = 2      = 2
# print(10 // 6)   # 10 / 6 = 1.66   = 1
# print(10 // 12)  # 10 / 12 = 0.83  = 0
# print(12 // 10)  # 12 / 10 = 0.83  = 1
# print(-10 // 3)   # -10 / 3 = -3.33 = -4

# Деление с остатком
# Оператор деления с остатком возвращает остаток от
# деления двух целых чисел


# print(16743758 / 5)  # 3348751.6
# print(16743758 % 5)  # 3
# print("Просто деление 16 / 5 =", 16 / 5, "-> Целочисленное деление 16 // 5 =", 16 // 5)  # 3.2
# print("Просто деление 16 // 5 =", 16 // 5, "-> 3 * 5 =", 3 * 5, "Деление с остатком 16 % 5 =", 16 % 5)  # 3.2
# print(124659 % 2)  # 1

# print(3.2 * 5)

# a = 16
# b = 4
# c = 4
# q = 16 / 4
# print("16 / 4 = ", q)
# r = b % c
# print("16 % 4 = ", r)
# a = b * q + r
# print(a)


# print(10 % 3)  # 10 / 3 = 3.33  = 1
# print(10 % 4)  # 10 / 4 = 2.5   = 2
# print(10 % 5)  # 10 / 5 = 2     = 0
# print(10 % 6)  # 10 / 6 = 1.66  = 4
# print(10 % 12)  # 10 / 12 = 0.83 = 10
# print(10 % 20)  # 10 / 20 = 0.5  = 10

# print(1234 // 10)
# print(1234 % 10)

# Задача 1. Напишите программу, определяющую число десятков и единиц в двузначном числе.

# Решение. Число единиц – это последняя цифра числа, число десятков – первая цифра. Чтобы получить последнюю цифру любого числа, нужно найти остаток от деления числа на
# 10
# 10. Чтобы найти первую цифру двузначного числа, нужно поделить число нацело на
# 10
# 10. Программа, решающая поставленную задачу, может иметь следующий вид:
# num = 754
# a = num % 10
# b = (num % 100) // 10
# c = num // 100
#
# print(a)
# print(b)
# print(c)


# num = int(input())
# last_digit = num % 10
# first_digit = num // 10
#
# print('Число десятков =', first_digit)
# print('Число единиц =', last_digit)

# Задача 2. Напишите программу, в которой рассчитывается сумма цифр двузначного числа.
# num = int(input())
# last_digit = num % 10
# first_digit = num // 10
#
# print('Сумма цифр =', last_digit + first_digit)

# Задача 3. Напишите программу, которая печатает число, образованное при перестановке цифр двузначного числа.

# Решение. Программа, решающая поставленную задачу, может иметь следующий вид:

# num = int(input())
# last_digit = num % 10
# first_digit = num // 10
#
# print('Искомое число =', last_digit * 10 + first_digit)


# Задача 4. Напишите программу, в которую вводится трехзначное число и которая выводит на экран его цифры (через запятую).

# 456Решение. Программа, решающая поставленную задачу, может иметь следующий вид:
#
# num = int(input())
# digit3 = num % 10
# digit2 = (num // 10) % 10
# digit1 = num // 100
#
# print(digit1, digit2, digit3, sep=',')

# n = 1234
# #
# # print(n // 10000)
# print(n % 10000 // 1000)
# print(n % 1000 // 100)
# print(n % 100 // 10)
# print(n % 10)

# a = 17 // (23 % 7)
# b = 34 % a * 5 - 29 % 4 * 3
# print(a * b)


# num1, num2, num3 = int(input()), int(input()), int(input())
# counter = 0  # переменная счётчик
# if num1 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# if num2 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# if num3 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# print(counter)

# i = 1
#
# if i / 2:
#     print(i, 'чётное')
# else:
#     print(i, 'нечётное')
#
# if i // 2:
#     print(i, 'чётное')
# else:
#     print(i, 'нечётное')
#
# if i % 2 == 0:
#     print(i, 'чётное')
# else:
#     print(i, 'нечётное')
# if i // 2 == 0:
#     print(i, 'чётное')
# else:
#     print(i, 'нечётное')
# if i % 2 != 0:
#     print(i, 'нечётное')
# else:
#     print(i, 'чётное')
# if i // 2 != 0:
#     print(i, 'нечётное')
# else:
#     print(i, 'чётное')

#
# a = int(input())
# n1 = a // 1000
# n2 = (a // 100) % 10
# n3 = (a % 100) // 10
# n4 = a % 10
# print(n1)
# print(n2)
# print(n3)
# print(n4)


# Урок 7

# Переменные приравнивания
# a = [1, 2, 3]
# b = a
# print('a =', a)
# print('b =',b)
# a.append(20)
# print('a =', a)
# print('b =',b)
# b.append(120)
# print('a =', a)
# print('b =',b)

# Метод Пример копирования переменной copy

# a = [1, 2, 3]
# b = a.copy()
# print('a =', a)
# print('b =',b)
# a.append(20)
# print('a =', a)
# print('b =',b)
# b.append(120)
# print('a =', a)
# print('b =',b)

# Метод разворачивающий список задом на перед
# a = [1, 2, 3, 4, 5,]
# print(a)
# a.reverse()
# print(a)

# Метод сортировки списка
# a = [2,4,1,7,4]
# a.sort()
# print(a)
# a.sort(reverse=True)  # сортирует список и выводит его в обратном порядке по убыванию
# print(a)

# Метод Сортировка строковоых значений
# По алфавиту
# a = ['Виталий', 'Сергей', 'Александр', 'Дима']
# a.sort()
# print(a)

# Сортировка По длине и можно в обратном порядке
# a = ['Виталий', 'Сергей', 'Александр', 'Дима']
# a.sort(key=len,reverse=True)
# print(a)


# a = [1, 2, 3, 4, 5,]
# print(a)
# a.sort()
# print(a)
#
# sort = sorted(a, reverse=True)
# print(a)


# Генерация случайных данных

# import random
#
# print(random.random())
# print(random.randint(3, 9))  # 9 включается
# print(random.randrange(8, 9))  # 9 не включается
#
# print(random.uniform(10.5, 25.5))
# print(round(random.uniform(10.5, 25.5), 2))

# Метод выбора случайного города или числа

# city_list = ["москва", "новосибирск", "воронеж", "сочи", "екатеренбург"]
# print(random.choice(city_list))
# print(random.choices(city_list, k=3))
#
# # Перемешать элементы внутри списка
# random.shuffle(city_list)
# print(city_list)
#
# n = [2, 5, 4, 8, 1,4,1,9,0,5,43,6]
# print(random.choice(n))
# print(random.choices(n, k=5))

# Полезные встроенные функции

# lst = [5,3,8,7,1]
# print(len(lst))
# print(sum(lst))  # не работает со строками
# print(max(lst))
# print(min(lst))

# Генерация случайных чисел и формирование списка из них.от 0 до 20 .кол-во чисел 10
# import random
# mas = [random.randint(0,10) for i in range(10)]
# print(mas)

# * Задача на уроке заполнить список из 10 элементов числами.Найти
# максимальный элемент и поместить его в начало
# import random
# mas = [random.randint(0,20) for i in range(10)]
# print(mas)
# c = (max(mas))
# print(c)
# mas.remove(c)
# mas.insert(0,c)
# print(mas)

# * Задача на уроке заполнить список из 10 элементов случайными числами.удалить
# все элементы расположенные перед минимальным элементом списка

# lst = [random.randint(0,20) for i in range(10)]
# print(lst)
#
# min_ch = min(lst)
# print('min',min_ch)
#
# ind_ch = lst.index(min_ch)
# print('index min',ind_ch)
#
# del lst[0: ind_ch]
#
# print(lst)


# Проверка в списке наличия какого то элемента с помощью in

# a = list('1g3j4hgj67')
# print(a)
# print('9' in a)
# print('h' in a)
#
# print('9' not in a)
# print('h' not in a)

# Прверка пустой список или нет

# lst = [1]
# print(bool(lst))
# if len(lst) == 0:  # 1 вариант записи
# # if not lst:  # 2 вариант
#     print('Список пустой')
# else:
#     print("В списветесть элементы")


# * Задача на уроке - даны два списка - надо
# создать три списка заполняя их в определеном порядке

#
# import random
#
# n1 = int(input('Введите размер первого списка: '))
# n2 = int(input('Введите размер второго списка: '))
# a = [random.randint(0,10) for i in range(n1)]
# b = [random.randint(0,10) for j in range(n2)]
# print('Первый список: ', a)
# print('Второй список: ', b)
# # из двух создаем один общий список
# c = a + b
# print('Третий список общий из двух', c)
#
# # из двух создаем один общий список без повторений
#
# d = []
# for element in a:
#     if element not in d:
#         d.append(element)
# for element in b:
#     if element not in d:
#         d.append(element)
# print('Третий список - Замена обоих элементов списка без повторений:',d)
#
# # 4 список содержащий общие элементы из 1 и 2 списков
#
# c =[]
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
# print('4 список -  Общие элементы для двух списков:',c)
#
# # 5 список из мин и макс значений каждого из списков
#
# x = [min(a),min(b),max(a),max(b)]
# print('min и max:',x)


# Вложенные списки
# m = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]
#
# # или строковый список
# m = ['Hello', 'World']
#
# print(m)
# print(len(m))
# print(m[0][0])


# Пример выведем в читабельный вид то что написанно в списке
# m = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]
# print(m)
# print()
# for row in range(len(m)):  # в row попадают 3 элемента списка
#     for col in range(len(m[row])):  # достаем из каждого из трех элементов их собственные элементы
#         print(m[row][col], end='\t')
#     print()

# другой вариант этого примера тобишь цикла
# for row in m:
#     for x in row:
#         print(x,end='\t')
#     print()


# Урок 8
# Пример циклов в одну строку и расписанный
# w,h =4,3
# # matrix = [[0 for x in range(w)] for y in range(h)]
#
# matrix = []
# for y in range(h):
#     new_row = []
#     for x in range(w):
#         new_row.append(0)
#     matrix.append(new_row)
# print(matrix)

# import random
# w, h = 4, 3
# matrix = [[random.randint(1,30) for x in range(w)] for y in range(h)]
#
# m = 0
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()


# Распаковка вложенных списков
# for x,y in [[1,2],[3,4],[5,6],[7,8]]:
#     print(x,'+',y,'=',x + y)


# w, h = 4, 3
# matrix = [[input('->') for x in range(w)] for y in range(h)]
# print(matrix)

# Математический модуль
# import math
#
# num1 = math.sqrt(4)
# num2 = math.ceil(4.2)
# num3 = math.floor(4.8)
# print(num1)
# print(num2)
# print(num3)
# print(math.pi)


# Импорт выборочных модулей и переименование если название длинное
# import math as m
# from math import sqrt,ceil
# from math import *  # То же сао что и выше - импорт всего и можно писать укороченно
#
#
# num1 = sqrt(4)
# num2 = ceil(3.1)
#
# print(num1)
# print(num2)


# Модуль времени
#
# import time
# import locale
#
# locale.setlocale(locale.LC_ALL, 'ru')
#
# second = time.time()
# print(second,'секунды')
#
# local_time = time.ctime()
# print(local_time,'местное время')
#
# res = time.localtime()
# print(res)
# print(res.tm_year)
# print(res.tm_year,'.',res.tm_mon,'.',res.tm_mday,sep='')
#
# print(time.strftime('today is %B %d,%Y'))
# print(time.strftime('сегодня %B %d,%Y'))
#
# print(time.strftime('%d\%d.%Y, %H:%M;%S,', time.localtime()))

# Пример с остановкой проги на 5 сек и ниже с целым числом
# stsrt = time.time()
# time.sleep(5)
# finish = time.time()
# res = finish - stsrt
# print(res)

# stsrt = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - stsrt
# print(res)


# *** Функция

# def hello(name):
#     print('hello', name)
#
#
# hello('igor')
#
# hello('irina')


#
# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x,y)
# get_sum('asd', 'rty')


# * Задача на уроке функция вывода на экран линии из чередующихся символов заданной длинны(функция которая принимает
#  три параметра но не возвращает никакого значения

# def symbol(count,a,b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end='')
#         else:
#             print(b, end='')
#     print()
#
#
# symbol(9,'+','-')
# symbol(7,'X','O')


# def get_sum(a, b):
#     print('сумма: ', end='')
#     return a + b
#
#
# x = 2
# y = 5
# res = get_sum(x,y)
# print(res)


# Пример проверяем числа и возвращаем блольшее и найти их роазность или сумму

# def maximum(one, two):
#     if one > two:
#         print('raznost ',end='')
#         return one - two
#     else:
#         print('summa ',end='')
#         return one + two
#
#
# print(maximum(9, 16))

# Задача на уроке - вывести куб всех чисел от 1 до 10
# (функция которая принимает один параметр и возвращает значение

# def cube(a):
#     return a ** 3
#
#
# for i in range(1,11):
#     print(i,'v kube =', cube(i))

# * Задача на уроке - написать функцию которая принимает список
# и меняет местами его первый и последний элемент.
# в исходном списке минимум 2 элемента

# 1 variant

# def change(lst):
#     symbol1 = lst.pop(0)
#     symbol2 = lst.pop()
#     lst.append(symbol1)
#     lst.insert(0,symbol2)
#     return lst
#
#
#
# print(change([1,2,3]))
# print(change([9,12,33,54,105]))
# print(change(['с','л','о','н']))

# 2 variant создаем элементы с индексом из списка и меняем их местами

# def change(lst):
#     lst[0],lst[-1] = lst[-1], lst[0]
#     return lst
#
#
# print(change([1,2,3]))
# print(change([9,12,33,54,105]))
# print(change(['с','л','о','н']))

# Функции с булевыми значениями

# def is_greater(x,y):
#     if x > y:
#         return True
#     else:
#         return False
#
# a = 10
# b = 5
# print(is_greater(a,b))
# print(is_greater(5,10))
#
# if is_greater(a,b):
#     print(a,'bolwe',b)


# * Задача на уроке функция провекрки надежности пароля

# def check_pass(passw):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in passw:
#         if 'A' <= ch <= 'Z':
#             has_upper = True
#         elif 'a' <= ch <= 'z':
#             has_lower = True
#         elif '0' <= ch <= '9':
#             has_num = True
#
#     if len(passw) >= 8 and has_upper and has_lower and has_num:
#         return True
#
#     return False
# p = input('vvedite passw: ')
# if check_pass(p):
#     print('vernui')
# else:
#     print('ne vernui')


# Типы аргументов у функций


# Передача аргументов в функцию или значения по умолчанию справа на лево

# Именнованый параметр

# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d  # 1+5+0+2
#                           # 1+5+2+1
#
# print(get_sum(1, 5, 2,7))
# print(get_sum(1, 5, 2,))  # 9
# print(get_sum(1, 5, ))
# print(get_sum(1, 5, d=2))  # 8

# задача на урокенаписать функцию которая имеет количество символов = 20 и символ "-"
# в качестве аргументов по умолчанию и выводит на экран набор произвольных символов заданной длины

# def set_param(c=20, s='-'):
#     print(s * c)
#
#
# set_param()
# set_param(7)
# set_param(5, '*')
# set_param(s='#')


# Задача на уроке функция принимает число и вычисляет сумму четных чисел и нечетных чисел

# def digit_sum(n, even=True):
#     s = 0
#     while n > 0:
#         current = n % 10
#         if even and current % 2 == 0:
#             s += current
#         if not even and current % 2:
#             s += current
#         n //= 10
#     return s
#
#
# print('сумма четных чисел')
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
# print('\nсумма нечетных чисел')
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))


# Особенности именованных параметров

# def display_info(name,age):
#     print('Name:', name,'Age:', age)
#
# display_info('ira', 23)
# display_info(23,'ira',)
# display_info(age = 23,name='ira')
# display_info("igor", age=23, name="ira")


# Урок 9

# Изменяемые и неизменяемые объекты
# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(id(lt1))
# print(id(lt2))
# print(lt1 == lt2)  # True
# print(lt1 is lt2)  # False
#
# a = 'Hello'
# b = 'Hello'
# print(id(a))
# print(id(b))
# print(a == b)  # True
# print(a is b)  # True
#
# n = 5
# m = 5
# print(id(n))
# print(id(m))
# print(n == m)  #True
# print(n is m)  #True

# Тип данных кортеж - это неизменяемый список (тип данных)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = (5,)  # создать кортеж можно со скобками или без но обязательно  запятой например - 5,
# b = tuple()
# print(type(a))
# print(type(b))
# print(a)
# print(b)

# n = ['hello', 'python']
# b = tuple(n)
# print(type(b))
# print(b)

# a = (1, 2, 3, 4, 5, 6)
# print(a)
# print(a[3])  # 4
# print(a[1:3])  # (2,3)
# a[1] = 3  # не работает, ошибка

# from random import randint
#
# # s = tuple(int(input('->')) for i in range(5))
# s = tuple(randint(0, 100) for i in range(5))
# print(s)


# Задачана уроке - заполнить кортеж из 12 элементовстепенями
# двойки от 1 до 12
# s = tuple(2 ** i for i in range(1, 13))
# print(s)


# Операции с кортежами

# t1 = tuple('hello')
# t2 = tuple('world')
# print(t1)
# print(t2)
# t3 = t1 + t2
# print(t3)
# # print(t1 * 2)
#
# # print(t3.count('l'))
# # if 'e' in t3:
# #     print(t3.index('e'))
#
# for i in t3:
#     print(i, end=' ')

# Задача на уроке - ищем совпадение одного символа кортежа в другом кортеже и выводим новый кортеж с от искомого элемента и до конца кортежа

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#               # a = tpl.index(el)  # 1
#               # b = tpl.index(el,a +1) + 1 # 4 + 1
#               # return tpl[a:b]
#             return tpl[tpl.index(el):tpl.index(el, tpl.index(el) + 1) + 1]
#         else:
#             return tpl[tpl.index(el):]  # tpl[2:]
#     else:
#         return tuple()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# Пример измиеняемости в кортеже данных
# t = (10,11,[1,2,3],[4,5,6],['hello','world'])
# print(t,id(t))
# t[4][0] = 'new'  # не чего не произойдет
# t[4].append('hi')
# print(t, id(t))


# Распаковка кортежа
# t = (1,2,3)
# # пример 1
# # x = t[0]
# # y = t[1]
# # z = t[2]
# # Пример 2
# x,y,z = t
# print(x,y,z)


# Распаковка данных из функции с помощью кортежа

# def get_uzer():
#     name = 'tom'
#     age = 22
#     is_married = False
#     return name,age,is_married
#
#
# # user = get_uzer()
# # # primer 1
# # print(user[0])
# # print(user[1])
# # print(user[2])
# # # primer 2
# # firs_name,year,married = user
# # primer 3
# firs_name,year,married = get_uzer()
# print(firs_name,year,married)


# Урок 10 - как изменить элементы в кортеже
# что бы перезаписать кортеж переделываем его в список меняем данные и обратно в кортеж
# tpl = (1,2,3,4,5,6)
# print(tpl)
# lst = list(tpl)
# print(lst)
# ptl1 = tuple(lst)
# print(ptl1)
# # можем удалить кортеж и будет ошибка при его вызове в принт
# del ptl1
# print(ptl1)


# Вложенные кортежы, создадим вложеный кортеж и пройдемся в цикле по нему

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
# print(countries, end="\n\n")
#
#
# for country in countries:
#     country_name, country_population, cities = country
#     print('\nСтрана:',country_name,'Население =',country_population)
#     for city in cities:
#         city_name,country_population = city
#         print('\tГород',country_name,'Население =', country_population )


# Урок 11 Множество (set) не упорядочный коллектионный тип данных который хронит только уникальные значение
# то есть одинаковые значения он просто напросто удаляет

# s = {'banana','apple','orange','banana','apple'}
# print(s)
# print(type(s))
# print(len(s))


# Создать пустое множество, со списками и кортежами работает одинаково - лишнее удаляет


# a = set('hello')
# print(a,type(a))

# c = ['red','blue','green',"red"]
# a = set(c)
# print(a,type(a))


# c = ('red','blue','green',"red")
# a = set(c)
# print(a,type(a))


# можем создать множество с помощью цикла в одну строку

# тут пример выводит только четные числа из множества
# mas = [1,2,3,4,4,5,5,2]
# s = {x for x in mas if x % 2 == 0}
# print(s)


# Задача на уроке - на вход функция получает строку или список чисел,преобразуйте их в множество,
# на выходе должно получится множество и количество элементов в нем

# def to_set (element):
#     st = set(element)
#     return st,len(st)
#
# print(to_set('y stroka'))
# print(to_set([4,5,4,8,7,7,77]))


# t = {'red','green','blue'}
# print('green' not in t)
# for i in t:
#     print(i)
#

# for in - особенности работы конструкции

# # проверим букву а в нашем множестве и если нет то выводим все без нее
# r = ['ab_1','ac_2','bc_1','bc_2']
# a = [i for i in r if 'a' not in i]
# print(a)


# найдем и запишем в верхнем регистре  a и  b
# r = ['ab_1','ac_2','bc_1','bc_2']
# a = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r]
# print(a)


# тут изменения будут только там где есть с
# r = ['ab_1','ac_2','bc_1','bc_2']
# a = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c']
# print(a)


# Добавление в множество элемента  и удаление

# a = {'tom','bob','alice'}
# print(a)
# a.add('ann')
# print(a)
# a.remove('ann')  # если обращении к несуществующему элементу ошибка KeyError
# print(a)
# user = 'tom'
# if user in a:
#     a.remove(user)
# print(a)

# есть м6етод для удаления без исключений

# a = {'tom','bob','alice'}
# print(a)
# a.add('ann')
# print(a)
# a.discard('ann1')
# print(a)

#  удаляем первый элемент ,но если указать название то удалится указанный элемент
# a = {'tom','bob','alice'}
# print(a)
# a.add('ann')
# print(a)
# n = a.pop()
# print(n)
# print(a)
# a.clear()  # удалить в множестве все элементы
# print(a)


# Операции с множествами

# объеденение
# a = {0,1,2,3}
# b = {4,3,2,1}
# c = a.union(b)
# # или аналог метода знак |
# v = a | b
# a |= b
# print(c)
# print(v)

# возвращает одинаковые пересечения множеств
# a = {0,1,2,3}
# b = {4,3,2,1}
# c = a & b
# # или через знак
# a &= b
# print(a)
# print(c)

#  возвращает то что есть в одном множестве но нет в другом
# a = {0,1,2,3}
# b = {4,3,2,1}
# c = a - b
# a -= b
# print(c)
# print(a)


# выводит из первого множ-а. то чего нет во втором и наоборот
# a = {0,1,2,3}
# b = {4,3,2,1}
# c = a ^ b  # a ^= b
# print(c)


# Задача на уроке дан набор множеств,
# нужно найти кол-во уникальных элементов и найти мин и макс элементы среди них


# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# # s = s1.union(s2,s3,s4,s5,s6,s7)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# count = len(s)
# print('count',count)
# print('min',min(s))
# print('max',max(s))
# print('sum',sum(s))


# Задача на уроке - найти общие буквы

# s1 = set('Hello')
# s2 = set('How are you')
# a = s1 & s2
# print(a)
# # что бы избавится от скобок и запятых пройдемся в цикле
# for i in a:
#     print(i,end=' ')


# Задача на уроке - определить кто чем занимается


# drawing = {'marina','geny','sveta'}
# music = {'kosty','geny','ily'}
#
# one_hobby = drawing ^ music
# print('один кружок',* one_hobby)
#
# both_hobbies = drawing & music
# print('оба кружка', * both_hobbies)
#
# drawing = drawing - both_hobbies
# # drawing -= both_hobbies
# print('рисование', drawing)


# подмножества пример
#
# a = {0,1,2,3,4}
# b = {3,2,1}
# print(a <= b)  # False
# print(a >= b)  # True


# Тип frozenset - замораживание

# s = frozenset([1,2,3,4,5])
# print(s)
# print(type(s))
# a = frozenset({'hello','world'})
# print(a)


# из списка преобразуем множество

# a = [8,9,7,4,5,8,7,9,4,6,5,1,3,2,5]
# print(a)
# b = set(a)
# print(b)
# a = tuple(b)
#
# print(a)


# -----------------------------------Урок 12 Словарь-------(dict)

# lst = [1,2,3]
# d = {'one':1,'two':2,'three':3,4:'four'}
# lst[0]=100
# print(lst[0])
# d['one']=10
# print(d['one'])
# print(d[4])


# Пустой словарь два синтаксиса записи

# d = {'one':1,'two':2,'four':'four'}
# print(d)
# print(type(d))
#
# d1= dict(one=1,two=2,four='four')
# print(d1)
# print(type(d1))


# Типы данных ключи в словаре ---- ключи в словаре могут быть только неизменяемые типы данных
# тру и фалс приравниваются к 1 и 0.

# d = {0:1,'two':2,(1,2.3):'кортеж',True:[2,3,6,7],1:45,False:(1,2)}
# print(d)


# обращение к ключам и их содержимому
#
# d = {0:1,'two':2,(1,2.3):'кортеж',True:[2,3,6,7]}
# print(d)
# print(d[True][1])
# print(d[(1,2.3)])
# print(d['two'])
# print(d[0])


# переделаем кортеж в словарь появится двоеточие

# lst = (('one', 1), ('two', 2), ('tree', 3))
# d = dict(lst)
# print(d)


# выводим числа в степени
# d = {a: a ** 2 for a in range(7)}
# print(d)


# выполним проверку на наличие ключа в словаре и выведем на экран,
# так же проведем удаление элемента создав условие  на случай если ключ введен неверно
# (что бы удалять только искомый ключ)

# d = {'one': 1, 'two': 2, 'four': 4}
# # print('one' in d)
# key = 'four1'
#
# # if key in d:
# #     del d[key]
#
# try:
#     del d[key]
# except KeyError:
#     print('элемента с ключом ' + key + ' нет в словаре')
#
#
# for i in d:
#     print(i, '->',d[i])


# Задача на уроке дан словарь с числами - нужно перемножить и вывести на экран

# a = {'x1': 3, 'x2': 7, 'x3': 5, 'x4':-1}
#
# comp = 1
# for key in a:
#     comp *= a[key]
# print('proizvedenie', comp)


# Задача на уроке - юзер вводит список овощей,мы сохраняем их с числовыми индексами
# нужно вывести и удалить не нужное,

# d = dict()
# d[1]=input('->')
# d[2]=input('->')
# d[3]=input('->')
# d[4]=input('->')
#
# d = {i: input('->') for i in range(1, 5)}
# print(d)
# dislike = int(input('какой элемент исключить '))
# del d[dislike]
# print(d)

# сумирование ключей
# a = {3: 'x1', 7: 'x2', 5: 'x3', -1: 'x4'}
# print(sum(a))


# Задача на уроке - дано товары с ценами юзер вводит номер товара и количество

# goods = {
#     '1': ['Core -i3-4330', 9, 4500],
#     '2': ['Core -i5-4670k', 3, 8500],
#     '3': ['AMD FX-4330', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core -i5-3450', 5, 6400],
# }
#
# for i in goods:
#     print(i, ') ', goods[i][0], '-', goods[i][1], 'шт. по', goods[i][2], 'руб', sep='')
#
# while True:
#     n = input('№: ')  # '2'
#     if n != '0':
#         if n in goods:
#             gty = int(input('Количество: '))  # 8
#             goods[n][1] += gty  # goods['2'][1] = 8
#         else:
#             print('не коректныйномер товара')
#     else:
#         break
#
# for i in goods:
#     print(i, ') ', goods[i][0], '-', goods[i][1], 'шт. по', goods[i][2], 'руб', sep='')


# Методы работы со словарем

# d = {'a': 1, 'b': 2, 'c': 3, }
# print(d.keys())  # ключи
# print(d.values())  # значения
# print(d.items())  # ключи и значения

# for i, j in d.items():
#     print(i, '->', j)
#
# print(list(d.items()))


# Копирование словаря
# d = {'a': 1, 'b': 2, 'c': 3, }
#
# d2 = d.copy()
#
# print('d:', d, id(d))
# print('d2:', d2, id(d2))
#
# d2['a'] = 5
# d['e'] = 7
#
# print('d:', d, id(d))
# print('d2:', d2, id(d2))
#
# # Очистка словаря
# d.clear()
# print('d:', d, id(d))
# print('d2:', d2, id(d2))


# d = {'a': 1, 'b': 2, 'c': 3}
# # print(d['e'])  # ошибка
# value = d.get('m','такого ключа нет')
# value1 = d.get('b','такого ключа нет')
# print(value)
# print(value1)


# Возможность удаления из словаря каких то элементов
# d = {'a': 1, 'b': 2, 'c': 3, }
# item = d.pop('a','нет ключа такого')  #  выводит удаляемый элемент,Если ввести не существующий ключ выведится сообщение
# print(item)
# print(d)


# Берем пару ключ - значение и удаляем
# d = {'a': 1, 'c': 3, 'b': 2, }
# item = d.popitem()  # удаляет последний элемент
# print(item)
# print(d)


# ---------------------------- Урок 13   ------------------------------

# Соеденим словари

# d = {'a': 1, 'c': 3, 'b': 2, }
# d1 = {'r':7,'q':40}
# d.update(d1)
# # Добавим список
# d2 = [('a', 20), ('b', 9)]
# d.update(d2)
# print(d)


# Задача на уроке соеденить два словаря в третий

# Методом
# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# # new_dict = x.copy()
# # new_dict.update(y)
# # С помощью оператора
# new_dict = x | y
# print(new_dict)


# Вложенные словари

# a = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'second': {
#         4: 'four',
#         5: 'five'
#     }
# }
# print(a)
# print()
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, ': ', a[x][y], sep='')


# Работа с вложенными структурами данных

# Задача на уроке юзер вводит имя и регион из предложенного в словаре
# а мы выводим его продажи и меняем на новое вводимое значение

# sales = {
#     'john': {'n': 3056, 's': 8463, 'e': 8441, 'w': 2694},
#     'tom': {'n': 4832, 's': 6786, 'e': 4737, 'w': 3613},
#     'anne': {'n': 5239, 's': 4802, 'e': 5820, 'w': 1859},
#     'fiona': {'n': 3904, 's': 3645, 'e': 8821, 'w': 2451}}
#
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print('\t', y, ': ', sales[x][y], sep='')
# person = input('Имя: ')
# region = input('Регион: ')
# print(sales[person][region])
# new_data = int(input('Новое значение: '))
# sales[person][region] = new_data
# print(sales[person])


# Генереаторы словарей

# d = {'n': 3056, 's': 8463, 'e': 8441, 'w': 2694}
# d = {value: key for key, value in d.items()}
# print(d)


# Задача на уроке из словаря вывести только два первых значения
#
# d = {'n': 1, 's': 2, 'e': 3, 'w':4}
# for key,value in list(d.items())[:2]:
#     print(f'{key}: {value}')


# Задача на уроке -преобразовать список в словарь
# (строки ключи и числа значения) - работает только если первое значение является строкой

# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]

# Создаем словарь или функцией или просто фигурные скобки
# d = dict()  # {}
# current_key = ''
# for item in a:
#     if type(item) == str:
#         d[item] = []
#         current_key = item
#     else:
#         d[current_key].append(item)
# print(d)


# создаем словарь из списков ключей и значений функцией zip
# двумя способами

# d = dict(zip([1,2,3],['one','two','three']))
# print(d)
# # или наоборот значения -  ключа и значения
# a = [1,2,3]
# b = ['one','two','three']
# f = {k: v for k, v in zip(b, a)}
# print(f)

# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d)
# # или наоборот значения - ключа и значения
# a = [4, 5, 6]
# b = ['one', 'two', 'three']
# f = {k: v for k, v in zip(b, a)}
# print(f)


# тут zip  работает со всеми типами одинаково
# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# d = [4.5,7.4,9.6]
# c = tuple(zip(a,b))
# c = list(zip(a,b))
# c = set(zip(a,b))
# c = dict(zip(a,b))
# c = list(zip(a,b,d))
# print(c)


# Обработка словарей у которых могут быть одинаковые ключи,
# соеденим два словаря взяв у них одинаковые ключи
# по очереди выведем элементы из этих словарей

# d_one = {'name': 'Igor', 'last_name': 'Petrov', 'job': 'Consultant'}
# d_two = {'name': 'Irina', 'last_name': 'Irisova', 'job': 'Manager'}
#
# for (k1,v1), (k2,v2) in zip(d_one.items(), d_two.items()):
#     print(k1,'->',v1)
#     print(k2,'->',v2)

#
# d = [(1, 'one'), (2, 'two'), (3, 'three')]
# a, b = zip(*d)
# print(a)
# print(b)


#
# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# d = list(zip(a,b))
# print(d)
# d.sort()
# print(d)
# print(dict(d))


# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# d = dict(zip(a, b))
# print(d)
# s = sorted(d.items())
# print(s)
# print(dict(s))


# Распакуем два словаря и поместим их в другой словарь двумя способами


# one = {'apple': 0.45, 'orange': 0.35, 'pepper': 0.7}
# two = {'pepper': 0.2, 'onion': 0.55}
# print({**one, **two})
# print({**two, **one})
#
# for k, v in {**two, **one}.items():
#     print(k, '->', v)


# Пронумируем элементы с помощью цикла в двух вариантах

# data = ['red', 'green', 'blue']
# num = 1
# for val in data:
#     print(num, ') ', val, sep='')
#     num += 1
#
# print()
#
# for num, val in enumerate(data, 1):
#     print(num, ') ', val, sep='')

# Распаковка двух списков
# a = [1,2,3]
# b = [*a,4,5,6]
# print(b)


# #
# def func (*args):
#     return args
#
# print(func(2))
# print(func(2,3,4,'abc'))
# print(func())


# Посчитаем количество элементов
# def summa(*params):
#     res = 0
#     for i in params:
#         res+=1
#     return res
#
# print(summa(1,2,3,4,5,6,7,8,9))
# print(summa(3,4,5))


# Задача на уроке -т написать функцию принимающую аргументы и создать словарь
# в котором каждый элемент и ключ и значение

# def to_dict(*args):
#     return {el: el for el in args}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('grey', (2, 17), 3.11, -4))


# def func(a,*args):
#     return a,args
#
# print(func(1))
# print(func(1,2,3,4,56,))


# Пример - выводим имя студента и его оценки в цикле ,если они у него есть


# def p_s(student, *scores):
#     print('Student Name:', student)
#     for score in scores:
#         print(score)
#
#
# p_s('irina', 5, 4, 4, 5, 3, 2)
# p_s('igor', 1, 2, 3, 4, 5)
# p_s('lew')


# Пример функциии которая принимает словарь и
# что то становится ключем а что то значением

# def func(**kwargs):
#     return kwargs
#
# print(func(a=1,b=2,c=3))
# print(func())
# print(func(d=9))


# primer

# def intro(**data):
#     for k, v in data.items():
#         print(k, '->', v)
#     print()
#
#
# intro(name='irina', surname='reznikova', age=22)


# Задача на уроке - создать функцию принимающую неограниченное количество параметров
# и обновляет существующий словарь,словарь обновляется при каждом вызове функции
# словарь напишем внизу функции

# def db(**kwargs):
#     my_dict.update(kwargs)
#
#
# my_dict = {'one': 'first'}
# db(k1=22, k2=32, k3=45, k4=91)
# print(my_dict)


# Пример функции принимающей списки,кортежи,именованный и
# позиционные параметры и выводящия все это в словарь


# Области видимости

# name = 'Tom'
# def hi():
#     global name
#     surname = 'semenov'
#     print('hello',name,surname)
#
#
# def bye():
#     print('good bye',name)
#
# hi()
# bye()
# print(name)
# print(id)


# *
# i = 5
#
# def func(arg=i):
#     print(arg)
#
# i=6
# func()


# *
# x = 4


# def add_file(a):
#     # x = 2
#
#     def add_some():
#         # x = 3
#         print('x=', x)
#         return a + x
#
#     return add_some()
#
#
# print(add_file(5))


# * Ошибка
# sum = 5
#
# lst = [1,2,4,63]
# print(sum(lst))


# * так вводить нельзя
# import builtins
#
# name = dir(builtins)
#
# for t in name:
#     print(t)


# ----------------------------    Урок 15

# Принцип работы вложенных функций

# def outer(who):
#     def ineer():
#         print('hello,', who)
#
#     ineer()
# outer('world')


# Еще пример области видимости

# def func():
#     a = 6  # 2
#
#     def func1(b):  # b = 4
#         a = 4  # 6
#         print(a + b)  # 6  # 4 + 4 = 8
#
#     print('a', a)  # 3  # a = 6
#     func1(4)
#
#
# func()


# Создадим глобальную переменную за пределами функции


# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30  # 35
#
#     def inner():
#         nonlocal a
#         a = 35
#         print('a',a)
#
#     inner()
#     t = a
#
#
# fn()
# c = x + t  # 25 + 30 = 55  # 25 + 35 = 60
# print(c)


# Еще пример nonlocal нужна что бы вывести переменную на уровень выше

# x = 5
#
# def fn1():
#     x = 25  # 2
#
#     def fn2():
#         # x = 35  # 4
#
#         def fn3():
#             nonlocal x
#             x = 55  # 6
#
#         fn3()  # 5
#         print('fn2.x =', x)  # 7
#     fn2()  # 3
#     print('fn1.x =', x)  # 8
#
#
# fn1()  # 1


# Далее еще пример если закоментировать нонлокал то результат будет по нулям


# def out(a1,b1,a2,b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a,b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a,b]
#
#
# res = out(2,3,-1,4)
# print(res)


#  Замыкние -возвращениевложенной функции без её вызова то есть без скобак

# def out(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
# it1 = out(5)
# print(it1(10))
#
# it2 = out(5)
# print(it2(2))


# Пример замены данных в переменных

# def fu1():
#     a = 1  # неизменяемый тип данных
#     b = 'line' # изменяемый
#     c = [1, 2, 3]
#
#     def fu2():
#         nonlocal a,b
#         c.append(4)
#         a+=1
#         b += '_new'
#         return a, b, c
#
#     return fu2()
#
#
# func = fu1()
# print(func)


# Задача на уроке - написать функцию подсчета посещаемых городов


# def func(city):
#     s=0
#
#     def inner():
#         nonlocal s
#         s+=1
#         print(city,s)
#
#     return inner
#
#
# res1=func('Москва')
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res2()
# res2()
# res1()


# lambda (анонимная функци)

# print((lambda x, y: x + y)(1, 2))
# fun = lambda x, y: x + y
# print(fun(1, 2))
# print(fun('a', 'b'))


# Задача на уроке - создать лямбда-выражение которое считает сумму двухт квадратов чисел
#
# print((lambda x, y: x ** 2 + y ** 2)(2, 5))
# print((lambda x, y=5: x ** 2 + y ** 2)(2))
# print((lambda x=2, y=5: x ** 2 + y ** 2)())
# print((lambda x=2, y=5: x ** 2 + y ** 2)(y=10))


#
# print((lambda *args:args)(1,2,3,4,5))


# y = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
#
# for i in y:
#     print(i('a1'))


# Различные записи функций

# 1
# def outer(n):
#     def inner(x):
#         return x + n
#
#     return inner
#
#
# f = outer(5)
# print(f(10))
#
# # Второй вариант
# def outer1(n):
#     return lambda x: x + n
#
#
# f1 = outer1(5)
# print(f1(10))
#
# # 3
#
# outer2 = lambda n:lambda x:x+n
# f2 = outer2(5)
# print(f2(10))
#
# # 4
# print((lambda n:lambda x:x+n)(5)(10))


# print((lambda n: lambda x: lambda c: c + x + n)(5)(10)(3))


# Отсоритируем кортеж сначала переделав его в список в двух вариантах

# # 1
#
# # def func(item):
# #     return item[1]
#
# # 2
#
# d = {'b':3,'c':1,'a':2}
# print(d)
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i:i[1])
# # lst.sort((key=func))
# print(lst)
# d1=dict(lst)
# print(d1)


# Задача на урове отсортировать команду по фамилиям ибаллам

# plaers = [
#     {'name':'Антон','last name':'Бирюков','reating':'2'},
#     {'name':'Алексей','last name':'Родня','reating':'1'},
#     {'name':'Федор','last name':'Сидоров','reating':'4'},
#     {'name':'Михаил','last name':'Югов','reating':'3'}
# ]
#
# res = sorted(plaers,key=lambda item:item['last name'])
# print(res)
#
# res1 = sorted(plaers,key=lambda item:item['reating'])
# print(res1)
#
# res2 = sorted(plaers,key=lambda item:item['reating'],reverse=True)
# print(res2)


#### Обратимся через индекс к нужному

# a = [
#     lambda x, y: x + y,
#     lambda x, y: x - y,
#     lambda x, y: x * y,
#     lambda x, y: x / y,
# ]
#
# print(a[0](5,2))
# print(a[1](5,2))
# print(a[2](5,2))


###### По ключу выберем нужный день недели

# d = {
#     1: lambda: print('Понеде'),
#     2: lambda: print('Вторник'),
#     3: lambda: print('Среда')
# }
#
# d[1]()
# d[3]()


#### Найдем максимальное значение

# print((lambda a,b:a if a > b else b)(10,20))

##### Мин знач между трем числами

# print((lambda a, b, c: a if (a < b and a < c) else (b if b < c else c))(10, 200, 3))


### ----------------------------  Урок 16
#### map(func, *iterables)


### 1
# def mult(t):
#     return t * 2
#
#
# lst1 = [2, 8, 12, -5, -10]
#
# lst2 = list(map(mult, lst1))
# print(lst2)  # [4, 16, 24, -10, -20]


####  2

# lst1 = [2, 8, 12, -5, -10]
#
# lst2 = list(map(lambda t: t * 2, lst1))
# print(lst2)  # [4, 16, 24, -10, -20]


### из вещественных чисел сделаем целые

###    1

# t = (2.88, -1.75, 100.55)
# t2 = tuple(map(lambda x: int(x), t))
# print(t2)

####  2

# t = (2.88, -1.75, 100.55)
# t2 = tuple(map(int,t))
# print(t2)


##### primer
#
# st = ['a','b','c','d','e',]
# num = [1,2,3,4,5]
#
# res = list(map(lambda x,y: (x,y),st,num))
# print(res)


#### Задача на уроке - найти сумму двух чисел

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# res = list(map(lambda x, y: x + y, l1, l2))
# print(res)


#### Пример выведем значения с длинной 3
#
# t = ('ajdk', 'fgh', 'rub', 'ggg', 'jjjjj')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)


#### отличие функций  map  и  filter ,одна только фильтрует другая еще и складывает

# b = [66, 90, 68, 59, 76, 40, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# res2 = list(map(lambda s: s + 5, b))
# print(res)
# print(res2)


### Пример возведем в степень 2 все числа из 10 которые с остатком от деления

# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10))))
# m1 = list(map(lambda x: x ** 2, [1, 3, 5, 7, 9]))
# print(m)
# print(m1)
# m2 = [x ** 2 for x in range(10) if x % 2]
# print(m2)


### Задача на уроке - вывести чисда в диапазоне от 10 до 20 включительно
#
# import random
#
# my_list = [random.randint(1,40) for i in range(20)]
#
# print(my_list)
# print(list(filter(lambda num: 10 <= num <= 20,my_list)))


### функция передается в качестве аргумента в другую функцию

# def hello():
#     return 'Hello,I am func "hello"'
#
#
# def s_func(func):
#     print('Hello,I am func "s_func"')
#     print(func())
#
#
# s_func(hello)


### Primer создаем функцию и записываем ее в переменную и вызываем со скобочками

# def hello():
#     return 'Hello,I am func "hello"'
#
#
# test = hello
# print(test())


### Декоратор


###  1
# def my_decorator(func):
#     def wrap():
#         print('Код до функции')
#         func()
#         print('Код после функции')
#     return wrap
#
#
# def func_test():
#     print('Hello, I am func "func_test"')
#
#
# test = my_decorator(func_test)
# test()


###  2 две функции в декораторе
# def my_decorator(func):  # декорирующая функция
#     def wrap():
#         print('*' * 30)
#         func()
#         print('=' * 30)
#
#     return wrap
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print('Hello, I am func "func_test"')
#
# @my_decorator
# def hello():
#     print('Hello,I am func "hello"')
#
#
# func_test()
# hello()

#### декорация в одну строку там где ретурн

# def bold(fn):
#     def wrap():
#         return '<br>' + fn() + '</br>'
#
#     return wrap
#
#
# def bold1(fn):
#     def wrap():
#         return '<i>' + fn() + '</i>'
#
#     return wrap
#
#
# @bold
# @bold1
# def hello():
#     return 'text'
#
#
# print(hello())


### Задача на уроке - создать декоратор который выводит количество вызовов декорирующих функций

###   1

# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count = count + 1
#         fn()
#         print('Вызов функции:', count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print('Hello')
#
#
# hello()
# hello()
# hello()

####     2
# def cnt(fn):
#     count = 0
#
#     def wrap(arg1,arg2):
#         nonlocal count
#         count = count + 1
#         fn(arg1,arg2)
#         print('Вызов функции:', count,'\n','-' * 20,sep='')
#
#     return wrap
#
#
# @cnt
# def hello(a,b):
#     print('Hello,',a,'\nHello,',b)
#
#
# hello('Py','JS')
# hello('PHP','C++')


#### Primer

# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print('args', args)
#         print('kwargs', kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_data(a, b, c, study='Ry'):
#     print(a, b, c, 'изучают', study, '\n')
#
#
# print_data('dfg', 'asd', 'cvb', study='C++')
# print_data('bnn', 'gbn', 'tre')


### Задача на уроке складываем два числа
# def decor(args1,args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, '=', end=' ')
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor('Сумма:','+')
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:",'-')
# def sub(a, b):
#     print(a - b)
#
#
# summa(2, 2)
# sub(7, 3)


## Задача на уроке - создать декораторкоторый принимает число,которое умножается на число принимаемой функцией

# def multiply(arg):
#     def test(fn):
#         def wrap(x):
#             return fn(x) * arg
#         return wrap
#     return test
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))


### ----------------------------- Урок 17 --------- Строки

# print(int('100',2))  # 4
# print(int('100',8))  # 64
# print(int('100',10))  # 100
# print(int('100',16))  # 256
#
# print(bin(18))  # 0b10010
# print(oct(18))  # 0o22
# print(hex(18))  # 0x12
#
# print(0b10010)
# print(0o22)
# print(0x12)
# print(0b10010 + 0o22 + 0x12 + 18)


#### Пример работы со строками

# q = 'Pyt'
# w = "hon"
# e = q + w
# print(e)
#
# # print(e * 3)
# # print('y' in e)
# # print('y1' in e)
#
# print(e[-6])
# print(e[:4])
# print(e[2:])
# print(e[::-1])


#### Пример замены букв с помощью срезов

# q = 'Pyt'
# w = "hon"
# e = q + w
# print(e)  # Python => Pytton
# e = e[:3] + 't' + e[4:]
# print(e)


### Задача на уроке - заменить символ в строке

# def changeCharToStr(s, c_old, c_new):
#     s2 = ''
#     i = 0
#
#     while i < len(s):
#         if s[i] == c_old:
#             s2 += c_new
#         else:
#             s2 += s[i]
#         i += 1
#     return s2
#
#
# str1 = 'Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования.'
# str2 = changeCharToStr(str1, 'N', 'P')
# print('str1=', str1)
# print('str2=', str2)


### Зарезервированные символы

# 1 указывает что юникод
#
# print('Привет')
# print(u'Привет')
#
# # 2 добавляет экранирование
#
# print('C:\\folder\\file.txt')
# print(r'C:\folder\file.txt')
# # Убирает слэш
#
# print(r'C:\\folder\\file.txt\\'[:-1])
# print(R'C:\\folder\\file.txt' + '\\')

# 3 f строка

# name = 'Саша'
# age = 39
# print(f'Меня зовут {name}. Мне {age} лет')
#
# # Уберем лишние цифры после точки
#
# m = 2.682869
# print(f'Число: {round(m, 2)}')
# print(f'Число: {m:.3f}')

# 4 Присваиваем сразу значение переменной
# x = 10
# y = 5
# print('x = ', x, ', y = ', y, sep='')  # ставим пробелы что бы их убрать
# print(f'{x = }, {y = }')

# 5 Арифметические действия
# x = 10
# y = 5
# print(f'{x} x {y} / 2 = {x * y / 2}')

# 6 Убираем фигурные скобки  или добавляем

# num = 74
# print(f'{num}')
# print(f'{{num}}')
# print(f'{{{num}}}')
# print(f'{{{{num}}}}')
# print(f'{{{{{num}}}}}')

# 7 Собираем путь к каталогу через переменные
# dir_name = 'my_doc'
# file_name = 'data.txt'
# print(fr'home\{dir_name}\{file_name}')
# print('home\\' + dir_name + '\\' + file_name)


#### Типы кавычек используются для документирования функций
#
# s ="""
# Многостро'чный' "новый"
# текст
# """
#
# print(s)
#
# s1 = '''
# Многострочный
# '''
# print(s1)


# Документация на функции

# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
# print(sum.__doc__)


#### Пример документации

# from math import pi
#
#
# def cylinder(r,h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2,4))


# Коды символов
# print(ord('a'))  # 97
# print(ord('й'))  # 1081

###  Пример в цикле находим любой код любого введеного символа

# while True:
#     n = input("->")
#     if n != '-1':
#         print(ord(n))
#     else:
#         break


####### Задача на уроке - дана строка ,нужно вывести ее аски коды
# и отсортировать в будующем введение символы юзер

# s = 'Test string for me'
# arr = [ord(x) for x in s]
# print('ASCII коды:',arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print('Среднее арифметическое:',arr)
# arr += [ord(x) for x in input('->')[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)


#  По коду получаем символ
#
# print(chr(97))
# print(chr(1048))
# print(chr(8364))


### Пример сравнения строк по кодам символов
#
# print('apple' == 'Apple')  # 97 == 65
# print('apple' > 'Apple')  # 97 > 65
#
# print(ord('a'))
# print(ord('A'))


### ----------------------------  Урок 18

# Создадим программу которая генерирует случайный пароль

# from random import randint
#
# SHORTEST = 7
# LONGTEST = 10
# MIN_ASCII = 33
# MAX_ASCII = 126
#
#
# def random_password():
#     random_length = randint(SHORTEST,LONGTEST)
#     result = ''
#     for i in range(random_length):
#         result += chr(randint(MIN_ASCII,MAX_ASCII))
#     return result
#
#
# print('Ваш случайный пароль:', random_password())


######### Методы строк

###  Изменение регистров разных букв в строках

# s = 'hello, WORLD! I am learning Rython'
# print(s.capitalize())
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())

# ### подсчет вхождений точных подстроки в строку
# s = 'hello, WORLD! I am learning Rython'
# print(s)
# print(s.count('h'))
# print(s.count('h', 1, -4))  # с заданным диапазоном от какого и до какого символа проверять

# индекс вхождения
# s = 'hello, WORLD! I am learning Rython'
# print(s.find('Rython',10, -20))  # с диапазоном поиска если не находит то -1 выводится
# print(s.find('l'))
# print(s.rfind('l'))  # с конца ищет
#
# print(s.index('l'))  # возвращает индекс или ошибку
# print(s.rindex('l'))


### Задача на уроке - переставить два слова в строке местами
# _s = input('Введите два слова через пробел: ')
# first = _s[:_s.find(' ')]
# second = _s[_s.find(' ') + 1:]
# print(second + ' ' + first)


## Ищем начинается ли строка с заданного символа
# s = 'hello, WORLD! I am learning Rython'
# print(s.startswith('hello'))
# print(s.find('I am'))
# print(s.startswith('I am', 14))
#
# print(s.endswith('on'))
# print(s.endswith('lo',3,5))


## Проверяем состоит ли стока только из букв или только из цифр(пробелы ,тире и прочее не считаются)
# s = 'hello, WORLD! I am learning Rython'
# print('abc123'.isalpha())
# print('abcABC'.isalpha())
# print(''.isalpha())
# print('123'.isdigit())
# print('123.234'.isdigit())
#
# print('abc123'.isalnum())
# print('abcA123'.isalnum())


## Проверяем находятся ли буквы в верхнеи или нижнем регистре
# s = 'hello, WORLD! I am learning Rython'
# print('abc'.islower())
# print('!abc456A'.islower())
#
# print('!456A'.isupper())
# print('!456Aa'.isupper())
#
# # Выровним строку по центру
# print('py'.center(10,'-'))
# print('py'.center(11,'-'))
#
# # Уберем пробельные символы
# print(' py'.lstrip())
# print('py    '.rstrip())
# print('    py   '.strip())
#
# # Удалим заданные символы и как только удалим при первом нахождении то остальные не удаем
# print('https://www.python.org'.lstrip())
# print('https://www.python.org'.lstrip('/:pths').rstrip('.org'))
# print('https://www.python.org'.strip('/:pths.org'))

# ##  Задача на уроке - заменим нужное слово и нужное количество раз
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(str1)
# print(str1.replace('Nython', 'Python', 2))


# Разделяем заданные символы заданным символом
# s1 = '-'
# seq = ('a','b','c')
# print(s1.join(seq))
# print('..'.join(['1','2']))  # объединяет итерируемый последовательность (состоит из строк) в строку
# print(':'.join('Hello'))

## Разделим строку на список из элементов этой строке разделенных пробелом
# s = 'hello, WORLD! I am learning Rython'
# print(s.split())
# print('www.python.org.ru'.split('.',2))  # посл два не разделяет а ниже первые не разделяет
# print('www.python.org.ru'.rsplit('.',2))


# Юзер вводит фамили имя отчество а прога выводит инициалы
# a = input('Введите ФИО: ').split()
# print(a)
# print(a[0], a[1][0] + '.', a[2][0] + '.')


####### Primer  получим либо строку либо числа
# a = input('Введите коды символов через пробел: ').split()
# print(a)
#
# b = list(map(int,a))
# print(b)


#### ________ Работа с регулярными выражениями

import re

# s = 'Я ищу совпадения в 2024 году. И я их найду в 2 счёта.'
# reg = 'совпадения'
# print(re.findall(reg,s))  # список содержащий все совпадения с шаблоном
#
# print(re.search(reg,s))  # месторасположение  первого совпадения с шаблоном
# print(re.search(reg,s).span())  # (6, 16)
#
# print(re.search(reg,s).start())  # 6
# print(re.search(reg,s).end())  # 16
#
# print(re.search(reg,s).group())  # совпадения


#######
# s = 'Я ищу совпадения в 2024 году. И я их найду в 2 счёта.'
# reg = 'совпадения'
# print(re.match(reg,s))  # Возвращаетместорасположение совпадения с шаблоном,в начале строки


#########
# s = 'Я ищу совпадения в 2024 году. И я их найду в 2 счёта.'
# reg = '[.я2]'
# print(re.split(reg,s))  # возвращает список,в котором строка разбита по шаблону


#############
# s = 'Я ищу совпадения в 2024 году. И я их найду в 2 счёта.'
# reg = r'\.'
# print(re.sub(reg,'!',s,1))  # поиск и замена (можно по количеству)


###########
# s = 'Я ищу совпадения в 2024 году. И я их найду в 2 счёта.'
# reg1 = r'[12][0-9][0-9][0-9]'
# reg = r'[А-яЁё]'
# print(re.findall(reg1,s))
# print(re.findall(reg,s))
#
# print(ord('а'))
# print(ord('я'))
# print(ord('ё'))


#############
# s = 'Я ищу совпадения в 2024 году. И я их найду в 2 счёта.'
# reg = r'[^0-9]'
# print(re.findall(reg,s))


########---------------- Урок 19

# Задача на уроке найти время в нужном формате
# st = "Час в 24-часовом формате от 00 до 23. 2021-06-15Е21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09."
# reg = r'[0-2][0-9]:[0-5][0-9]'
# print(re.findall(reg,st))


# Ищем нужные цифры в строке
# d = 'Цифры: 7, +17, --42, 0.3'
# print(re.findall(r'[+-]?\d+[.\d]*',d))


######## Удалим все после решетки и заменим тире на точку
# st = '05-03-1987 # Дата рождения'
# print('Дата рождения:', re.sub('-', '.',re.sub(r'#.*','',st)))


### Задача на уроке - Написать регулярное выражение для нахождения всех ключей
# и значей(ищем элементы от одного до любого количества повторений пока
# не встречается точка с запятой)

# st = 'author=Пушкин А.С.; title = Евгений Онегин; prise =200; year= 1831'
# reg = r'\w+\s*=\s*[^;]+'
# print(re.findall(reg,st))


### Найдем числа который состоят из двух трех или четырех символов

# st = '12 сентябра 2021 года 79456713687122'
# reg = r'\d{2,4}'
# print(re.findall(reg,st))


# Задача найти номер телефона
# 1
# st = '+7 499 456-45-76, +74994564576, 74994564576'
# reg = r'\+?7\d*'
# print(re.findall(reg,st))
# # 2
# st = '+7 499 456-45-76, +74994564576, 74994564576'
# reg = r'\+?7\d{10}'
# print(re.findall(reg,st))


# Проверим валидность пароля на определенные символы

# def valid_login(name):
#     return re.findall(r'^[A-Za-z0-9_-]{6,16}$',name)
#
#
# print(valid_login('Python_master'))
# print(valid_login('Python@master'))

## Флаги

# print(re.findall(r'\w+','12 + й'))
# print(re.findall(r'\w+','12 + й',flags=re.ASCII))
# print(re.findall(r'\w+','12 + й',flags=re.A))
# print(re.findall(r'\w+','12 + й',re.A))


###

# text = 'hello world'
# # print(re.findall(r'\w+',text))
# print(re.findall(r'\w+',text,re.DEBUG))

##Найдем букву я в разных регистрах

# s = 'Я ищу совпадения в 2024 году. И я их найду в 2 счёта'  #. 198765 Hel_lo[-World] 2000010 002000'
# reg = r'я'
# print(re.findall(reg,s,re.IGNORECASE))


####
# text = '''
# one
# two
# '''
# # print(re.findall(r'one.\w+', text))
# # print(re.findall(r'one.\w+', text,re.DOTALL))
# print(re.findall(r'one$',text))
# print(re.findall(r'one$',text,re.MULTILINE))

### Игнорируем пробелы и переносы в написанном коде для поиска нужных символов

# print(re.findall(r'''
# [a-z.-]+    # 1
# @           # @
# [a-z.-]+    # 2
# ''','test@mail.ru',re.VERBOSE))


##
# text = '''Python,
# python,
# PyTHON'''
# reg = '(?mi)^python'
# print(re.findall(reg, text))


### --------------- 20 Урок

# text = '<body>Пример жадного соответствия регулярных выражений<body>'
# print(re.findall('<.+?>',text))
#
# # *?, +?, ??
# # {m,n}?, {,n}?, {m,}?
#
# st = '12 сентябра 2021 года 79456713687122'
# reg = r'\d{2,}?'
# print(re.findall(reg,st))


### Primer
# s = "<p>Изображение <img src='bg.jpg'> - фон страницы</p>"
# # reg = r'<img.*?>'
# reg = r'<img[^>]*>'
# print(re.findall(reg,s))


#### Ищем именно картинку с атрибутами
# s = "<p>Изображение <img alt='картинка' src='bg.jpg'> - фон страницы</p>"
# reg = r'<img\s+[^>]*src\s*=\s*[^>]+>'
# print(re.findall(reg,s))


## Задача на уроке - найти сноски в квадратных скобках
# text = "Python (в русском языке встречаются названия пито́н [16]или па́йтон [17]) — высокоуровневый язык " \
#        "программирования общего назначения с динамической строгой типизацией " \
#        "и автоматическим управлением памятью[18][19]."
#
# print(re.findall(r'\[\d+]',text))


### Primer
# s = 'Петр, Ольга и Виталий отлично учатся!'
# reg = 'Петр|Виктор|Ольга'
# print(re.findall(reg,s))


### Задача на уроке - поиск ключа и значений
# s = 'int = 4, float = 4.0f, double = 8.0'
# # # reg = r'\w+\s*=\s*\d[.\w]*'
# # # print(re.findall(reg,s))
# # # Найдем без double
# # # # reg = r'(?:int|float)\s*=\s*\d[.\w]*'
# # # # print(re.findall(reg,s))
# # # (?:...) - это группирующа скобка являетс не сохранющей
# # reg = r'((?:int|float)\s*=\s*(\d[.\w]*))'
# # print(re.findall(reg,s))
# reg = r'(?:int|float)\s*=\s*\d[.\w]*'
# print(re.findall(reg,s))

## Ищем айпи адрес
# s ='127.0.8.1'
# # s = '127.168.255.255'
# # reg = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
# reg = r'(?:\d{1,3}.){3}\d{1,3}'
# print(re.findall(reg,s))

### Разобьем строку на символы и уберем пробелы
# s = '5 + 7*2 - 4'
# reg = r'\s*([+*-])\s*'
# print(re.split(reg,s))


### Задача на уроке - юзер вводит дату по шаблону а мы проверяем на соответствие
# a = '01-12-1921'
# pattern = '(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])'
# print(re.findall(pattern,a))


###### Найдем все цифры от одной до любого количества и потом все что не цифры
# s = 'Я ищу совпадения в 2024 году. И я их найду в 2 счёта.'
# reg = r'([0-9]+)\s(\D+)'
# print(re.findall(reg,s))
# print(re.search(reg,s).group())
# m = (re.search(reg,s))
# print(m[0])
# print(m[1])
# print(m[2])


#### Добавим к городам нумерацию
# text = '''
# Самара
# Москва
# Тверь
# Уфа
# Казань
# '''
#
# count = 0
# def repl_find(m):
#        global count
#        count += 1
#        return f"<option value='{count}'>{m.group(1)}</option>\n"
#
#
# print(re.sub(r'\s*(\w+)\s*',repl_find,text))


#####
# s = "<p>Изображение <img src='bg.jpg'> - фон страницы</p>"
# reg = r"<img\s+[^>]*src\s*=(?P<q>['\"])(.+?)(?P=q)>"
# print(re.findall(reg,s))

# (?P<name>...) (?P=name)


# #  Польза круглых скобок Нужно найти дату со слэшом и заменить на точку
# s = 'Самолет прилетает 10/23/2024. Будем рады вас видеть после 10/24/2024.'  # 23.10.2024
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# print(re.sub(reg, r'\2.\1.\3', s))


## Найдем адрес сайта и сделаем его кликабельной ссылкой
# s = 'yandex.com and yandex.ru'
# reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r'http://\1', s, re.IGNORECASE))



### ---------------- Урок 21