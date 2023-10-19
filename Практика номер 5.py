# номер 1
# a = input()
# a1 = a.split(' ')
# z = 0
# for i in a1:
#     for j in i:
#         if j[0] == 'е':
#             z+=1
# print(z)

# номер 2
# a = input()
# z=0
# while ':' in a:
#     if ':' in a:
#         a = a.replace(':', '%', 1)
#         z+=1
# print(a, z)

# номер 3
# a = input()
# z=0
# while '.' in a:
#     if '.' in a:
#         a = a.replace('.', '', 1)
#         z+=1
# print(a, z)

# номер 4
# a = input()
# z=0
# while 'а' in a:
#     if 'а' in a:
#         a = a.replace('а', 'о', 1)
#         z+=1
# p1 = a.count(' ')
# p2 = len(a)
# print(a, z, p2-p1)

# номер 5
# a = input()
# print(a.lower())

# номер 6
# a = input()
# z=0
# while '.' in a:
#     if '.' in a:
#         a = a.replace('а', '', 1)
#         z+=1
# print(a, z)

# номер 7
# s = input()
# n = len(s)
# s = s[:n // 2].replace('п', '*') + s[n // 2:]
# print(s)

# номер 8
# a = input()
# a = a[:-1]
# print(a)
# p = a.split(' ')
# print(p)
# print(len(p))

# номер 9
# a = input()
# b = input()
# print(a.count(b))

# номер 10
# s = input()
# print(s.title())

# номер 11
# a = input()

# номер 12
a = input()
z = 0
a = a.split()
for i in a:
    if i[-1] == 'я':
        z+=1
print(z)