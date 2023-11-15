# 1.1
# def fac(x):
#     if x == 0:
#         return 1
#     return fac(x-1)*x
# x = int(input())
# n = int(input())
# print((x**n)/fac(n))

2.2
b = []
z = 0
def vvod():
    a = int(input())
    b.append(a)
    if a == 0:
        maximum(b)
    else:
        print(b)
        vvod()

    
def maximum(x):
    x.remove(max(x))
    print(max(x))

vvod()