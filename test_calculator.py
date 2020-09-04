from calculator import add

def test_add(a=1, b=2):
    n = add(a, b)
    m = a + b
    return n == m 
    
def test_add_float(a=0.1, b=0.2):
    #print(add(a,b))
    #print(a+b)
    return abs((add(a,b)) - (a+b)) < 1e-5

    
print(test_add())
print(test_add(0.1, 0.2))   #Samme resultat som add_float
print(test_add_float())

