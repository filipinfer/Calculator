from Calc import add
from Calc import sub
from Calc import div



def test_add():
    assert add(2, 3) == 5
    assert add(1, 4) == 5

def test_sub():
    assert sub(4, 3) == 1
    assert sub(6, 1) == 7

def test_div():
    assert div(4,2) == 2
    assert div(10,2) ==5
