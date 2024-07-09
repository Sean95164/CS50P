import sys
 # hello
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
else:
    c = 0
    try:
        if(sys.argv[1][-3:] != ".py"):
            sys.exit("Not a Python file")

        with open(sys.argv[1],"r") as file:
            for line in file:
                if(line.lstrip(" ").startswith("\n") or line.lstrip(" ").startswith("#")):
                    continue
                c+=1

        print(c)
    except FileNotFoundError:
        sys.exit("File does not exist")


