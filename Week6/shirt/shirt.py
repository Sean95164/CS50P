from PIL import Image,ImageOps
import sys,os

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

else:
    file1_extension = os.path.splitext(sys.argv[1])[1].lower()
    file2_extension = os.path.splitext(sys.argv[2])[1].lower()
    if(file1_extension not in [".jpg",".jpeg","png"]):
        sys.exit("Invalid input")
    if(file1_extension != file2_extension):
        sys.exit("Input and output have different extensions")
    try:
        photo = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")

        size = shirt.size
        rephoto = ImageOps.fit(photo,size)

        rephoto.paste(shirt,shirt)
        rephoto.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Invalid input")
