#! /usr/bin/python3

import pandas as pd

# Load the CSV data into a DataFrame
data = pd.read_csv('data.csv')

# Let's assume you want to find the average of a column named "Score"
average_value = data['Score'].mean()

print(f"The average Score of the  column is: {average_value:.2f}")




print("###############################################################################################")


import csv

values = []

# Open the CSV file
with open('data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        # Assuming the column name is Score
        value = float(row['Score'])
        values.append(value)

average_value = sum(values) / len(values)

print(f"The average value Score of the students is: {average_value:.2f}")

