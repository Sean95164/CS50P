from jar import Jar
import pytest

def test_init():
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

    with pytest.raises(ValueError):
        jar = Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(2)
    jar.deposit(2)
    assert jar.size == 2

    with pytest.raises(ValueError):
        jar.deposit(1)


def test_withdraw():
    jar = Jar(2)
    assert jar.size == 0
    jar.deposit(1)
    assert jar.size == 1
    jar.withdraw(1)
    assert jar.size == 0

    with pytest.raises(ValueError):
        jar.withdraw(1)
