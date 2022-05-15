import pytest

from vectors.point import Point


def get_point(x, y):
    return Point(x, y)


@pytest.mark.parametrize("x, y, result", [
    (1, 2, (1.0, 2.0)),
    (0, 0, (0.0, 0.0)),
    (-1, -2, (-1.0, -2.0)),
    (1.5, 0, (1.5, 0.0)),
    ('1', '0', (1, 0.0)),
    ('2.5', '0', (2.5, 0.0)),
])
def test_get_point(x, y, result):
    point = get_point(x, y)
    assert (point.x, point.y) == result


@pytest.mark.parametrize("x, y, result", [
    (1, 2, 'coord x: 1.0 coord y: 2.0'),
    (0, 0, 'coord x: 0.0 coord y: 0.0'),
    (-1, -2, 'coord x: -1.0 coord y: -2.0'),
    (1.5, 0, 'coord x: 1.5 coord y: 0.0'),
    ('1.5', 0, 'coord x: 1.5 coord y: 0.0'),
])
def test_get_point_str(x, y, result):
    point = get_point(x, y)
    assert point.__str__() == result


@pytest.mark.parametrize("x, y, result", [
    (1, '', ValueError),
    ('', 0, ValueError),
    ('один', -2, ValueError),
    ([], 0, TypeError),
    (1, (), TypeError),
    (1, (1,), TypeError),
    ([3], 1, TypeError),
    ({4}, 1, TypeError),
    (None, 1, TypeError),
])
def test_get_point_exceptions(x, y, result):
    with pytest.raises(result):
        get_point(x, y)


def test_get_point_missing():
    with pytest.raises(TypeError):
        get_point()
