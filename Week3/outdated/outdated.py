months = [
    "",
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    while True:
        user_input = input("Dates: ")
        try:
            year, month, day = format_1(user_input)
            if month > 12 or day > 31:
                continue
        except ValueError:
            try:
                year, month, day = format_2(user_input)
                if month > 12 or day > 31:
                    continue
            except ValueError:
                continue
        break
    print(f"{year:04d}-{month:02d}-{day:02d}")


def format_1(string):
    month, day, year = map(int, string.split("/"))
    return year, month, day


def format_2(string):
    month_and_day, year = string.split(", ")
    month, day = month_and_day.split(" ")
    month = months.index(month)
    return int(year), int(month), int(day)


main()
