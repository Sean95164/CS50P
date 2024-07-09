from twttr import shorten

def test_twttr():
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("TwItter") == "Twttr"
    assert shorten("CS50") == "CS50"
