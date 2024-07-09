import sys
import csv
from tabulate import tabulate
table = []

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
else:
    if(sys.argv[1][-4:] != ".csv"):
        sys.exit("Not a CSV file")
    try:
        with open(sys.argv[1],"r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if(sys.argv[1] == "regular.csv"):
                    headers = ['Regular Pizza','Small','Large']
                    table.append([row["Regular Pizza"],row["Small"],row["Large"]])
                elif(sys.argv[1] == "sicilian.csv"):
                    headers = ['Sicilian Pizza','Small','Large']
                    table.append([row["Sicilian Pizza"],row["Small"],row["Large"]])

        print(tabulate(table,headers,"grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")
