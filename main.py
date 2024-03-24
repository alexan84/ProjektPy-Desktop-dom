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


### ---------------- Урок 21 ----- Рекурсия - это функция которая вызывает саму себя

#### Пример пишем функцию для спуска по этажам подъезда

# def elevator(n):
#     if n == 0:
#         print('Вы в подвале')
#         return
#     print('=>',n)
#     elevator(n -1)
#     print(n,end=' ')
#
#
# n1 = int(input('На каком вы этаже: '))
# elevator(n1)


### Задача на уроке -  найти сумму элементов списка

## 1 С помощью обычного цикла фор

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res


## 2  С помощью рекурсии
# def sum_list(lst):
#     if len(lst) == 1:
#         print(lst,'=> lst[0]',lst[0])
#         return lst[0]  # 9
#     else:
#         print(lst, '=> lst[0]', lst[0])
#         return lst[0] + sum_list(lst[1:])  # 1 + 3 + 5 + 7
#
#
# print(sum_list([1,3,5,7,9]))


### Задача пишем число и систему исчесления в которую это число переведется
# def to_str(n, base):  # n = 3
#     convert = '0123456789ABCDEF'
#     if n < base:  # 3 < 10
#         return convert[n]  # '3'
#     else:
#         return to_str(n // base, base) + convert[n % base]  # convert[6] => '5' '6'
#
#
# print(to_str(365, 10))

### Первод в шестнадцатиричную систему

# def to_str(n, base):  # n = 254
#     convert = '0123456789ABCDEF'
#     if n < base:  # 254 < 16
#         return convert[n]  # convert[15] => 'F'
#     else:
#         return to_str(n // base, base) + convert[n % base]  # convert[14] => 'E'
#
#
# print(to_str(254, 16))


#### Пример Составим вложенные списки и посчитаем сколько всего элементов в списке

# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
# print(names)
# print(names[0])
# print(isinstance(names[0], list))
# print(names[1])
# print(isinstance(names[1], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))
#
#
# def count_item(lst):
#     count = 0
#     for item in lst:
#         if isinstance(item,list):
#             count += count_item(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_item(names))


#### Пример удалим пробелы и табуляцию из строки

# def remove(text):
#     if not text:
#         return ""
#     if text[0] == "\t" or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print('   Hello\tWorld                      a')
# print(remove('   Hello\tWorld                      a'))


####------------------------------ Файлы


# Текстовые
# Бинарные

# # f = open(r'C:\Users\blend\Desktop\PYTHON\test.txt', 'r')  # mode='r'
# f = open('test.txt', 'r')  # mode='r'
# print(*f)
# print(f)
# f.close()
# print(f.closed)
# print(f.mode)
# print(f.name)
# print(f.encoding)


# f = open('test.txt', 'r')
# print(f.read(3))
# print(f.read())
# f.close()


# f = open('test1.txt', 'r')
# # print(f.read())
# print(f.readline())  # Считалаи оодну строку из файла
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()

#
# f = open('test1.txt', 'r')
# print(f.readlines(16))
# print(f.readlines())  # считали все данные из файла и вернули список строк
# f.close()


# f = open('test1.txt', 'r')
# for line in f:
#     print(line)
# f.close()


## Задача - посчитать количество строк в файле

# f = open('test1.txt', 'r')
# count = 0
# for line in f:
#     print(line)
#     count += 1
# f.close()
# print(count)


## Создадим файл
# f = open('xyz.txt', 'w')
# f.write('Hello\nWorld!\n')
# f.close()


# Добавляет текст в конец файла
# f = open('xyz.txt', 'a')
# f.write('Hello\n')
# f.close()


# Перезаписывает файл в одну строку
# f = open('xyz.txt', 'w')
# line = ['This is line 1\n', 'This is line 2']
# f.writelines(line)
# f.close()


########-------------------------------- Уроку 22

# f = open('xyz.txt', 'w')
# lst = [str(i) for i in range(1,20)]
# print(lst)
# for index in lst:
#     f.write(index + '\t')
# f.close()


### Задача - заменить 2 строку на другие значения
# Создадим файли закоментируем его
# f = open('text2.txt','w')
# f.write('Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n')
# f.close()
#
# # Считываем данные файла и записываем в переменную
# f = open("text2.txt", "r")
# rl = f.readlines()
# f.close()
#
# # Заменили по индексу вторую строку
# print(rl)
# rl[1] = 'Hello World\n'
# print(rl)
#
# # Только тут перезапишем в самом файле нужный элемент
# f = open("text2.txt","w")
# f.writelines(rl)
# f.close()


# Задача удалить выбранную строчку юзером

# f = open('text2.txt','w')
# f.write('Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n')
# f.close()

# filename = "text2.txt"
# f = open(filename, "r")
# rl = f.readlines()
# f.close()
#
# print(rl)
#
# pos = int(input('Введите индекс для удаления: '))
# if 0 <= pos < len(rl):
#     rl.pop(pos)
# else:
#     print('Индекс введен не верно')
#
# print(rl)
#
# f = open(filename, "w")
# f.writelines(rl)
# f.close()


# Дополнительные методы

# f = open('test.txt','r')
# print(f.read(3))
# print(f.tell())  # возвращает текущую позицию условного курсора
# print(f.seek(1))  # переместил условный курсор в заданную позицию
# print(f.read())
# print(f.tell())
# f.close()


# Перезапишем файл и поставим курсор в начало строки
# f = open('test.txt','r+')
# print(f.write('I am learning Python'))
# print(f.tell())
# print(f.seek(3))
# print(f.write('-туц ые-'))
# print(f.tell())
# f.close()


# Перезапишем файл и в цикле пройдемся по символам и выведем нужный диапазон
# with open('test.txt','w+') as f:
#     print(f.write('01234\n56789'))
#
# with open('test.txt','r') as f:
#     for line in f:
#         print(line[:3])


# Список преобразуем в строку и запишем в файл - тут ошибка
# file_name = 'res_1.txt'
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     print(lt)
#     return ''.join(lt)
#
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))  # [4.5,2.8,3.9,1.0,0.3,4.33,7.777]
#
# # Прочтем файл
# with open(file_name, 'r') as f:
#     nums = f.read()
#
# print(nums)
#
# nums_list = list(map(float, nums.split()))  # не удалось преобразовать строку в число с плавающей запятой
# print(nums_list)
# print(sum(nums_list))
# print(len(nums_list))
# print('Done!')


## Задача вывести из файла слово максимальной длины или несколько таких слов


# def longest_worlds(file):
#     with open(file,'r',encoding='utf-8') as text:
#         w = text.read().split()
#         max_length = len(max(w,key=len))  # Длина самого длинного слова
#         print(max_length)
#         res = [word for word in w if len(word) == max_length]
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# print(longest_worlds('worlds.txt'))


## Работа контекстного менеджера с несколькими файлами параллельно
#
# one = 'one.txt'
# two = 'two.txt'
#
# # text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
# #
# # with open(one,'w') as f:
# #     f.write(text)
#
# with open(one,'r') as fr, open(two,'w') as fw:
#     for line in fr:
#         line = line.replace('Строка','Линия -')
#         fw.write(line)


#####--------------------- Урок 23

# Модуль OS и OS.PATH

import os
# import os.path


# print(os.getcwd())  # Путь к текущей директории
# print(os.listdir())  # Список директорий и файлов
# print(os.listdir('..'))

# os.mkdir('folder1')  # Создание одной папки
# os.makedirs('nested1/nested2/nested3')  # создание папки в паках с промежуточными директорими
# os.rmdir('folder1')  # удаление папки
# os.remove('folder1/test.txt')  # удаление папки
# os.remove('xyz.txt')  # Удаление файла

# os.rename('nested1','test')  # Переименовать папку
# os.rename('worlds.txt','test/words_new.txt')  # переименовали файл и переместили в заданную директорию
# os.rename('test1.txt','folder1/file.txt')  # переименовали файл и переместили в заданную директорию и приэтом может создать промежуточные директории


## Проходим по выбранной папке и просмотримвсе её вложенные папки и файлы
# for root,dirs,files in os.walk('test',topdown=True):
#     print('Root',root)
#     print('Subdirs',dirs)
#     print('Files',files)


### Задача - удалить пустые директории в ветки
# def remove_empty_dirs(root_tree):
#     print(f'Удаление пустых директорий в ветви {root_tree}')
#     print('-' * 50)
#
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f'Директория {root} удалена')
#
#
#     print('-' * 50)
#
# remove_empty_dirs('test')

# по индексу
# print(os.path.split(r'C:\ProjektPy-Desktop-dom\test\folder1\file.txt'))
# print(os.path.dirname(r'C:\ProjektPy-Desktop-dom\test\folder1\file.txt'))
# print(os.path.basename(r'C:\ProjektPy-Desktop-dom\test\folder1\file.txt'))
# # создадим новый путь из строк выше
# print(os.path.join(r'C:\ProjektPy-Desktop-dom','folder1'))


## Задача - создать прогу которая создаст дерево директорий и файлов,
# заполнить текстом и снизу вверх и сверху вниз выполнить обход и вывести данные на экран

# создадим список из начальной и конечной директории и в цикле пройдемся по ним и создадим ветку
# dirs = [r'Work\F1', r'Work\F2\F21']
# for d in dirs:
#     os.makedirs(d)

# создадим переменную с ключем и значением
# files = {
#     'Work' : ['w.txt'],
#     r'Work\F1' : ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21' : ['f211.txt', 'f212.txt',],
# }
# #
# # # С помощью метода создадим из разных частей один общий путь(d это ключ  f это значение)
#
# for d, f in files.items():
#     for file in f:
#         file_path = os.path.join(d, file)
#         open(file_path,'w').close()

# заполним файлы текстом

# files_with_text = [r'Work\w.txt',r'Work\F1\f12.txt', r'Work\F2\F21\f211.txt', r'Work\F2\F21\f212.txt']
# for file in files_with_text:
#     with open(file, 'w') as f:
#         f.write(f'Какой то текст для файла по пути: {file}')


# Work\w.txt
# Work\F1\f11.txt
# Work\F1\f12.txt
# Work\F1\f13.txt
# Work\F2\F21\f211.txt
# Work\F2\F21\f212.txt

# Выполняем обход дерева

# def print_tree(root,topdown):
#     print(f"Обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
#     for root,dirs,files in os.walk(root,topdown):
#         print(root)
#         print(dirs)
#         print(files)
#     print("-" * 50)
#
#
# print_tree('Work',False)
# print_tree('Work',True)


##################

# print(os.path.exists(r'C:\Users\blend\Desktop\PYTHON\test\words_new.txt'))  # проверяет существование пути
#
# print(os.path.isfile(r'C:\Users\blend\Desktop\PYTHON\words_new.txt'))  # проверяет что указанный путь является правильным путем к файлу
#
# print(os.path.isdir(r'C:\Users\blend\Desktop\PYTHON\test'))  # проверяет что указанный путь является правильным путем к папке


###########

import time

# path = 'main.py'
# # print(os.path.getsize(path))  # возвращает размер в байтах
# # print(os.path.getsize(path) / 1024)  # в килобайтах
#
# print(time.strftime('%d.%m.%Y, %H:%M:%S', time.localtime(os.path.getatime(path))))  # время последнего доступа к файлу(без модуля time пишется в секундах)
# print(time.strftime('%d.%m.%Y, %H:%M:%S', time.localtime(os.path.getctime(path))))  # время создания файла
# print(time.strftime('%d.%m.%Y, %H:%M:%S', time.localtime(os.path.getmtime(path))))  #  время последнего изменения файла


##### Задача - написать прогу которая проверяет существует ли файл и если да то вывести его данные

# file_path = r'test\folder1\file.txt'
# if os.path.exists(file_path):
#     dirs, name = os.path.split(file_path)
#     print(f'{name} ({dirs}) - последний доступ к файлу: {os.path.getatime(file_path)}')
# else:
#     print(f'Файл {file_path} не существует')


############---------------- Урок    24   ООП
# Классы и объекты


# class Point:
#     x = 1
#     y = 2
#
#
# p1 = Point()
# p1.x = 5
# p1.y = 25
# print(p1.x)
# print(p1.y)
# print(p1.__dict__)
# print(id(p1))
#
# p2 = Point()
# p2.x = 10
# print(p2.x)
# print(p2.y)
# print(p2.__dict__)
# print(id(p2))
# print(id(Point))
#
# print(isinstance(p1, Point))
# print(isinstance(p2, Point))


## Создание методов
# class Point:
#     x = 1
#     y = 2
#
#     def set_coord(self,x,y ):
#         self.x = x
#         self.y = y
#         print(self.__dict__)
#
#
# p1 = Point()
# # p1.x = 5
# # p1.y = 25
# p1.set_coord(5,24)
# # Point.set_coord(p1)
#
# p2 = Point()
# # p2.x = 10
# # p2.y = 30
# p2.set_coord(10,30)


#### Задача создать класс человек с его параметрами
# class Human:
# # создадим свойства
#     name = 'name'
#     birthday = '00.00.0000'
#     phone = '00-00-00'
#     country = 'country'
#     city = 'city'
#     address = 'address'
# # создаем 1 метод для вывода наших свойств
#     def print_info(self):
#         print(' Персональные данные '.center(40,'*'))
#         print(f'Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\n'
#               f'Страна: {self.country}\nГород: {self.city}\nДомашний адрес: {self.address}')
#         print('=' * 40)
# # Второй метод для ввода данных
#     def input_info(self,first_name,birthday,phone,country,city,address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
# # Реализуем доступ к отдельным полям через методы значений класса
# # Заменим только адрес и имя
# # 1
#     def set_address(self,address):  # Устанавливает адрес
#         self.address = address
#     def get_address(self):  # Получаем адрес
#         return self.address
# # 2
#     def set_name(self,name):  # Устанавливает name
#         self.name = name
#     def get_name(self):  # Получаем name
#         return self.name
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info('Юля','23.05.1986','45-46-98','Россия','Москва','Чистопрудный бульвар,1А')
# h1.print_info()
# h1.set_address('ул.Ленина,56')
# print(h1.get_address())
# h1.set_name('Юлия')
# print(h1.get_name())


#### Задача создать класс сотрудника с его данными двумя методами (то есть функциями)

# class Person:
#     skill = 10  # статическое свойство
#     # name = ''
#     # surname = ''
#
#     def __init__(self,name,surname):
#         self.name = name  # динамическое свойство
#         self.surname = surname
#         print('Инициализатор класса:',self)
#
#     def __del__(self):
#         print('Удаление класса', self)
#
#     def print_info(self):
#         print('Данные сотрудника', self)
#
#     def add_skill(self,k):
#         self.skill += k
#         print('Квалификация сотрудника', self.skill,end='\n\n')
#
#
# p1 = Person("Виктор","Резник")
# p1.print_info()
# p1.add_skill(3)
# # del p1
#
# p2 = Person("Анна","Долгих")
# p2.print_info()
# p2.add_skill(2)


########## Задача создать роботакоторый должен поздороваться и выключить его

# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print('Инициализация робота:', self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, 'Выключается!')
#
#         Robot.k -= 1
#
#         if Robot.k == 0:
#             print(self.name,'был последним')
#         else:
#             print('Работающих роботов осталось:', Robot.k)
#
#     def say_hi(self):
#         print('Приветствую! Меня зовут:', self.name)
#
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# print('Численность роботов:', Robot.k)
#
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# print('Численность роботов:', Robot.k)
#
# print('\nЗдесь роботы могут проделывать какую-то работу\n')
#
# print('Роботы закончили свою работу. Давайте их выключим')
#
#
# del droid1
# del droid2
#
# print('Численность роботов:', Robot.k)


### -------------  Урок 25

# Primer 1
# # Модификаторы доступа
# # public - name
# # protected - _name
# # private - __name
#
# class Point:
#     __slots__ = ['__x', '__y'] # Закрываем создание элиментов из вне
#
#     def __init__(self, x, y):
#         self.__x: int | float
#         self.__y: int | float
#         if self.__check_value(x) and self.__check_value(y):
#             self.__x = x
#             self.__y = y
#         # self.set_coordinates(x, y) # так не получиться, еще нет x и y
#
#     @classmethod
#     def __check_value(cls, c):
#         if isinstance(c, (int, float)):
#             return True
#         return False
#
#     def get_coordinates(self):
#         return self.__x, self.__y
#
#     # def set_coordinates(self, x, y):
#     #     if isinstance(x, (int, float)) and isinstance(y, (int, float)):
#     #         self.__x = x
#     #         self.__y = y
#     #     else:
#     #         print('Координаты должны быть числами')
#
#     def set_coordinates(self, x, y):
#         if self.__check_value(x) and self.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print('Координаты должны быть числами')
#
#     def get_x(self):
#         return self.__x
#
#     def set_x(self, x):
#         if self.__check_value(x):
#             self.__x = x
#         else:
#             print('Координата', x, 'должна быть числом')
#
#     def get_y(self):
#         return self.__y
#
#     def set_y(self, y):
#         if self.__check_value(y):
#             self.__y = y
#         else:
#             print('Координата', y, 'должна быть числом')
#
#
# p1 = Point(5, 10)
# # print(p1.x, p1.y)
# # p1.x = 100 # Создание нового свойства, но не изменение атрибута.
# # p1.y = 'abc'
# # print(p1.x, p1.y)
# # print(p1.__dict__)
# # p1._Point__x = 100
# # p1._Point__y = 50
# # print(p1._Point__x, p1._Point__y)
#
# # p1.set_coordinates(100, 200)
# # print(p1.get_coordinates())
# # print(p1._Point__x, p1._Point__y)
#
# # p1.set_coordinates(10.5, 15.5)
# # print(p1.get_coordinates())
# # print(p1._Point__check_value(5))
#
# p1.set_x('100')
# print(p1.get_x(), p1.get_y())
# p1.set_y(30.4)
# print(p1.get_x(), p1.get_y())
# # p1._Point__x = 'abc'
# # print(p1._Point__x)
# # print(p1.__dict__)


# Primer 2
#
# class Point:
#     # __slots__ = ['__x', '__y']
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __get_x(self):
#         return self.__x
#
#     def __get_y(self):
#         return self.__y
#
#     def __set_x(self, x):
#         self.__x = x
#
#     def __del_x(self):
#         del self.__x
#
#     def __set_y(self, y):
#         self.__y = y
#
#     def __del_y(self):
#         del self.__y
#
#     x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 100
# # print(Point.__dict__)
# print(p1.__dict__)
# del p1.x
# print(p1.__dict__)


##### Задача создать класс для преобразования киллограмов в фунты

# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if not isinstance(new_kg, (int, float)):
#             raise TypeError('Килограммы задаются только числами')
#         self.__kg = new_kg
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#     def print_data(self):
#         print(self.kg, 'кг => ', end='')
#         print(self.to_pounds(), 'фунтов')
#
#
# weight = KgToPounds(12)
# # print(weight.kg, 'кг => ', end='')
# # print(weight.to_pounds(), 'фунтов')
# weight.print_data()
# weight.kg = 41
# # print(weight.kg, 'кг => ', end='')
# # print(weight.to_pounds(), 'фунтов')
# weight.print_data()


# Сколько раз вызываласся класс
# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#     # get_count = staticmethod(get_count())
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
#
# print(Point.get_count())
# print(p2.get_count())

# вычетание или прибавление единицы
# class Change:
#     @staticmethod
#     def increment(number):
#         return number + 1
#
#     @staticmethod
#     def decrement(number):
#         return number - 1
#
# print(Change.increment(10), Change.decrement(10))


#### Задача подсчет максимума и минимуму и т.п разных аргументов

# class Math_matic:
#
#     @staticmethod
#     def get_max(*data):
#         return max(*data)
#
#     @staticmethod
#     def get_min(*data):
#         return min(*data)
#
#     @staticmethod
#     def get_average(*data):
#         from statistics import mean
#         return mean(*data)
#
#     # @staticmethod
#     # def factorial(n):
#     #     if n == 1:
#     #         return 1
#     #     else:
#     #         return Math_matic.factorial(n - 1) * n
#
#     @staticmethod
#     def get_factorial(number):
#         fact = 1
#         for i in range(1, number + 1):
#             fact *= i
#         return fact
#
#     @staticmethod
#     def get_factorial(number):
#         from math import factorial
#         return factorial(number)
#
#
# data = [3, 5, 7, 9]
#
# print(Math_matic.get_max(data))
# print(Math_matic.get_min(data))
# print(Math_matic.get_average(data))
# print(f'Факториал числа (5)', Math_matic.get_factorial(5))


### Задача подсчета площади геометрических фигур

# from math import sqrt
#
#
# class Square:
#     __count = 0
#
#     @staticmethod
#     def square_triangle1(a, b, c):
#         Square.__count += 1
#         p = (a + b + c) / 2
#         return sqrt(p * (p - a) * (p - b) * (p - c))
#
#     @staticmethod
#     def square_triangle2(a, b):
#         Square.__count += 1
#         return 0.5 * a * b
#
#     @staticmethod
#     def square_area(a):
#         Square.__count += 1
#         return a * a
#
#     @staticmethod
#     def square_rectangle(a, b):
#         Square.__count += 1
#         return a * b
#
#     @staticmethod
#     def get_count():
#         return Square.__count
#
#
# print('Площадь треугольника по формуле Герона:', Square.square_triangle1(3, 4, 5))
# print('Площадь треугольника через основание и высоту:', Square.square_triangle2(6, 7))
# print('Площадь квадрата:', Square.square_area(7))
# print('Площадь прямоугольника:', Square.square_rectangle(2, 6))
# print('Количество подсчетов площади:', Square.get_count())


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
#                 graphic += '* ' + '  ' * (self.height - 2) + '*' + '\n'
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


#########---------------- Урок 26 --------------------


####### Задача преобразуем введеные данные даты в нужный формат

#
# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split('.'))
#         date1 = cls(day, month, year)
#         return date1
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count('.') == 2:
#             day, month, year = map(int, date_as_string.split('.'))
#             return day <= 31 and month <= 12 and year <= 3999
#
#     def string_to_db(self):
#         return f'{self.year}-{self.month}-{self.day}'
#
#
# dates = [
#     '30.12.2023',
#     '30-12-2020',
#     '01.01.2024',
#     '12.31.2020'
# ]
#
#
# for string_date in dates:
#     if Date.is_date_valid(string_date):
#         date = Date.from_string(string_date)
#         print(date.string_to_db())
#     else:
#         print('Неправильная дата или формат строки с датой')
#
#
# # date2 = Date.from_string('23.10.2024')
# # print(date2.string_to_db())
# # string_date = '23.10.2024'
# # date = Date(day, month, year)
# # print(date.string_to_db())


### Задача создать класс - аккаун банковског счета со всеми данными


# class Account:
#     # Сначало пишем статические свойства
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     # Метод оповещающий что счет открыт
#     # И тут пишем динамические свойства
#     def __init__(self, surname, num, percent, value=0):
#         self.surname = surname
#         self.num = num
#         self.percent = percent
#         self.value = value
#         print(f'Счет{self.num} принадлежащий {self.surname} был открыт.')
#         print('*' * 50)
#
#     # Деструктор - закрытие счета
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счет #{self.num} принадлежащий {self.surname} был закрыт.')
#
#     # Метод изменения статических переменных(установка новых значений доллара)
#     # В разных методах мы по разному обращаемся к переменным класса!!!!!!
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#     # Меняе значение курса евро
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     # Метод конвертации валюты на счете
#     # Первым создаем статический метод где указывается принцип конвертации валют
#     # А далее создаем методы под каждую валюту отдельно и там указываем метод принципа конвертации
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     # Метод добавления денег на баланс и вывод остатка
#     def add_money(self,val):
#         self.value += val
#         print(f'{val} {Account.suffix} было успешно добавлено!')
#         self.print_balance()
#
#     # Тут вылью берется из init а рэйтюсд из статических переменных
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f'Состояние счета: {eur_val} {Account.suffix_eur}')
#
#     # Создадим метод показывающий баланс
#     def print_balance(self):
#         print(f'Текущий баланс {self.value} {Account.suffix}')
#
#     # Метод изменения владельца счета
#     def edit_onwer(self, surname):
#         self.surname = surname
#
#     # Метод начисления процентов , тут происходит расчет начисления и вызов баланса
#     def add_percent(self):
#         self.value += self.value * self.percent
#         print('Проценты были успешно начислены')
#         self.print_balance()
#
#     # Метод снятия денег и показывание остатка на балансе
#     # С условием того что на балансе достаточно денег,что бы не допустить минусового баланса
#     def withdraw_money(self,val):
#         if val > self.value:
#             print(f'К сожалению у вас нет {val} {Account.suffix}')
#         else:
#             self.value -= val
#             print(f'{val} {Account.suffix} было успешно снято')
#         self.print_balance()
#
#     # Метод - информация о счете
#     def print_info(self):
#         print('Информация о счете:')
#         print('-' * 20)
#         print(f'#{self.num}')
#         print(f'Владелец: {self.surname}')
#         self.print_balance()
#         print(f'Проценты: {self.percent:.0%}')
#         print('-' * 20)
#
#
# # Создаем экземпляр класса где приходят параметры человека на его аккаунт
# # Присвоим переменной класс и будем вызывать класс обращаясь к переменной
# acc = Account('Долгих', '12345', 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# # С начала перезапишем курс(изменим),потом сразу вызовем показывающий курс метод
# Account.set_usd_rate(2)
# print()
# # Вызовем метод изменяющий евро как выше вызывали изменение доллара
# Account.set_eur_rate(3)
# acc.convert_to_usd()
# acc.convert_to_eur()
# # Меняем фамилию владельца счета и выводим инфу о счете
# acc.edit_onwer('Дюма')
# acc.print_info()
# print()
# acc.add_percent()
# print()
# acc.withdraw_money(100)
# print()
# acc.withdraw_money(3000)
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)


### Задача пользователь при устройстве на работу оставляет свои данные

# Свойства в классе сделаем закрытыми

# import re
#
#
# class UserData:
#     # иницилизируем методы что бы при запуске программы иметь возможность смотреть что у нас получается
#     def __init__(self, fio, old, ps, weight):
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     # Сделаем возможность что бы за пределами класса менять какие то свойства
#     # создаем декоратор проперти и для каждого из наших свойств делаем геттер и сеттер
#     # геттер только возвращает значение
#     # .
#     @property  # это геттер
#     def fio(self):
#         return self.__fio
#
#     @fio.setter  # это сеттер
#     def fio(self, fio):
#         self.verify_fio(fio)  # Проведем проверку и если этот метод не выкинет исключение то тогда
#         self.__fio = fio  # иницилизируемв нашу переменную новое значение
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.verify_old(old)
#         self.__old = old
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, w):
#         self.verify_weight(w)
#         self.__weight = w
#
#     # Задача смотреть что будет неправильно и будем сами включать исключения
#     # и каждое из этих свойств будем проверять отдельно
#     # и создадим статический метод котроый будет проверять ввод некоректных данных
#
#     @staticmethod
#     # Водном методе сделаем несколько проверок
#     def verify_fio(fio):
#         # ПРоверим тип данных если не соответствует
#         # то выведется ошибка то есть исключение(вводим в парметры класса)
#         if not isinstance(fio, str):
#             raise TypeError('ФИО должно быть строкой')
#         # Проверим формат вводимых фио(3 слова)
#         f = fio.split()
#         if len(f) != 3:
#             raise TypeError('Неверный формат ФИО')
#         # Проверим корректность введеных фио(только буквы и тире) и игноркэйс для отвязки от регистра
#         # при помощи регулярных выражений(В квадратных скобкам это один любой символ)
#         # и метон джойн соеденим строки фио в одну и пройдемся в цикле
#         # проверив введены ли допустимы символы в тех данных которые ввел пользователь
#         letters = "".join(re.findall('[a-zа-яё-]', fio, re.IGNORECASE))
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError('В ФИО можно использовать только буквы и дефис')
#
#     # создадим декоратор и метод проверки года рождения
#     # проверим методом isinstance на соответсвие целого числа в графе возраст.
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old,
#                           int) or old < 14 or old > 120:  # если в олд не целое число то будет  или диапазон возраста не подходит
#             raise TypeError('Возраст должен быть целым числом в диапазоне от 14 до 120 лет')
#
#     # Проверим вес
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError('Вес должен быть вещественным числом и от 20 кг и выше')
#
#     # Проверим паспортные данные
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError('Паспорт должен быть строкой')
#         # Проверим что в 1 элементе только 4 символа а во 2 элем только 6 символов (по индексу укажем)
#         # - разобьем его на список с элементами и проверим длину списка(должно быть 2 элемента серия и номер)
#         s = ps.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError('Не верный формат паспорта')
#         # Проверим на наличие букв с помощью метода в цикле
#         for p in s:
#             if not p.isdigit():  # Все что не цифра
#                 raise TypeError('Серия и номер паспорта должны быть числами')
#
#
# #  Сразу Создадим экземпляр класса что бы мы могли видоизменть что то
# #  что будет неправильно и передадим в него данные человека
# p1 = UserData('Волков Игорь Николаевич', 26, '1234 567890', 80.8)
# # Заменим отчество
# p1.fio = 'Волков Игорь Викторович'
# print(p1.fio)
# # Заменим возраст
# # p1.old = '26'
# # print(p1.old)
# # выше проверили что отрабатывают ошибки(исключени)
# p1.old = 26
# print(p1.old)
# p1.weight = 78.8
# print(p1.weight)
# p1.password = '4321 098765'
# print(p1.password)


######--------------------- Урок 28 --------------------------- ООП Наследование

#
# # Создадим класс наследник который будет иметь доступ ко всем свойствам и методам родительского класса
# # 1 Это просто пример
# # class Point:
# #     def __init__(self, x=0, y=0):
# #         self.__x = x
# #         self.__y = y
# # # Является ли клас который передается первым наследником который передается вторым
# # print(issubclass(Point, object))
# # print(issubclass(Point, int))
#
# # 2 Создадим класс линия с двумя точками на плоскости и цветом и толщиной линии
# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):  # при обращении к какому то экземпляру класса,
#         # показывает что нарисовали (магический метод)
#         return f'({self.__x}, {self.__y})'
#
#
# # Создадим общий класс для классов линий и прямоугольников и будем указывать его в скобках этих классов
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red',
#                  width: int = 1):  # укажем какой тип данных должен поступать через дветочие - это используется как рекомендация для использование этого класса
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width  # если свойство делаем закрытым то прописываем геттеры и сетеры ниже
#         print('Инициализатор базового класса Prop ')
#     def get_width(self):  # обращение по названию - self.get_width()
#         return self.__width
#
#
# class Line(Prop):
#     def __init__(self,*args):  # Попробуем создать свой инициализатор
#         print('Переопределенный инициализатор Line')
#         # Prop.__init__(self, *args)
#         super().__init__(*args)  # получает доступ к еэементу над ним к родительскому элементу
#     def draw_line(self):  # Это класс создающий линию
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.get_width()}')
#
#
# # создадим еще класс рисование прямоугольника
# # class Rect(Prop):
# #     def draw_rect(self):  # Это класс создающий линию
# #         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.get_width()}')
#
#
# line = Line(Point(1, 2), Point(10, 20), 'yellow',5)  # Координаты точки поинт так как там два параметра(На пересечении икса и игрика)
# line.draw_line()
# # print()
# # print(line.get_width())  # доступ к закрытому свойству с двумя подчеркиваниями(__)
# # print()
# # print(line._color)  # проверка что получаем доступ (_) к цвету за пределами класса к одному подчеркиванию
# # print()
# # rect = Rect(Point(30, 40), Point(70, 80))
# # rect.draw_rect()


# Создадим класс для рисования фигур,и укажем общее св-во. цвет
# но какие именно фигуры будут рисовать мы укажем в классе наследнике


# class Figure:  # родительский класс
#     def __init__(self, color):
#         self.__color = color
#     @property  # создадим геттеры и сеттеры для цвета что бы получать к цвету доступ
#     def color(self):
#         return self.__color
#     @color.setter
#     def color(self, c):
#         self.__color = c
# class Rectangle(Figure):  # это класс треугольник,с высотой и шириной,
#     # а так же цветом доступ к которому мы получили от родительского класса.
#     # мы своим дочерним классом расширили то что есть в родительском классе
#     def __init__(self,width, height, color):
#         self.width = width
#         self.height = height
#         super().__init__(color)
#         # раз свойства закрытые то сделаем проверки,но потом откроем их что бы отрабатывали проверки в сеттэрах
#     @property
#     def width(self):  # вернем ширину
#         return self.__width
#     @width.setter
#     def width(self, w):  # сделаем проверку для вводимых значений
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError('Некорректное значение высоты')
#     @property
#     def height(self):  # вернем ширину
#         return self.__height
#     @height.setter
#     def height(self, h):  # сделаем проверку для вводимых значений
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError('Некорректное значение ширины')
#     def area(self):  # вернем полощадь прямоугольника
#         print(f'Площадь {self.color} прямоугольника = ', end="")  # вернем полное описание фигуры
#         return self.__width * self.__height

# rect = Rectangle(10, 20, 'green')
# print(rect.area())
###################################

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):  # при обращении к какому то экземпляру класса,
#         # показывает что нарисовали (магический метод)
#         return f'({self.__x}, {self.__y})'
#     def is_digit(self):  # создадим во вспомогательном классе вспомогательный метод для замены значений x и y
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#     def is_int(self):  # создадим во вспомогательном классе вспомогательный метод для замены значений x и y
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):  # укажем какой тип данных должен поступать через дветочие - это используется как рекомендация для использование этого класса
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width  # если свойство делаем закрытым то прописываем геттеры и сетеры ниже
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print('Координаты должны быть числами')
# class Line(Prop):
#     def set_coord(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print('Координаты должны быть целочисленными значениями ')
#     def draw_line(self):  # Это класс создающий линию
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
# # создадим еще класс рисование прямоугольника
# class Rect(Prop):
#     def draw_rect(self):  # Это класс создающий линию
#         print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# line = Line(Point(1, 2), Point(10, 20), 'yellow',5)  # Координаты точки поинт так как там два параметра(На пересечении икса и игрика)
# line.set_coord(Point(15, 45), Point(100, 200))  # изменим рисование линии
# line.draw_line()
# print()
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.set_coord(Point(55.5, 45.6), Point(100, 200))  # переопределим параметры прям-ка, рект ищет сеткурд в классе рекс и не находит ,значит он видит что рект наследуется от проп и идет тогда в проп и унего находит метод которые проверяет исдиджест(возможность ввода целых чисел)
# rect.draw_rect()


## Пример как работает наследование с доступом к методам

# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):  # выведем параметры прям - ка
#         print(f'Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}')
#
#
# class RectFon(Rect):  # этот класс наследуется от рект
#     def __init__(self, width, height, background):
#         self.fon = background
#         super().__init__(width, height)  # получаем доступ к ширине и высоте
#
#     def show_rect(self):
#         super().show_rect()
#         print('Фон:', self.fon)
# class RectBorder(Rect):
#     def __init__(self, width, height, a, b, c):
#         super().__init__(width, height)
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def show_rect(self):
#         super().show_rect()
#         print(f'Толщина линий: {self.a}\nРамка: {self.b}\nЦвет: {self.c}')
#
#
# shape1 = RectFon(400, 200,'yellow')
# shape1.show_rect()
# print()
# shape2 = RectBorder(600, 300, '1px', 'solid', 'red')
# shape2.show_rect()


# Наследование не только от своих типах данных а от любых,которые уже существуют

# class Vektor(list):
#     # def __init__(self, lst):
#     #     super().__init__()
#     #     self.lst = lst
#
#     def __str__(self):
#         return " ".join(map(str, self))
#
#
# v = Vektor([1, 2, 3])
# print(sum(v))
# print(v)
# print(type(v))


###############- Перегрузка методов-№№№№№№№№№№№№№№№№№№


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):  # при обращении к какому то экземпляру класса,
#         # показывает что нарисовали (магический метод)
#         return f'({self.__x}, {self.__y})'
#     def is_digit(self):  # создадим во вспомогательном классе вспомогательный метод для замены значений x и y
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#     def is_int(self):  # создадим во вспомогательном классе вспомогательный метод для замены значений x и y
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):  # укажем какой тип данных должен поступать через дветочие - это используется как рекомендация для использование этого класса
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width  # если свойство делаем закрытым то прописываем геттеры и сетеры ниже
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print('Координаты должны быть числами')
# class Line(Prop):
#     def draw_line(self):  # Это класс создающий линию
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#     def set_coord(self, sp=None, ep=None):  # если приходит только одна координата и другая имеет значение ноне то мы будем менять только первую координату
#         if ep is None:
#             if sp.is_int():
#                 self._sp = sp
#             else:
#                 print('Координата sp должна быть целочисленным значением ')
#         elif sp is None:
#             if ep.is_int():
#                 self._ep = ep
#             else:
#                 print('Координата ep должна быть целочисленным значением ')
#         else:
#             if sp.is_int() and ep.is_int():
#                 self._sp = sp
#                 self._ep = ep
#             else:
#                 print('Координаты должны быть целочисленными значениями ')
#
#
# # с помощью перегрузки методов мы можем вызывать либо одну либо две координаты
#
# line = Line(Point(1, 2), Point(10, 20), 'yellow',5)  # Координаты точки поинт так как там два параметра(На пересечении икса и игрика)
# line.draw_line()
# print()
# line.set_coord(Point(15, 45), Point(100, 200))  # изменим рисование линии
# line.draw_line()
# print()
# line.set_coord(Point(550, 55))
# line.draw_line()
# print()
# line.set_coord(ep=Point(90, 20))
# line.draw_line()


###-Абстрактные методы


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):  # при обращении к какому то экземпляру класса,
#         # показывает что нарисовали (магический метод)
#         return f'({self.__x}, {self.__y})'
#     def is_digit(self):  # создадим во вспомогательном классе вспомогательный метод для замены значений x и y
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#     def is_int(self):  # создадим во вспомогательном классе вспомогательный метод для замены значений x и y
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):  # укажем какой тип данных должен поступать через дветочие - это используется как рекомендация для использование этого класса
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width  # если свойство делаем закрытым то прописываем геттеры и сетеры ниже
#     def draw(self):  # это создаем при условии что где то будет удален метод дров и поставленно 3 точки за место него
#         raise NotImplementedError('В дочернем кслассе должен быть определен метод draw()')
# class Line(Prop):
#     def draw(self):  # Это класс создающий линию
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
# class Rect(Prop):
#     def draw(self):  # Это класс создающий линию
#         print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}')
# class Ellipcs(Prop):
#     # def draw(self):  # Это класс создающий линию
#     #     print(f'Рисование эллипса: {self._sp}, {self._ep}, {self._color}, {self._width}')
#     ...
# # Создадим список и с помощью метода будем добавлять в конец его координаты из классов
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(20, 10)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellipcs(Point(-10, -10), Point(10, 10)))
#
# # Теперь в цикле пройдемся по списку из координати методом дров нарисуем линии
# for f in figs:
#     f.draw()

####-------------------Урок28-----------------------------
#
from math import pi
from abc import ABCMeta, abstractmethod, ABC


class Table(metaclass=ABCMeta):
    def __init__(self, width=None, height=None, radius=None):
        if radius is None:
            self.table_type = 'прямоугольный'
            self.width = width
            self.height = height
        else:
            self.table_type = 'круглый'
            self.radius = radius

    def __str__(self):
        description = f'Форма стола: {self.table_type}\n'
        if self.table_type == 'прямоугольный':
            return (
                description +
                f'Ширина стола: {self.width}\n'
                f'Высота стола: {self.height}'
            )
        else:
            return (
                description +
                f'Радиус стола: {self.radius}'
            )

    @abstractmethod
    def square(self):
        pass


class RectangleTable(Table):
    def __init__(self, width, height):
        super().__init__(
            width=width,
            height=height
        )

    def square(self):
        return self.width * self.height


class CircleTable(Table):
    def __init__(self, radius):
        super().__init__(radius=radius)

    def square(self):
        return round(pi * self.radius ** 2, 2)


tables = [
    RectangleTable(20, 10),
    RectangleTable(20, 20),
    CircleTable(radius=20),
]

for table in tables:
    print(table)
    print(f'Площадь стола: {table.square()}\n')


########################### урок 28 по видео
# import math
#
#
# class Stol:
#     pass
#
#
# class PStol:
#     forma = "prymougolnui"
#     width = 'widthh'
#     height = 'heightt'
#     year = 2020
#     # x: float = 17.8  # 1 z
#     x: float = 5.  # 2,3 z
#     y: float = 7.  # 2,3 z
#
#
# class KStol:
#     forma = 'kruglui'
#     radius = 'radiuss'
#     c: float = 5.
#
#     def hello(x):
#         print('HELLO')
#         return 'hello'
#
#     def world():
#         print(2 + 3)
#         return 'world!!!'
#
#     def calc_sum(c, num_1, num_2):
#         print(num_1 + num_2)
#
#     def setnum(self):
#         self.x = 20
#
#     # 23 создадим два атрибута
#     def set_value(self, x, y):
#         self.x = x
#         self.y = y
#
#     # 23 создадим сложение атрибутов
#     def send_sum(self):
#         return self.x + self.y
#
#     # 24 инициализируем рост и имя и при вызове класса будем их вводить
#     def __init__(self, height: int, name: str):
#         self.height: int = height
#         self.name: str = name
#
#     # 25 создадим шаблон с параметрами год и имя
#     def __init__(self, age: int, name: str):
#         self.age: int = age
#         self.name: str = name
#
#     # 26 инициализируем нужные параметры для вычисления треугольника
#     def __init__(self, a: float, b: float, c: float):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     # 26 создаем метод вычисления треугольника
#     def check_equals(self):
#         return self.a == self.b or self.b == self.c or self.a == self.c

#############################################################################
# 26 проверка что треугольник равнобедренный
# t = KStol(1, 10, 1.1)  # создаем экземпляр и вводим парамерты треугольника
# print('равнобедренный' if t.check_equals() else 'неравнобедренный')  # если параметры проходят проверку то выводится нужно значение


# 25 покажем двух различных людей
# p1 = KStol(15, 'ted')
# p2 = KStol(22, 'kop')
# print(p1.name, p2.name)
# print(p1.age, p2.age)


# 24 создадим экземпляр и вызовем инициализируемые объекты
# a = KStol(179, 'bob')
# print(a.__dict__)
# print(a)


# 23 вычисляем сумму
# a = KStol()
# a.set_value(5, y=2)  # сначало введем данные
# result = a.send_sum()  # теперь сложим и выведем на экран
# print(result)


# ps = PStol()
# ks = KStol()


# 23
# a = KStol()
# a.setnum()  # добавляем в область видимости функцию(ссылка на экземпляр )
# b = KStol()
# print(a.__dict__)
# print(b.__dict__)  # а тут не будет видно так как не добавили функцию


# 22
# self формальный параметр функции, его параметр передается экземпляру

# 21 выведем функцию сложения
# m = KStol()
# m.calc_sum(9,8)

# 20 вызов функции через экземпляр класса, обязательно ставить скобочки после названия класса - двумя способами
# KStol().hello()
# # или так в качестве аргумента ставим экземпляр
# KStol.hello(KStol())
# # гораздо проще создавать екземпляр и через него вызывать атрибуты
# p = KStol()
# p.hello()

# 19 вызов функции через класс без аргумента
# KStol.world()

# 18 если вызов функции через экземпляр то нужен обязатено указывать аргумент в самой функции
# p = KStol()
# p.hello()
# # если вызывать функцию через название класса то будет ошибка и тогда в качестве аргумента функции указывается экземпляр (при указанном аргументе в функции в классе)
# KStol.hello(p)

# 17 функция в классе является его атрибутом,вызовем две функции (разными способами) и составим предложение
# print(KStol.hello() + ' ' + getattr(KStol, 'world')())

# 16
# при удалении не существующего атрибута выведем надпись об этом
# try:
#     del KStol.name
# except AttributeError:
#     print('такого атрибута не существует')
# del KStol.name

# 15
# если изменим год то количество столов уменьшается на 2 (это будет х)
# PStol.year += 1
# PStol.x -= 2
# print(PStol.__dict__)

# 14
# найдем площадь круга и прямоугольника использууя модуль для пи
# print(math.pi * KStol.c**2)
# print()
# print(PStol.x * PStol.y)

# 13 создадим класс, потом экземпляр в котором создадим атрибут,который не виден в классе
# a = PStol()
# a.c = 'hello'
# print(PStol.__dict__, a.__dict__, sep='\n')
# # так же заменим значение атрибута в классе
# setattr(PStol, 'x', 15987)
# print(PStol.x)

# 12
######## создадим экземпляр и заменим в нем знаечение атрибута  и выведем посмотреть
# ps = PStol()
# setattr(ps, 'forma', 21)
# print(getattr(PStol,'forma'))
# print(ps.__dict__, ps.forma)


# 11
###### выведем значение атрибутов двумя способами а так же удалим один атрибут из класса(в анотациях он бы сохранился)
# # 1
# print(getattr(PStol,'forma'), getattr(KStol,'forma'), sep='\n')
# # 2
# print(PStol.forma, KStol.forma, sep='\n')
# #
# del PStol.width
# print(PStol.__dict__)  # удостоверимся что атрибут удалился

# 10
################## создадим 2 экземпляра класса и потом в одном экземпляре изменим значение арибута а в другом добавим атрибут
# и выведем посмотреть что в них находится что бы удостоверится что где
# stol_1 = PStol()
# stol_2 = PStol()
#
# stol_1.width = 'gyd'
# print(stol_1.__dict__)
# stol_2.color = 'grey'
# print(stol_2.__dict__)
# stol_1.x = 150
# print(stol_1.__dict__)
#
# print(PStol.__dict__)

# 9 область видимости, создаем два экземпляра класса для одного класса
# a = KStol()
# b = KStol()
# создадим динамически два атрибута
# a.colory = 'black'
# b.colory = 'green'
# поменяем значение имеющегося статического атрибута
# a.forma = 165
# print(a.__dict__, b.__dict__, KStol.__dict__, sep='\n')  # в глобальном классе не чего не добавилосьбтолько локально создались атрибуты которые не видны в классе


# 8 обращение к атрибутам класса через экземпляры_______________ 8  урок
# ps = PStol()
# ks = KStol()
# print(ps.height, ks.radius)

############ 1 zadanie
# PStol.y = 'yes'  # создаем динамический  новый атрибут
# print(PStol.y)
# print()
# del PStol.x  # удаляем статический атрибут из класса и его значение пропадает а название остается
# print(PStol.__dict__)
###############

############### 2 zadanie
# print(getattr(PStol, 'x') + getattr(PStol, 'y'))  # сложим два атрибута
# print(getattr(PStol, 'z', 'Такого числа не существует'))  # выведем сообщение если вводим не существующий атрибут
##############

############## 3 zadanie создаем динамически 2 атрибута двумя способами
# setattr(Stol, 'f', 'kvadrat')
# Stol.g = 'htlo world'
# print(getattr(Stol, 'g').upper())  # выведем атрибут в верхнем регистре
# print(Stol.__dict__)
##############


############# 4 zadanie удалим 2 атрибутф и выведем сообщение что его не существует, двумя способами
# del PStol.x
# print(getattr(PStol, 'x', 'не существует такого атрибута'))
# delattr(PStol, 'y')
# print(getattr(PStol, 'y', 'нет атрибута'))
#############


# print(PStol.forma)
# print()

# 7
# print(PStol.__dict__)

# 6
# при несуществующем атрибуте выводим нужную надпись
# print(getattr(PStol, 'x', 'не существует такого атрибута'))
# print()

# 5
# меняем значение атрибута
# setattr(PStol, 'forma', 'kvadrat')
# print(PStol.forma)

# 4
# динамическое создание атрибута
# так
# setattr(PStol, 'f', 'kvadrat')
# print(PStol.f)
# # или так
# PStol.f = 15
# print(PStol.f)
# print()

# 3
# удаление атрибутов
# так
# del PStol.forma
# print(PStol.forma)
# или так
# delattr(PStol, 'forma')
# print(PStol.forma)
# print()

# 2
# проверяем тип объекта
# print(type(ps), type(ks), sep='\n')
# print()
# проверяем принадлежность к классу
# print(isinstance(ps, PStol))
# print(isinstance(ps, KStol))
# print()

# 1
# print(isinstance(5, str))
# print(isinstance('cat', str))
# print(isinstance([1, 2, 3], str))
# print()


#####################################################################################################################
# Строение класса
# class Cat:
#     age: int = 2  # статические атрибуты / атрибуты класса / состояние класса / свойства класса
#     breed: str = 'Bengal'
#
#     def __init__(self, color: str):  # конструктор класса / метод инициализации экземпляра / атрибут класса
#         self.color: str = color  # динамический атрибут / локальные свойства / атрибут экземпляра /состояние объекта
#
#     def meow(self) -> None:  # метод
#         print('Мяу')
#
# # вызываем мяу 2 способа
# # 1
# tom = Cat('blask')
# Cat.meow(tom)
# # 2
# getattr(Cat, 'meow')(tom)
# # смотрим что том динамически создан и имеет только цвет
# print(tom.__dict__)
# print(Cat.__dict__)


# задача 2 создать класс персон ,добавить динамически атрибут и удалить его
# import pprint
#
# class Person:
#     name: str = 'MAx'
#     age: int = 37
#
#
# setattr(Person, 'color', 'green')
# pprint.pprint(Person.__dict__)  # видим что добавили
#
# print(getattr(Person, 'color', 'нет такого атрибута'))
#
# delattr(Person,"color")
#
# pprint.pprint(Person.__dict__)


# задача 3 класс компьютер с атрибутами,выводим число пи,смотрим прокси,удалить атрибут двумя способами
import pprint
import math

# class Comp:
#     age: int = 5
#     price: int = 200
#     size: str = 'big'
#
#
# print(getattr(Comp, 'sdf', str(math.pi)))  # выводим пи
# pprint.pprint(Comp.__dict__)
# #  удаляем и проверяем
# del Comp.price
# delattr(Comp, 'size')
# pprint.pprint(Comp.__dict__)


# 4 задача класс с атрибутами,создание динамическиго атрибута,проверить этот атрибут метотом гетаттриб -является ли он статическим(есть ли в классе)
# class Person:
#     name: str = 'liza'
#     age: int = 12
#
#
# l = Person()  # создадим экземпляр
# l.color = 'blue'
# print(getattr(Person, 'color', 'не является статическим'))
# print(isinstance(Person, type), isinstance(l, int), sep='\n')  # проверяем тип класса и экземпляра -не принадлежит к классу тип и int


# 5 задача
"""Создайте класс, объявите внутри него пустую функцию.
Динамически подключите к классу новый атрибут со значением 5.
Проверьте, является ли данный атрибут - свойством конкретного экземпляра данного класса.
Обратитесь к данной функции и выведите результат обращения.
"""

# class A:
#     def send():
#         pass
#
#
# A.attr = 5
# a = A()
# # a.color = 6
# # print(a.color in a.__dict__)
# print(A.attr in a.__dict__)  #  является ли данный атрибут - свойством конкретного экземпляра данного класса.
# print(A.send)  # Обратитесь к данной функции


# 6 задача тут функция является методом
"""Создайте класс, реализуйте внутри него метод, выводящий сумму двух чисел по входным данным.
Вызовите данную функцию относительно некоторых значений её параметров и отобразите результат на экране.
"""
# class B:
#     def add(self, x: float, y: float) -> float:
#         return x + y
#
# a = B()
# print(a.add(15., 15.))


# 7 задача
"""Объявите класс, внутри создайте метод экземпляра класса, который будет динамически
подключать к экземпляру два новых атрибута.
Реализуйте внутри класса новый метод экземпляра, который будет выводить сумму двух чисел
по входящим значениям.
Вызовите и обратитесь к данной функции через посредство класса и созданного экземпляра. Что вы заметили в данных случаях?
"""

# class A:
#     def add(self, a: float, b: float) -> float:  # последнее флойд означает что функция возвращает число с точкой
#         return a + b
#
# A.x = 5
# A.y ='hello'
#
# print(A.add(A(), 25., 25.))

# 8  задача
"""Реализуйте следующий класс -
Внутри класса имеются два произвольных атрибута, принимающих некоторые значения,
 пусть это будут статические атрибуты класса.
Создайте функцию-метод экземпляра класса, которая будет дублировать данные атрибуты
класса для экземпляра.
Обратитесь к атрибуту __dict__, созданного экземпляра, чтобы отобразить их значения.
"""


# class A:
#     x = 4
#     y = 2
#
#     def dublicate(self):  # через селф присваиваем значениям метода статические значения класса!!!
#         self.x = self.x
#         self.y = self.y
#
#
# a = A()  # создаем екземпляр и смотрим что внем не чего нет
# print(a.__dict__)
# a.dublicate()  # теперь в эеземпляре вызовом метода создаем дублирующие атрибуты
# print(a.__dict__)  # теперь тут есть атрибуты которые дублируются с класса в экземпляр


# 9 задача не понятное решение с ошибкой

# class A:
#     def __int__(self, x):  # функция не чего не возвращает
#         self.x = x
#         self.y = 'default'
#
#
# a = A()
# print(a.__dict__)


# 10 задача метод вычисления окружностей - не работает пишет не принимает аргументов
# class Circumference:
#     def __init__(self, radius: float) -> None:
#         self.radius = radius
#
#     def calc_square(self) -> float:
#         return math.pi * self.radius**2
#
#
# c = Circumference(1.)
# print(c.calc_square())


# classmethod
# class A:
#     x = 5
#     y = 2
#
#     def __init__(self, a):
#         self.a = a
#     # @classmethod
#     # def sud(cls):
#     #     return cls.x - cls.y
#     @classmethod
#     def cud(cls):
#         return cls(13)
#
#
# # print(A.sud())
# print(A.cud().__dict__)


###################################################### уроки  selfedu
# class Point:
#     color = 'red'
#     circle = 2
#
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_coords(self):
#         return self.x, self.y
#
#
# pt = Point(1,2)
#
# print(pt.__dict__)


### Пример класса Person
# from string import ascii_letters
#
#
# class Person:
#     S_RUS = 'абвгдеёжзклмнопрстуфхцчшщьыъэюя-'
#     S_RUS_UPPER = S_RUS.upper()  # переводим все буквы выше в верхний регистр
#
#     def __init__(self, fio, old, ps, weight):
#         self.verify_fio(fio)
#
#         self.__fio = fio.split()
#         self.__old = old
#         self.__ps = ps
#         self.__weight = weight
#
#     # пропишем несколько вспомогательных методов класса для проверки коректности каждого переданного значения
#     # если тип фио не строка выведем ошибку
#     @classmethod
#     def verify_fio(cls, fio):
#         if type(fio) != str:
#             raise TypeError('ФИО должно быть строкой')
# # далее разобьем стоку фио что бы было все через пробел написанно,на выходе получим список из фио
# #  проверим что длина этого списка равна 3,если не равна то выведем исключение.
#         f = fio.split()
#         if len(f) !=3:
#             raise TypeError('Неверный формат ФИО')
# # что в фио используются только буквы и дефис.для этого создадим строку
# # где указывается какие символы должны использоваться,применяя иморт модулу и заранее подготовив свойства класса
#         letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
# # затем в цикле проверим имеются ли хотя бы один символ
#         for s in f:
#             if len(s) < 1:
#                 raise TypeError('В ФИО должен быть хотя бы один символ')
#             if len(s.strip(letters)) != 0:
#                 raise TypeError('В ФИО можно использовать только буквы и дефис')
# p = Person('Семенов Александр Викторович', 39, '1234 567890', 89.0)

####################################################################
# class Geom:
#     name = 'Geom'
#
#     def __init__(self, x1, y1, x2, y2):
#         print(f'инициализатор Geom для {self.__class__}')
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
#
#
# class Line(Geom):
#
#     def draw(self):
#         print('Рисование линии')
#
#
# class Rect(Geom):
#     def __init__(self, x1, y1, x2, y2, fill=None):
#         super().__init__(x1, y1, x2, y2)
#         print('инициализатор Rect')
#         self.fill = fill
#
#     def draw(self):
#         print('Рисование прямоугольника')
#
#
# l = Line(0, 0, 10, 20)
# r = Rect(1,2,3,4)