# Вариант 1
# 1
# from math import *
# def S_Fihure(type,*args):
#     if type == 1: # Круг
#         r = int(str(args)[1:-2])
#         return pi*r**2
#     elif type == 2:
#         l = list(args[:-1])
#         z = 1
#         for i in l:
#             z*=i
#         return (z/2) * sin(args[-1])
#     elif type == 3:
#         l = list(args)
#         z = 1
#         for i in l:
#             z*=i
#         return z
#     elif type == 4:
#         z = args[0] + args[1]
#         return (z/2) * args[-1]
# answ = int(input('''Введите номер фигуры:
#                  1 - Круг
#                  2 - Треугольник
#                  3 - Четырехугольник
#                  4 - Трапеция
#                  : '''))
# if answ == 1:
#     rad = int(input('Введите радиус: '))
#     print(S_Fihure(1, rad))
# elif answ == 2:
#     lenght = int(input('Введите длину первого катета треугольника: '))
#     hight = int(input('Введите длину второго катета треугольника: '))
#     alf = int(input('Введите угол между катетами (от 1 до 180): '))
#     print(S_Fihure(2, lenght, hight, alf))
# elif answ == 3:
#     lenght = int(input('Введите длину основания четырехугольника: '))
#     weight = int(input('Введите длину боковой стороны четырехугольника: '))
#     print(S_Fihure(3, lenght,))
# elif answ == 4:
#     f_osn = int(input('Введите длину большего основания: '))
#     s_osn = int(input('Введите длину меньшего основания: '))
#     hight = int(input('Введите длину высоты:'))
#     print(S_Fihure(4, f_osn, s_osn, hight))

#2
# a = [1,2,3,4,5,6,1,9,2,]
# b = [18,27,98,78,67,54]
# c = [196,26,7,280,17]
# def summa(*args):
#     s = list(args)
#     z1 = 0
#     z2 = 0
#     for i in s:
#         for j in i:
#             z1+=int(j)
#             z2+=1
#     return z1, z1/z2
# abc = []
# abc.append(a), abc.append(b), abc.append(c)
# for i in abc:
#     print(summa(i))

# Вариант 2
# 1
# from math import sqrt
# def sixangle(a):
#     return (sqrt(3)*3*a**2)/2
# lenth = int(input('Введите длину стороны шестиугольника: '))
# print(sixangle(lenth))

# 2
# lenth = []
# weight = []
# for i in range(3):
#     lenth.append(int(input()))
#     weight.append(int(input()))
# print('Длины четырехугольников: ')
# print(lenth)
# print(weight)
# for i in range(3):
#     a = lenth[i]
#     b = weight[i]
#     print(a*b)

# Вариант 3
# 1
# a = []
# b = []
# def Gipot(*args):
#     z = list(args)
#     k = 0
#     for i in z:
#         k+=(i**2)
#     return k
# if Gipot(a) < Gipot(b):
#     print('Первая гипотенуза больше')
# elif Gipot(a) < Gipot(b):
#     print('Вторая гипотенуза больше')
# else:
#     print('Гипотенузы равны')

# 2
# stroka = 'Дима дома жарит котлеты'
# strok = stroka.lower()
# st = strok.split()
# for i in st:
#     l = list()
#     for j in i:
#         l.append(j)
#     print(l.sort())
#     print(l)