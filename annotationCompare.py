'''
This script compares two sets of manual annotations in a single data file and
flags those records where the annotations were different.
'''
import csv

annotationFile = 'Calibration.csv'

with open(annotationFile, mode= 'r') as file:
    csvFile = csv.reader(file)
    data = list(csvFile)

index = 0
for record in data:
    if record[7] != record[9]:
        data[index].append('diff')
    index += 1

with open(annotationFile, mode= 'w', newline= '') as file:
    writer = csv.writer(file)
    writer.writerows(data)