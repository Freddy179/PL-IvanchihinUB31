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
# a = []
# print(a.max(), a.min())

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
# for i in range(len(a)):
#     if a[i] > 20:
#         a[i] = 1
#     elif a[i] < 10:
#         a[i] = 0
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
# for i in range(len(a)):
#     if a[i] < 15:
#         a[i] = a[i] * 2
# print(a)

# Вариант 4
# 1
# a = [1, 2, 4, 6, 7, 8, 10, 5, 3]
# b = max(a)
# print(b, a.index(b)+1)

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