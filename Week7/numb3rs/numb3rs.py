import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    cond_1 = re.search(r"^(((\d{1,2})|(1\d{2})|(2[0-4]\d)|(25[0-5]))\.){3}((\d{1,2})|(1\d{2})|(2[0-4]\d)|(25[0-5]))$", ip)
    if cond_1:
        return True
    else:
        return False




if __name__ == "__main__":
    main()
    # ip = input("IPv4 Address: ")
    # matches = re.search(r"^[1-9][1-9][1-9]\.$", ip)
    # if matches:
    #     print("ok")
    # else:
    #     print("no")
