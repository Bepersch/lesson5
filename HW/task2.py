def unique_symbols(_list):
    count = 1
    _list = sorted(_list)
    for j in range(len(_list) - 1):
        if _list[j] != _list[j+1]:
            count += 1
    return count


try:
    n = int(input("Введите размер массива: "))
    if n <= 0:
        raise ValueError
    a = []
    for i in range(n):
        a.append(int(input("Введите элемент %d: " % i)))
except ValueError:
    print("Вы ввели не целое число или задади отрицательный размер")
else:
    print("Уникальных символов: %d" % unique_symbols(a))
