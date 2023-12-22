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
#
# # for i, j in d.items():
# #     print(i, '->', j)
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




















