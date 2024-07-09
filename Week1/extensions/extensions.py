file_name = input("File name: ").lower().strip()
if file_name.endswith((".gif",".jpg",".jpeg",".png",".pdf",".txt",".zip")):
    suffix = file_name[file_name.rindex(".")+1:]
    match suffix:
        case "gif" | "png":
            print("image/" + suffix)

        case "jpg" | "jpeg":
            print("image/jpeg")

        case "pdf" | "zip":
            print("application/" + suffix)

        case "txt":
            print("text/plain")
else:
    print("application/octet-stream")