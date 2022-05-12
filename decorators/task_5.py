"""
После решения задач написать функцию и задекорировать её сразу несколькими из созданных декораторов и посмотреть на
результат и суметь объяснить его. Потом поменять порядок декорирования и проделать то же самое.
"""
import time


def get_slogan(slogan):
    def buy_cats(func):
        def wrapper(*args, **kwargs):
            time.sleep(2)
            print(slogan)
            return func(*args, **kwargs)
        return wrapper
    return buy_cats


def test_func_custom(attempts):
    def test_func(func):
        def wrapper(*args, **kwargs):
            count = attempts
            while count != 0:
                try:
                    return func(*args, **kwargs)
                except Exception as error:
                    print(f"Error {error} func '{func.__name__}' attemts left {count}")
                    count -= 1
        return wrapper
    return test_func


def seconder(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        finish = time.perf_counter()
        print(f'function "{func.__name__}" performed {finish - start}')
    return wrapper


@get_slogan('Сейчас функция может быть сработает')
@test_func_custom(5)
@seconder
def division(a, b):
    time.sleep(2)
    return a / b


div = division(1, 1)
print(div)


"""
seconder, get_slogan, test_func_custom: 
seconder - замеряет время от выполнения get_slogan до последнего выполнения test_func_custom.

get_slogan, seconder, test_func_custom: 
сначала выполняется get_slogan, затем замеряется время всех выполнений test_func_custom.

seconder, test_func_custom, get_slogan: 
get_slogan выполняется перед каждым выполнением test_func_custom, а seconder замеряет их общее время.

test_func_custom, get_slogan, seconder:
Отловит ошибки get_slogan, если они будут. Если ошибок не будет, то отловит их у division и сработает slogan каждый раз.
seconder замеряет время выолнения division, только если у той нет ошибок.

Вывод:
Декораторы оборачивают друг друга с обычной функцией как в "матрёшке" или "капусте" снизу вверх.
"""
