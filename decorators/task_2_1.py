"""
2.1 Написать декоратор, который внутри себя выполнял бы функцию и возвращал бы результат её работы в случае успешного
выполнения. В случае возникновения ошибки во время выполнения функции нужно сделать так, чтобы выполнение функции было
повторено ещё раз с теми же самыми аргументами, но не более 10 раз.
Если после последней попытки функцию так и не удастся выполнить успешно, то бросать исключение.
2.2 Параметризовать декоратор таким образом, чтобы количество попыток выполнения функции можно было задавать как
параметр во время декорирования.
"""


def test_func(func):
    def wrapper(*args, **kwargs):
        attempts = 10
        while attempts != 0:
            try:
                return func(*args, **kwargs)
            except Exception as error:
                print(f"Error {error}")
                attempts -= 1
    return wrapper


@test_func
def division(a, b):
    return a / b


div = division(1, 0)
print(division(1, 0))
