import pytest

from tasks.ascii_transfer import ascii_convert


def test_ascii_convert():
    string = 'test_text'
    res = ascii_convert(string)
    for i in string:
        assert next(res) == ord(i)


def test_ascii_convert_stop_iteration():
    res = ascii_convert("t")
    with pytest.raises(StopIteration):
        next(res)
        next(res)


@pytest.mark.parametrize("argument, exception", [
    (1, TypeError),
    (None, TypeError),
    ('', StopIteration)
])
def test_ascii_convert_arguments(argument, exception):
    with pytest.raises(exception):
        next(ascii_convert(argument))
