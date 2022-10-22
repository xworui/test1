print('Введите n')

n = int(input())


if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    F1 = 0
    F2 = 1
    i = 1
    Fn = 0
    while n > i:
        Fn = F1 + F2
        F1, F2 = F2, Fn
        i += 1
    print(Fn)