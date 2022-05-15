import pytest

from vectors.point import Point3D


def get_point_3d(x, y, z):
    return Point3D(x, y, z)


@pytest.mark.parametrize("x, y, z, result", [
    (1, 2, 3, (1.0, 2.0, 3.0)),
    (0, 0, 0, (0.0, 0.0, 0.0)),
    (-1, -2, -3, (-1.0, -2.0, -3.0)),
    (1.5, 0, -1, (1.5, 0.0, -1.0)),
    ('1', '0', 0, (1, 0.0, 0.0)),
    ('3.5', '0', 0, (3.5, 0.0, 0.0)),
])
def test_get_point_3d(x, y, z, result):
    point = get_point_3d(x, y, z)
    assert (point.x, point.y, point.z) == result


@pytest.mark.parametrize("x, y, z, result", [
    (1, 2, 3, 'coord x: 1.0 coord y: 2.0 coord z: 3.0'),
    (0, 0, 0, 'coord x: 0.0 coord y: 0.0 coord z: 0.0'),
    ('1.5', '1', 0, 'coord x: 1.5 coord y: 1.0 coord z: 0.0'),
])
def test_get_point_str_3d(x, y, z, result):
    point = get_point_3d(x, y, z)
    assert point.__str__() == result


@pytest.mark.parametrize("x, y, z, result", [
    (1, '', 0, ValueError),
    ('', 0, 0, ValueError),
    ('один', -2, 0, ValueError),
    ([], 0, 0,  TypeError),
    (1, (), 0,  TypeError),
    (1, (1, ), 0, TypeError),
    ([3], 1, 0,  TypeError),
    ({4}, 1, 0,  TypeError),
    (None, 1, 0, TypeError),
])
def test_get_point_exceptions_3d(x, y, z, result):
    with pytest.raises(result):
        get_point_3d(x, y, z)


def test_get_point_missing_3d():
    with pytest.raises(TypeError):
        get_point_3d()
