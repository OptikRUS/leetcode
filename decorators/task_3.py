"""
3.1 Написать кэширующий декоратор. Суть в том, что если декорируемая функция будет запущена с теми параметрами с
которыми она уже запускалась - брать результат из кэша и не производить повторное выполнение функции.
3.2 Сделать так, чтобы информация в кэше была актуальной не более 10 секунд. Предусмотреть механизм автоматической
очистки кэша в процессе выполнения функций.
3.3 Параметризовать время кэширования в декораторе.
"""
import time


def cashe(func):
    cash_dict = {}

    def wrapper(*args, **kwargs):
        return cash_dict.setdefault(args, func(*args, **kwargs))

    return wrapper


@cashe
def division(a, b):
    return a / b


print(division(1, 2))
print(division(1, 4))
print(division(1, 2))
print(division(1, 4))
print(division(1, 3))

# start = time.perf_counter()
# print(start)
# time.sleep(2)
# finish = time.perf_counter()
# print(finish)
# print(finish - start)
