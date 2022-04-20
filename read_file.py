import csv
import pandas as pd

with open("innovators.csv", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'{", ".join(row)}')
            line_count += 1
        print(f'{row["SN"]}, {row["Name"]}, {row["Contribution"]}.')
        
      