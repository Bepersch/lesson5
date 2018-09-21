from random import randint


def randgame(n, k):
    ans = randint(1, n)
    for i in range(k):
        print("Осталось попыток: %d" % (k - i))
        try:
            a = int(input("Ваше число: "))
        except TypeError:
            print("Вы ввели не целое число")
        if i == k - 1 and a != ans:
            return "Вы не угадали\nПопытки закончились\nЗагаданное число: %d" % ans
        elif a < ans:
            print("Ваше число меньше загаданного")
        elif a > ans:
            print("Ваше число больше загаданного")
        elif a == ans:
            return "Вы угадали"


try:
    n = int(input("Диапазон: "))
    k = int(input("Кол-во попыток: "))
    if k <= 0 or n <= 0:
        raise ValueError
except ValueError:
    print("Вы ввели не целое или одно из чисел <0")
else:
    print(randgame(n, k))
