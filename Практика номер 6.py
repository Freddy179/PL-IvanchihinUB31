# Вариант 7
# 1
# a = [2, 5, 1, 6, 7, 9]
# z1 = 0
# z2 = 1
# for i in a:
#     if int(a.index(i)) % 2 == 0:
#         z1 += i
#     else:
#         z2 *= i
# print(z1, z2)

# 2
# a = [1, 6, 1, 2, 4, 17, 29, 0]
# print(max(a), min(a))

# Вариант 10
# 1
# a = [5, 1, 2, 4, 5, 6]
# for i in a:
#     b = a.count(i)
#     if b > 1:
#         print(i)
#         break
#     else:
#         print('ничего не найдено')

# 2
# a = [19, 21, 8, 9, 25, 28, 5, 15, 24, 4, 31, 4, 56, 6, 18, 17]
# b = a
# for i in a:
#     if i > 20:
#         i = 1
#     elif i < 10:
#         i = 0
#     else:
#         pass
# print(a, b)

# Вариант 13
# 1
# a = [5, 1, 2, 4, 5, 6, 2, 7, 6]
# c = []
# z = []
# for i in a:
#     b = a.count(i)
#     if b > 1:
#         if str(i) not in c:
#             z.append(i)
#             z.append(a.index(i))
#             c += str(i)
# print(z)

# 2
# a = [19, 21, 8, 9, 25, 28, 5, 15]
# for i in a:
#     if i < 15:
#         i = i * 2
# print(a)

# Вариант 4
# 1
# a = [1, 2, 4, 6, 7, 8, 10, 5, 3]
# print(max(a), a.index(max(a))+1)

# 2
a = [15, 7, 8, 4, 2, 3, 9]
b = []
for i in a:
    if i % 2 != 0:
        b.append(i)
if len(b) == 0:
    print('ничего не найдено')
b.sort(reverse=True)
print(b)
