import pytest

from vectors.vector_3d import Vector3D, Point3D


def get_point_3d(x, y, z):
    return Point3D(x, y, z)


def get_vector_3d(x, y, z):
    return Vector3D(x, y, z)


@pytest.mark.parametrize("x, y, z, result", [
    ((1, 2, 3), (4, 5, 6), (1, 2, 3), (3.0, 3.0, 3.0)),
    (get_point_3d(1, 2, 3), get_point_3d(4, 5, 6), get_point_3d(1, 2, 3), (3.0, 3.0, 3.0)),
    ('1', 2, 3, (1.0, 2.0, 3.0)),
    ('1.5', 2, 3, (1.5, 2.0, 3.0)),
])
def test_get_vector_3d(x, y, z, result):
    vector = get_vector_3d(x, y, z)
    assert (vector.x, vector.y, vector.z) == result


@pytest.mark.parametrize("x, y, z, res", [
    (1, '', 0, ValueError),
    ('', 0, 0, ValueError),
    ('один', -2, 0, ValueError),
    ([], 0, 0, TypeError),
    (1, (), 0, TypeError),
    (1, (1,), 0, TypeError),
    ([3], 1, 0, TypeError),
    ({4}, 1, 0, TypeError),
    (None, 1, 0, TypeError),
])
def test_get_vector_3d_exceptions(x, y, z, res):
    with pytest.raises(res):
        get_vector_3d(x, y, z)


@pytest.mark.parametrize("x, y, z, result", [
    (1, 2, 3, 'coord x: 1.0 coord y: 2.0 coord z: 3.0'),
    (get_point_3d(1, 2, 3), get_point_3d(4, 5, 6), get_point_3d(1, 2, 3), 'coord x: 3.0 coord y: 3.0 coord z: 3.0'),
])
def test_get_vector_str(x, y, z, result):
    assert get_vector_3d(x, y, z).__str__() == result


def test_get_vector_3d_missing():
    with pytest.raises(TypeError):
        get_vector_3d()


@pytest.mark.parametrize("x_1, y_1, z_1, x_2, y_2, z_2, result", [
    (1, 2, 3, 4, 5, 6, (-3.0, -6.0, -3.0)),
    (1, 2, 3, 1, 2, 3, (0.0, 0.0, 0.0)),
    (4, 5, 6, 1, 2, 3, (3.0, 6.0, 3.0)),
])
def test_vector_vector_mul(x_1, y_1, z_1, x_2, y_2, z_2, result):
    vector = get_vector_3d(x_1, y_1, z_1).vector_mul(get_vector_3d(x_2, y_2, z_2))
    assert (vector.x, vector.y, vector.z) == result
