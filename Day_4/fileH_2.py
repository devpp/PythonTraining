import csv

# open the file
with open(
        r"C:\Users\P.Purushothaman\OneDrive - Shell\EUC_Solution_Automation\Dev++\Learn\Python\Training\Day_4\Book1.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1

    print(f'Processed {line_count} lines. ')

    # open the file
