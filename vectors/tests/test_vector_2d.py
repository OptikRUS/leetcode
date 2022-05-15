import pytest

from vectors.vector_2d import Vector, Point


def get_point(x, y):
    return Point(x, y)


def get_vector(x, y):
    return Vector(x, y)


@pytest.mark.parametrize("x, y, result", [
    (1, 2, (1.0, 2.0)),
    (0, 0, (0.0, 0.0)),
    (-1, -2, (-1.0, -2.0)),
    (1.5, 0, (1.5, 0.0)),
    ('1', '0', (1, 0.0)),
    ('2.5', '0', (2.5, 0.0)),
    (get_point(1, 2), get_point(0, 0), (-1.0, -2.0)),
])
def test_get_vector(x, y, result):
    vector = get_vector(x, y)
    assert (vector.x, vector.y) == result


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
    (get_point(1, 2), None, TypeError),
])
def test_get_vector_exceptions(x, y, result):
    with pytest.raises(result):
        get_vector(x, y)


@pytest.mark.parametrize("x, y, result", [
    (1, 2, 'coord x: 1.0 coord y: 2.0'),
    (0, 0, 'coord x: 0.0 coord y: 0.0'),
    (-1, -2, 'coord x: -1.0 coord y: -2.0'),
    (1.5, 0, 'coord x: 1.5 coord y: 0.0'),
    ('1.5', 0, 'coord x: 1.5 coord y: 0.0'),
    (get_point(1, 2.5), get_point(2, 1.5), 'coord x: 1.0 coord y: -1.0'),
    (get_point(1, 2.5), (2.5, 3), 'coord x: 1.5 coord y: 0.5'),
    ((1, 2.5), get_point(2.5, 3), 'coord x: 1.5 coord y: 0.5'),
    ((1, 2), (2, 3), 'coord x: 1.0 coord y: 1.0'),
])
def test_get_vector_str(x, y, result):
    assert get_vector(x, y).__str__() == result


def test_get_vector_missing():
    with pytest.raises(TypeError):
        get_vector()


@pytest.mark.parametrize("x_1, y_1, x_2, y_2, result", [
    ((0, 0), (4, 3), (3, 4), (0, 0), -0.96),
    (get_point(0, 0), (4, 3), (3, 4), (0, 0), -0.96),
    ((0, 0), get_point(4, 3), (3, 4), (0, 0), -0.96),
    ((0, 0), (4, 3), get_point(3, 4), (0, 0), -0.96),
    ((0, 0), (4, 3), (3, 4), get_point(0, 0), -0.96),
    (get_point(0, 0), get_point(4, 3), (3, 4), (0, 0), -0.96),
    ((0, 0), (4, 3), get_point(3, 4), get_point(0, 0), -0.96),
    (get_point(0, 0), (4, 3), (3, 4), get_point(0, 0), -0.96),
    ((0, 0), get_point(4, 3), get_point(3, 4), (0, 0), -0.96),
])
def test_vector_corner(x_1, y_1, x_2, y_2, result):
    assert get_vector(x_1, y_1).corner(get_vector(x_2, y_2)) == result


@pytest.mark.parametrize("x_1, y_1, x_2, y_2, x_3, y_3, result", [
    ((0, 0), (1, 1), (2, 2), (0, 0), (1, 1,), (0, 0), (-2.0, -2.0)),
    (get_point(0, 0), (1, 1), (2, 2), (0, 0), (1, 1,), (0, 0), (-2.0, -2.0)),
    ((0, 0), get_point(1, 1), (2, 2), (0, 0), (1, 1,), (0, 0), (-2.0, -2.0)),
    ((0, 0), (1, 1), get_point(2, 2), (0, 0), (1, 1,), (0, 0), (-2.0, -2.0)),
    ((0, 0), (1, 1), (2, 2), get_point(0, 0), (1, 1,), (0, 0), (-2.0, -2.0)),
    ((0, 0), (1, 1), (2, 2), (0, 0), get_point(1, 1, ), (0, 0), (-2.0, -2.0)),
    ((0, 0), (1, 1), (2, 2), (0, 0), (1, 1,), get_point(0, 0), (-2.0, -2.0)),
    (get_point(0, 0), get_point(1, 1), get_point(2, 2), get_point(0, 0), get_point(1, 1, ), get_point(0, 0),
     (-2.0, -2.0)),
])
def test_vector_add(x_1, y_1, x_2, y_2, x_3, y_3, result):
    vector_1 = get_vector(x_1, y_1)
    vector_2 = get_vector(x_2, y_2)
    vector_3 = get_vector(x_3, y_3)
    vector = vector_1 + vector_2 + vector_3
    assert (vector.x, vector.y) == result


@pytest.mark.parametrize("x_1, y_1, x_2, y_2, x_3, y_3, result", [
    ((0, 0), (1, 1), (2, 2), (0, 0), (1, 1,), (0, 0), (4.0, 4.0)),
    (get_point(0, 0), (1, 1), (2, 2), (0, 0), (1, 1,), (0, 0), (4.0, 4.0)),
    ((0, 0), get_point(1, 1), (2, 2), (0, 0), (1, 1,), (0, 0), (4.0, 4.0)),
    ((0, 0), (1, 1), get_point(2, 2), (0, 0), (1, 1,), (0, 0), (4.0, 4.0)),
    ((0, 0), (1, 1), (2, 2), get_point(0, 0), (1, 1,), (0, 0), (4.0, 4.0)),
    ((0, 0), (1, 1), (2, 2), (0, 0), get_point(1, 1, ), (0, 0), (4.0, 4.0)),
    ((0, 0), (1, 1), (2, 2), (0, 0), (1, 1,), get_point(0, 0), (4.0, 4.0)),
    (get_point(0, 0), get_point(1, 1), get_point(2, 2), get_point(0, 0), get_point(1, 1, ), get_point(0, 0),
     (4.0, 4.0)),
])
def test_vector_sub(x_1, y_1, x_2, y_2, x_3, y_3, result):
    vector_1 = get_vector(x_1, y_1)
    vector_2 = get_vector(x_2, y_2)
    vector_3 = get_vector(x_3, y_3)
    vector = vector_1 - vector_2 - vector_3
    assert (vector.x, vector.y) == result


@pytest.mark.parametrize("x, y, n, res", [
    (1, 3, 3, (3.0, 9.0)),
    (1, 3, 0, (0.0, 0.0)),
])
def test_vector_mul(x, y, n, res):
    vector = get_vector(x, y)
    vector * n
    assert (vector.x, vector.y) == res


@pytest.mark.parametrize("x, y, res", [
    (3, 4, 5.0),
    (0, 5, 5.0),
    (5, 0, 5.0),
    (0, 0, 0.0),
])
def test_vector_abs(x, y, res):
    assert abs(Vector(x, y)) == res


@pytest.mark.parametrize("x_1, y_1, x_2, y_2, result", [
    (3, 4, 4, 3, 24.0),
    (0, 4, 4, 3, 12.0),
    (3, 0, 4, 3, 12.0),
    (3, 4, 0, 3, 12.0),
    (3, 4, 0, 0, 0.0),
    (0, 0, 4, 3, 0.0),
    (0, 0, 0, 0, 0.0),
])
def test_vector_scalar(x_1, y_1, x_2, y_2, result):
    assert get_vector(x_1, y_1).scalar_mul(get_vector(x_2, y_2)) == result
