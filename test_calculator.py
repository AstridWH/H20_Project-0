from calculator import add, Factorial, Sin, divide, Cos, Tan
import math as math
import pytest

tol = 1e-13

def test_add_Exercise_1(a=1, b=2):
    from_add = add(a, b)
    control = a + b
    assert from_add == control

def add_number_and_string_Exercise_5(a=1, b= 'hello'):
    with pytest.raises(TypeError):
        add(a,b)
    
def test_add_float_Exercise_2(a=0.1, b=0.2):
    assert abs((add(a,b)) - (a+b)) < tol

def test_add_string_Exercise_3(a = 'Hello', b = 'World'):
    from_add = add(a, b)
    control = a + b
    assert from_add == control 

@pytest.mark.parametrize("a, answer", [((1.0,2.0),3.0), ((3.0,4),7), ((10,7),17), ("Hello", "World"), "Hello World"])
def test_add_paramertize_int_float_str_Exercise_6(a,answer):
    from_add = add(a[0], a[1])
    assert from_add == answer

def test_factorial_Exercise_4(k = 10):
    from_Factorial = Factorial(k)
    control = math.factorial(k)
    assert abs(from_Factorial-control) < tol

@pytest.mark.parametrize("a, answer", [(2,2), (3, 6), (10, 3628800)])
def test_factorial_parametrize_Exercise_6(a, answer):
    assert Factorial(a) == answer

def test_sin_Exercise_4(x=math.pi/2, N=85):
    control = math.sin(x)
    from_Sin = Sin(x, N)
    assert abs(control-from_Sin) < tol

@pytest.mark.parametrize("a, answer", [((0, 85), 0), ((math.pi/6, 85), 1/2), ((math.pi/2, 85), 1), ((3*math.pi/2, 85), -1)])
def test_sin_parametrize_Exercise_6(a, answer):
    from_Sin = Sin(a[0], a[1])
    assert abs(from_Sin-answer) < tol
    
def test_divide_Exercise_4(x=34926, y=5821):
    control = x/y
    from_divide = divide(x, y)
    assert control == from_divide

def test_divide_by_zero_Exercise_5(x = 1, y = 0):
    with pytest.raises(ZeroDivisionError):
        divide(x,y)

@pytest.mark.parametrize("a,answer", [((4, 2), 2), ((14, 7), 2), ((81, 3), 27)])
def test_divide_parametrize_Exercise_6(a, answer):
    from_divide = divide(a[0], a[1])
    assert from_divide == answer

def test_cos_Exercise_4(x=math.pi/4, N=85):
    control = math.cos(x)
    from_Cos = Cos(x, N)
    assert abs(control - from_Cos) < tol

@pytest.mark.parametrize("a, answer", [((0, 85), 1), ((math.pi/3, 85), 1/2), ((math.pi/2, 85), 0), ((math.pi, 85), -1)])
def test_cos_parametrize_Exercise_6(a,answer):
    from_Cos = Cos(a[0], a[1])
    assert abs(from_Cos-answer) < tol


def test_tan_Exercise_4(x=math.pi/4, N=85):
    control = math.tan(x)
    from_Tan = Tan(x, N)
    assert abs(control - from_Tan) < tol

@pytest.mark.paramertize("a,answer", [((0, 85), 0), ((math.pi/4, 85), 1), ((math.pi, 85), 0)])
def test_tan_parametrize_Exercise_6(a,answer):
    from_Tan = Tan(a[0], a[1])
    assert abs(from_Tan - answer) < tol 
    