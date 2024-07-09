from numb3rs import validate

def test_1():
    assert validate("255.255.255.255") == True
def test_2():
    assert validate("512.512.512.512") == False
def test_3():
    assert validate("1.2.3.1000") == False
def test_4():
    assert validate("cat") == False
def test_5():
    assert validate("75.999.76.65") == False
