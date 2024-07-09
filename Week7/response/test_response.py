from response import is_valid

def test_1():
    assert is_valid("malan@harvard.edu") == "Valid"
def test_2():
    assert is_valid("malan@@@harvard.edu") == "Invalid"
def test_3():
    assert is_valid("swsc940106@gmail..com") == "Invalid"
