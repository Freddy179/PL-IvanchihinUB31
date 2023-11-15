# Вариант 1
# 1
# from random import randint # формируем матрицу с рандомными числами
# N = int(input())
# A = []
# for i in range(N):
#     A.append([randint(-10, 10)] * N)
# for i in range(N):
#     for j in range(N):
#         print(A[i][j], end = ' ')
#     print()

# zsum = 0
# zcount = 0
# for i in range(N):
#     for j in range(N):
#         if i == j: # если число в главной диагонали
#             if A[i][j] >= 0: 
#                 zsum+=int(A[i][j])
#                 zcount+=1
# print(zsum, zcount)

# 2
# from random import randint
# N = int(input('Кол-во строк: '))
# M = int(input('Кол-во солбцов: '))
# A = []
# for i in range(M): # формируем матрицу
#         b = []
#         for j in range(N):
#             b.append([randint(-10, 10)])
#         A.append(b)
# print('Исходный массив:')
# for p in range(M): # выводим матрицу
#     for k in range(N):
#         print(A[p][k], end = ' ')
#     print()

# for i in A: # Ищем максимальное и минимальное число
#      for j in [i]:
#         maximum = max(i) # Максимальное число и его индекс
#         maI = i.index(maximum)
#         minimum = min(i) # Минимальное число и его индекс
#         miI = i.index(minimum)
#         i[maI], i[0] = i[0], i[maI] # Замена максимального и первого
#         i[miI], i[-1] = i[-1], i[miI] # Замена минимального и последнего
# print('Измененный массив:')
# for p in range(M):
#     for k in range(N):
#         print(A[p][k], end = ' ')
#     print()

# Вариант 3
# 1
from random import randint
N = int(input())
a = []
for i in range(N): #формируем матрицу
    b = []
    for j in range(N):
        b.append([randint(-10, 10)])
    a.append(b)
for p in range(N): # выводим матрицу
    for k in range(N):
        print(a[p][k], end=' ')
    print()

for p in range(N): 
    for k in range(N):
        if a[p][k] != a[k][p]:
            z = 'F'
            break
if z!='F':
    print('Матрица симметрична')
else:
    print('Матрица несимметрична')

# # 2
# from random import randint  # доделать
# N = int(input())
# M = int(input())
# a = []
# for i in range(N): #формируем матрицу
#     b = []
#     for j in range(M):
#         b.append([randint(-10, 10)])
#     a.append(b)
# for p in range(N): # выводим матрицу
#     for k in range(N):
#         print(a[p][k], end=' ')
#     print()
# d = 0
# spisok_strok = []
# spisok_stolbc = []
# for i in a:
