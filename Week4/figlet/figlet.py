from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

if sys.argv[1] in ["--font", "-f"] and sys.argv[2] in figlet.getFonts():
    figlet.setFont(font=sys.argv[2])
elif len(sys.argv) == 1:
    random_font = random.choice(figlet.getFonts())
    figlet.setFont(font=random_font)
else:
    sys.exit("Invalid usage")

user_input = input("Input: ")
print(figlet.renderText(user_input))
