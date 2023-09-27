# # номер 7
# n = int(input())
# z1 = 1
# z2 = 0
# for i in range(1, n+1):
#     z1*=i
#     z2+=z1
# print(z2)

# # номер 6
# N = int(input())
# z = 1
# for i in range(1, N+1):
#     z *= i
# print(z)

# # # номер 5
# N = int(input())
# z = 0
# for i in range(1, N+1):
#     z+=i**3
# print(z)

# номер 1
# A = int(input())
# B = int(input())
# z = []
# for i in range(A,B):
#     z.append(i)
# print(z)

# номер 2
# A = int(input())
# B = int(input())
# z = []
# if A<B:
#     for i in range(A,B):
#         z.append(i)
# else:
#     for i in range(A,B):
#         z.append(i)
#         z.reverse()
# print(z)

# номер 3
# A = int(input())
# B = int(input())
# z = []
# for i in range(A,B):
#     if i%2!=0:
#         z.append(i)
# print(z)

# номер 4
# N = int(input())
# z = 0
# while N!=0:
#     n = int(input())
#     z+=n
#     N-=1
# print(z)

# номер 8
n = int(input())
if n<=9:
    for i in range(1, n+1):
        for a in range(1, i+1):
            print(a, step='', end='')
else:
    print('Try again')

# номер 9
# N = int(input())
# z = 0
# a = 0
# b = 1
# c = 0
# while N != 0:
    # if a == b:
    #     a +=b
#     elif a<b:
#         c=a+b
#         a = c
#     elif b<a:
#         c=a+b
#         b = c
#     z+=c
#     N-=1
# print(z)

# номер 10
# N = int(input())
# K = int(input())
# summ = 0
# number1 = 1
# number2 = 0
# number3 = 0
# fl = 0
# while fl != K or N != 0:
#     if fl!=K:
#         if number1 == number2:
#             number1 += number2
#         if number1 < number2:
#             number3 = number1 + number2
#             number1 = number3
#         elif number2 < number1:
#             number3 = number1 + number2
#             number2 = number3
#         fl+=1
#     else:
#         if number1 < number2:
#             number3 = number1 + number2
#             number1 = number3
#         elif number2 < number1:
#             number3 = number1 + number2
#             number2 = number3
#         summ += number3
#         N-=1
# print(summ)