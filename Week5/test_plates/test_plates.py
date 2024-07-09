from plates import is_valid

def test_oneword():
    assert is_valid("H") == False

def test_alpha_error():
    assert is_valid("OUTATIME") == False

def test_alpha_error1():
    assert is_valid("NRVOUS") == True

def test_alpha_error2():
    assert is_valid("CS50P2") == False

def test_alpha_error3():
    assert is_valid("CS50P") == False

def test_startwith_zero():
    assert is_valid("CS05") == False

def test_startwith_numeric():
    assert is_valid("1122") == False

def test_having_dot():
    assert is_valid("PI3.14") == False

def test_right_plates():
    assert is_valid("CS50") == True
    assert is_valid("ECTO88") == True
