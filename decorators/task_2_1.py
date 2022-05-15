"""
2.1 Написать декоратор, который внутри себя выполнял бы функцию и возвращал бы результат её работы в случае успешного
выполнения. В случае возникновения ошибки во время выполнения функции нужно сделать так, чтобы выполнение функции было
повторено ещё раз с теми же самыми аргументами, но не более 10 раз.
Если после последней попытки функцию так и не удастся выполнить успешно, то бросать исключение.
2.2 Параметризовать декоратор таким образом, чтобы количество попыток выполнения функции можно было задавать как
параметр во время декорирования.
"""


def test_func_custom(attempts):
    def test_func(func):
        def wrapper(*args, **kwargs):
            count = attempts
            while count != 0:
                try:
                    return func(*args, **kwargs)
                except Exception as error:
                    print(f"Error {error} attemts left {count}")
                    count -= 1
        return wrapper
    return test_func


@test_func_custom(5)
def division(a, b):
    return a / b


print(division(1, 0))
