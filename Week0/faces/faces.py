def main():
    symbol = input("Input: ")
    print(convert(symbol))

def convert(symbol):
    symbol = symbol.replace(":)","🙂").replace(":(","🙁")
    return symbol

main()