from seasons import get_minutes_words
from datetime import date

def test_transform_to_word():
    recorded_day = date(2000, 1, 1)
    assert get_minutes_words(recorded_day - date(1999, 1, 1)) == "Five hundred twenty-five thousand, six hundred minutes"
    assert get_minutes_words(recorded_day - date(1999, 12, 31)) == "One thousand, four hundred forty minutes"
    assert get_minutes_words(recorded_day - date(1970, 1, 1)) == "Fifteen million, seven hundred seventy-eight thousand eighty minutes"
