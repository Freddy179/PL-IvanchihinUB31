# 1
# from random import randint
# f1 = open('C:/Program Files/IvanchihinUB31vvod.txt', 'w')
# N = int(input())
# a = []
# for i1 in range(N):               # Формируем квадратную матрицу
#     b = []
#     for j1 in range(N):
#         b.append(randint(-10, 10))
#     a.append(b)
# for k1 in a:                      # Записываем матрицу в файл
#     f1.write(str(k1)[1:-1] + '\n')

# f1.close()
# f1 = open('C:/Program Files/IvanchihinUB31vvod.txt', 'r')
# f2 = open('C:/Program Files/IvanchihinUB31vivod.txt', 'w')

# l1 = f1.read().rstrip().split('\n') # открываем файл, что бы получить список строк
# print(l1)
# zsum = 0
# zcount = 0
# count_index = 0 # count_index выступает за индекс главной диагонали. Числа главной диагонали начинаются с 0 и на каждой строке оно больше на 1
# for i in l1:
#     i = i.split(', ') # удаляем все запятые в строках ибо без строк сложно считывать
#     print()
#     for j in i:
#         if i.index(j) == count_index and int(j) >= 0: # если число на главной диагонали
#             zsum += int(j)
#             zcount += 1
#     count_index+=1 # увеличиваем значение индекса
# print(zcount, zsum)
# f2.write('Количество чисел: ' + str(zcount) + ' ' + '\n' + 'Сумма чисел:' + ' ' + str(zsum))
# f1.close()
# f2.close()

# 2
from random import randint
N = int(input('Кол-во столбцов: '))
M = int(input('Кол-во строк: '))
f1 = open('C:/Program Files/IvanchihinUB31vvod.txt', 'w')
a = []
for i1 in range(M):               # Формируем матрицу
    b = []
    for j1 in range(N):
        b.append(randint(-10, 10))
    a.append(b)
for k1 in a:                    # Записываем матрицу в файл
    f1.write(str(k1)[1:-1] + '\n')

print('Исходный массив:')
for p in range(M):                # выводим матрицу
    for k in range(N):
        print(a[p][k], end = ' ')
    print()
f1.close()

f1 = open('C:/Program Files/IvanchihinUB31vvod.txt', 'r')
f2 = open('C:/Program Files/IvanchihinUB31vivod.txt', 'w')

l1 = f1.read().rstrip().split('\n')
for q1 in l1:
    q1 = q1.split(', ') # удаляем ненужные запятые
    l2 = list() # список для чисел
    for q2 in q1: # запихиваем int числа строки в список
        q2 = int(q2)
        l2.append(q2)
        # меняем строку
        maximum = max(l2) # Максимальное число и его индекс
        maI = l2.index(maximum)
        minimum = min(l2) # Минимальное число и его индекс
        miI = l2.index(minimum)
        l2[maI], l2[0] = l2[0], l2[maI] # Замена максимального и первого
        l2[miI], l2[-1] = l2[-1], l2[miI] # Замена минимального и последнего
    print(l2)
    f2.write(str(l2) + '\n')

f1.close()
f2.close()