def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    alpha = 0
    num = 0
    for c in s:
        if(c.isalpha()):
            alpha += 1
        elif(c.isdecimal()):
            num += 1
        elif(c in ["," , " " , "."]):
            return False

    if(alpha>=2 and len(s)<=6 and s[:alpha].isalpha()):
        if(s[alpha:alpha+1] != "0"):
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()
