"""
3.1 Написать кэширующий декоратор. Суть в том, что если декорируемая функция будет запущена с теми параметрами с
которыми она уже запускалась - брать результат из кэша и не производить повторное выполнение функции.
3.2 Сделать так, чтобы информация в кэше была актуальной не более 10 секунд. Предусмотреть механизм автоматической
очистки кэша в процессе выполнения функций.
3.3 Параметризовать время кэширования в декораторе.
"""
import time


def cashe_with_timer(sec):
    def cashe(func):
        cash_dict = {}

        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = cash_dict.setdefault(args, func(*args, **kwargs))
            finish = time.perf_counter()
            cash_dict['time'] = finish - start
            if cash_dict['time'] > sec:
                var = cash_dict['time']
                cash_dict.clear()
                cash_dict['time'] = var
            return result

        return wrapper
    return cashe


@cashe_with_timer(10)
def division(a, b):
    return a / b


print(division(1, 2))
print(division(1, 4))
print(division(1, 2))
print(division(1, 4))
print(division(1, 3))
