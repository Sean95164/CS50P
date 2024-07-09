def main():
    string = input("Input: ")
    print("Output: ", end="")
    print(shorten(string))
    print()


def shorten(word):
    new_word = ""
    for c in word:
        if c.lower() in ["a", "e", "i", "o", "u"]:
            continue
        new_word += c
    return new_word


if __name__ == "__main__":
    main()
