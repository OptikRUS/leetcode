"""
4.1 Написать декоратор, который бы измерял время работы функции и печатал бы его на экран.
4.2 Доработать декоратор таким образом, чтобы в логах было название запускаемой функции помимо времени исполнения.
4.3 Доработать декоратор так, чтобы запись лога для функции велась в файл, путь к которому нужно было бы задавать во
время декорирования, как параметр.
"""
import time
from time import perf_counter


def seconder_logs(filename):
    def seconder(func):
        def wrapper(*args, **kwargs):
            start = perf_counter()
            func(*args, **kwargs)
            time.sleep(2)
            finish = perf_counter()
            with open(filename, 'a') as f:
                f.write(f'function "{func.__name__}" performed {finish - start}\n')
        return wrapper

    return seconder


@seconder_logs('test.txt')
def division(a, b):
    return a / b


division(1, 2)
