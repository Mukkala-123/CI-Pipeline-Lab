from app import add, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_multiply():
    assert multiply(2, 4) == 8

def test_divide():
    assert divide(10, 2) == 5
