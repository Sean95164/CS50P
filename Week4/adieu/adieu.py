import inflect
p = inflect.engine()
name_list = []
try:
    while True:
        name = input("Input: ")
        name_list.append(name)
except EOFError:
    print("Adieu, adieu, to " + p.join(name_list))
