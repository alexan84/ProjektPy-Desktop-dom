# print("hello!!!!")
# print("Привет")

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


# * Цикл For

# for element in collection:
#    print(element)

# for element in range(n):
#     print(element)

# print(list(range(5)))

# range(start, stop, step))  # start=0 step=0

# * Пример использования цикла
# for i in range(9):
#     print(i, end=" ")
#
# print()

# тут же запускаем вайл для паралельного сравнения циклов
# i = 0
# while i < 9:
#     print(i, end=" ")
#     i += 1


# * Задача на уроке - вводится число и нужно вывести все целые числа на которое заданное число делится без остатка
# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")


# * Задача на уроке - вывести целые числа в диапазоне от 10 до 100 у которых есть одинаковые две цифры
a = 100
for i in range(10, 100):
    if i % 10 == i // 10:
        print(i, end=" ")

