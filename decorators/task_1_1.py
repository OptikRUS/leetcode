"""
1.1 Написать декоратор, который перед запуском произвольной функции с произвольным набором аргументов будет показывать
в консоли сообщение "Покупайте наших котиков!" и возвращать результат запущенной функции.
1.2 Параметризовать декоратор таким образом, чтобы сообщение, печатаемое перед выполнением функции можно было задавать
как параметр во время декорирования.
"""


def buy_cats(func):
    def wrapper(*args, **kwargs):
        print("Покупайте наших котиков!")
        return func(*args, **kwargs)
    return wrapper


@buy_cats
def division(a, b):
    return a / b


div = division(1, 2)
print(div)
