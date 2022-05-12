import pytest

from tasks.tumbochka_iterator import Iterator, Tumba


def create_add(element):
    tumbochka = Tumba()
    tumbochka.add_item(element)
    return tumbochka


test_data = [
    (1, 1),
    ('item', 'item'),
    ([1, 2, 3], [1, 2, 3]),
    ({3, 4, 5}, {3, 4, 5})
]


@pytest.mark.parametrize("element, result", test_data)
def test_add_item(element, result):
    assert create_add(element).items[0] == result


@pytest.mark.parametrize("element, result", test_data)
def test_iter(element, result):
    for i in create_add(element):
        assert i == result


@pytest.mark.parametrize("n, result", [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5),
])
def test_to_custom(n, result):
    tumbochka = Tumba()
    for i in range(1, 6):
        tumbochka.add_item(i)
    iterator = Iterator(tumbochka.items)
    iterator.to_custom(n)
    assert next(iterator) == result


@pytest.mark.parametrize("elements, n, exception", [
    (1, 1, IndexError),
    ('item', 1, IndexError),
    ([1, 2, 3], 2, IndexError),
    (None, 3, IndexError)
])
def test_to_custom_exception(elements, n, exception):
    with pytest.raises(exception):
        Iterator(create_add(elements).items).to_custom(n)


@pytest.mark.parametrize("element, result", [
    (1, 0),
    ('item', 0),
    ([1, 2, 3], 0),
    (None, 0)
])
def test_to_start(element, result):
    iterator = Iterator(create_add(element).items)
    iterator.to_start()
    assert iterator.count == result


def test_stop_iteration():
    res = Iterator(create_add(1).items)
    with pytest.raises(StopIteration):
        next(res)
        next(res)


def test_add_item_exception():
    with pytest.raises(TypeError):
        tumbochka = Tumba()
        tumbochka.add_item()
