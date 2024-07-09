items = {}

while True:
    try:
        item = input("").upper()
        if item not in items:
            items[item] = 1
        else:
            items[item] += 1

    except EOFError:
        break

in_order_list = list(sorted(items))
for item in in_order_list:
    print(f"{items[item]} {item}")
