from datetime import date
import re, sys
import inflect

# get the user input, return the user born year, month, and day
def get_born_year():
    birth = input("Date of Birth: ")
    if (re.search(r"\d\d\d\d-\d\d-\d\d", birth)):
        return map(int, birth.split("-"))
    else:
        sys.exit("This is invalid input!")

# get the words of minutes
def get_minutes_words(timedelta):
    p = inflect.engine()
    minutes = round(timedelta.total_seconds() / 60.0)
    words = p.number_to_words(minutes, andword="") + " minutes"
    return words.capitalize()


def main():
    year, month, day = get_born_year()
    timedelta = date.today() - date(year, month, day)
    print(get_minutes_words(timedelta))




if __name__ == "__main__":
    main()
