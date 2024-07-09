import sys,csv

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
else:
    try:
        with open(sys.argv[1],"r") as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            # for row in reader:
            #     firstname, lastname = row["name"].strip().split(", ")
            #     writer.writerow({"first":f" {firstname}", "last":lastname, "house":row["house"]})
        processed = []
        for row in rows:
            firstname, lastname = row["name"].strip().split(", ")
            processed.append({"first":lastname, "last":firstname, "house":row["house"]}) # This is so tricky.
        with open(sys.argv[2],"w") as file:
            writer = csv.DictWriter(file, fieldnames = processed[0])
            writer.writeheader()
            writer.writerows(processed)
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
