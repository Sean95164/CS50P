import random as rd


def main():
    level = get_level()
    left_times = 3
    correct = 0
    for _ in range(10):
        x, y, ans = generate_integer(level)
        while left_times != 0:
            print(f"{x} + {y} = ",end = "")
            try:
                user_input = int(input())
                if(user_input == ans):
                    correct += 1
                    left_times = 3
                    break
                else:
                    print("EEE")
                    left_times -= 1
            except ValueError:
                print("EEE")
                left_times -= 1

        if left_times == 0:
            print(f"{x} + {y} = {ans}")
            left_times = 3

    print(f"Score: {correct}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if(level in [1,2,3]):
                break
        except ValueError:
            continue
    return level

def generate_integer(level):
    match level:
        case 1:
            x = rd.randint(0,9)
            y = rd.randint(0,9)
            ans = x + y
            return x, y, ans
        case 2:
            x = rd.randint(10,99)
            y = rd.randint(10,99)
            ans = x + y
            return x, y, ans
        case 3:
            x = rd.randint(100,999)
            y = rd.randint(100,999)
            ans = x + y
            return x, y, ans
        case __:
            raise ValueError

if __name__ == "__main__":
    main()
