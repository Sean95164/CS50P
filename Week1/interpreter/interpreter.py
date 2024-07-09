def main():
    expression = input("Expression: ")
    x, y, z = expression.split(" ")
    x = float(x)
    z = float(z)
    print(transform(x,y,z))

def transform(x, y, z):
    match y:
        case "+":
            return round(x+z,1)
        case "-":
            return round(x-z,1)
        case "*":
            return round(x*z,1)
        case "/":
            return round(x/z,1)

main()