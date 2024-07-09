def main():
    time = input("What time is it? ")
    hours = convert(time)
    if(7 <= hours <= 8):
        print("breakfast time")
    elif(12 <= hours <= 13):
        print("lunch time")
    elif(18 <= hours <= 19):
        print("dinner time")

def convert(time):
    hour, minute = time.split(":")
    hours = float(hour) + float(minute) / 60.0
    return hours


if __name__ == "__main__":
    main()