import pandas as pd
import csv
import os
import pytest


# Remove CSV file
os.system("rm innovators.csv")

# Data Frame Module
print('Data Frame Module')
data = [['Tom', 'Jack', 'Steve', 'Ricky'], [28, 34, 29, 42]]
df = pd.DataFrame(data, columns=['Soldier', 'Pilot', 'Engineer', 'Doctor'], index=[
                  'Name', 'Age'])
print(df)

# Write CSV file
print('\nWrite CSV file')
print('CSV file write Successful\n')
with open('innovators.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(data[0])
    writer.writerow(data[1])
    print('Read CSV file')

 # Read CSV file
with open("innovators.csv", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'{", ".join(row)}')

# Assertions
#  assert column names
def test_column_name():
    column_list = list(df)
    expected_list = ['Soldier', 'Pilot', 'Engineer', 'Doctor']
    assert column_list == expected_list

# assert row names
def test_row_name():
    row_list_name = df.index.values[0]
    row_list_age = df.index.values[0]
    assert row_list_name == 'Name'
    assert row_list_age == 'Age'
