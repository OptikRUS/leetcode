"""
Написать генератор, который будет принимать на вход строку и возвращать по запросу последовательно числовое
представление из таблицы ASCII очередного символа этой строки.
"""


def ascii_convert(string: str):
    for i in string:
        yield ord(i)


a = ascii_convert('какая-то строка')
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))



