from source.math_operation import add, sub

def test_add_two_numbers():
    assert add(5, 3) == 8
    assert add(-1, -3) == -4

def test_sub_two_numbers():
    assert sub(5, 3) == 2
    assert sub(-1, -3) == -2
    assert sub(5, 1) == 4