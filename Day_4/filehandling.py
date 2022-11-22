import csv

# open the file
with open(r"C:\Users\P.Purushothaman\OneDrive - Shell\EUC_Solution_Automation\Dev++\Learn\Python\Training\Day_4\Book1.csv") as csv_file:
    csvFile = csv.reader(csv_file)
    for lines in csvFile:
        print(lines)
