from calculator import add

def test_add(a=1, b=2):
    n = add(a, b)
    m = a + b
    assert n == m 
    