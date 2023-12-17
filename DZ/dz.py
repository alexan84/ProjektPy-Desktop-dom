# DZ 3 (18.11.23)
a = int(input("Число символов: "))
b = input("Тип символов: ")
c = int(input("Ориентация строки 0 или 1: "))
i = 0
while i < a:
    if c == 0:
        print(b, end=" ")
        i += 1
    else:
        print(b, end="\n")
        i += 1





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