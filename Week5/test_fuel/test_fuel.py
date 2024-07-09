from fuel import convert, gauge
import pytest

def test_1():
    assert gauge(convert("3/4")) == "75%"


def test_2():
    assert gauge(convert("1/4")) == "25%"


def test_3():
    assert gauge(convert("4/4")) == "F"


def test_4():
    assert gauge(convert("0/4")) == "E"

def test_5():
    with pytest.raises(ValueError):
        gauge(convert("5/4"))

def test_6():
    with pytest.raises(ZeroDivisionError):
        gauge(convert("3/0"))

def test_7():
    assert gauge(convert("1/100")) == "E"

def test_8():
    assert gauge(convert("99/100")) == "F"
