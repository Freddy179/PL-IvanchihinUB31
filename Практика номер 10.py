# 1
# from random import randint
# f1 = open('C:/Program Files/IvanchihinUB31vvod.txt', 'w')
# N = int(input())
# a = []
# for i1 in range(N):              
#     b = []
#     for j1 in range(N):
#         b.append(randint(-10, 10))
#     a.append(b)
# for k1 in a: 
#     f1.write(str(k1)[1:-1] + '\n')

# f1.close()
# f1 = open('C:/Program Files/IvanchihinUB31vvod.txt', 'r')
# f2 = open('C:/Program Files/IvanchihinUB31vivod.txt', 'w')

# l1 = f1.read().rstrip().split('\n') 
# zsum = 0
# zcount = 0
# count_index = 0 
# for i in l1:
#     i = i.split(', ') 
#     print()
#     for j in i:
#         if i.index(j) == count_index and int(j) >= 0: 
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
for i1 in range(M):
    b = []
    for j1 in range(N):
        b.append(randint(-10, 10))
    a.append(b)
for k1 in a:
    f1.write(str(k1)[1:-1] + '\n')

print('Исходный массив:')
for p in range(M):
    for k in range(N):
        print(a[p][k], end = ' ')
    print()
f1.close()

f1 = open('C:/Program Files/IvanchihinUB31vvod.txt', 'r')
f2 = open('C:/Program Files/IvanchihinUB31vivod.txt', 'w')

l1 = f1.read().rstrip().split('\n')
for q1 in l1:
    q1 = q1.split(', ')
    l2 = list() 
    for q2 in q1:
        q2 = int(q2)
        l2.append(q2)
        # меняем строку
        maximum = max(l2) 
        maI = l2.index(maximum)
        minimum = min(l2)
        miI = l2.index(minimum)
        l2[maI], l2[0] = l2[0], l2[maI]
        l2[miI], l2[-1] = l2[-1], l2[miI] 
    print(l2)
    f2.write(str(l2) + '\n')

f1.close()
f2.close()
