while True:
    try:
        x, y = map(int, input("Fraction: ").split("/"))
        if x % 1 != 0 or y % 1 != 0:
            continue
        elif x > y:
            continue
        else:
            break

    except (ValueError, ZeroDivisionError):
        pass

percentages = round(x / y * 100)
if percentages >= 99:
    print("F")

elif percentages <= 1:
    print("E")

else:
    print(f"{percentages}%")
