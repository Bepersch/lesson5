def string_format(_str):
    count = ""
    _str = _str.title()
    _str = _str.split()
    for i in _str:
        count += i + " "
    return count[:-1]


n = str(input("Введите сроку:\n"))
print(string_format(n))
