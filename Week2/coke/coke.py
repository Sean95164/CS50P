due = 50
while True:
    if(due<=0):
        print("Change Owed:", -due)
        break

    print("Amount Due:",due)
    coin_input = int(input("Insert coin: "))
    if(coin_input not in [25,10,5]):
        continue
    due -= coin_input
