import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches_1 = re.search(r"([0-9]|1[0-2])(:[0-5]\d)? AM to ([0-9]|1[0-2])(:[0-5]\d)? PM", s)
    matches_2 = re.search(r"([0-9]|1[0-2])(:[0-5]\d)? PM to ([0-9]|1[0-2])(:[0-5]\d)? AM", s)
    if matches_1:
        hour1, minute1, hour2, minute2  = matches_1.groups()
        if minute1 == None:
            minute1 = 0
        else:
            minute1 = minute1[1:]
        if minute2 == None:
            minute2 = 0
        else:
            minute2 = minute2[1:]
        if 1<=int(hour1)<=11:
            return f"{int(hour1):02}:{int(minute1):02} to {int(hour2)+12:02}:{int(minute2):02} "
        elif int(hour1) == 12:
            if int(hour2) != 12:
                return f"00:{int(minute1):02} to {int(hour2)+12:02}:{int(minute2):02}"
            else:
                return f"00:{int(minute1):02} to 12:{int(minute2):02}"
    elif matches_2:
        hour1, minute1, hour2, minute2  = matches_2.groups()
        if minute1 == None:
            minute1 = 0
        else:
            minute1 = minute1[1:]
        if minute2 == None:
            minute2 = 0
        else:
            minute2 = minute2[1:]
        if 1<=int(hour2)<=11:
            return f"{int(hour1)+12:02}:{int(minute1):02} to {int(hour2):02}:{int(minute2):02}"
        elif int(hour2) == 12:
            if int(hour1) != 12:
                return f"{int(hour1)+12:02}:{int(minute1):02} to 00:{int(minute2):02}"
            else:
                return f"12:{int(minute1):02} to 00:{int(minute2):02}"
    else:
        raise ValueError



if __name__ == "__main__":
    main()
