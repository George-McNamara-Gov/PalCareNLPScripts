'''
This script replaces common names in TriageDescription and TriageObject text 
fields.
'''
import csv

#A .csv file containing a EDIS records.
calibrationFile = ''

#A .csv file containing a list of names.
nameListFile = ''

#The name for the file generated by this script.
nameReplacedCalibrationFile = ''

#The name which will replace any name from the list of names.
replacementName = 'Glenn'

#TODO: Import calibration file and store as a list of lists called data.

data = []

#TODO: Import nameListFile and store as a list of strings called names.

names = []

#TODO: Write a function which replaces any substring from names in the 
#TraigeObject or TriageDescription fields with replacementName.
def replaceNames(record : list):
    pass

newData = [replaceNames(record) for record in data]

with open(nameReplacedCalibrationFile, mode= 'w', newline= '') as file:
    writer = csv.writer(file)
    writer.writerows(newData)