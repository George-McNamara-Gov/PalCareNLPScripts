'''
This script adds keyword search flags to a data file given a particular list of
keywords. It was previously used to record keyword combinations.
'''

import csv

dataFile = 'inputs/tblEDIS_ALL_Jul2015toJul2022.csv'

#Chnage me to change which search terms come in.
searchFile = 'inputs/FinalSearchTerms.csv'

#Change me to change the name of the output file.
outFile = 'KeywordFlagged.csv'

with open(dataFile, mode= 'r') as file:
    csvFile = csv.reader(file)
    data = list(csvFile)

with open(searchFile, mode= 'r') as file:
    searchTermFile = csv.reader(file)
    searchList = list(searchTermFile)

def contains(term, s):
    s = s.upper()
    index = s.find(term.upper())
    if index == -1:
        return False
    else:
        return True

def containsTerms(string):
    check = False
    for term in searchList:
        if contains(term[0], string):
            check = True        
    return check

def identified(record):
    check1 = containsTerms(record[13])
    check2 = containsTerms(record[14])
    return check1 or check2

count = 0
index = 0
termSets = []
counts = []
for record in data:
    id = identified(record)
    if id:
        data[index].append('1')
        count += 1
    else:
        data[index].append('0')
    index += 1

with open(outFile, mode= 'w', newline= '') as file:
    writer = csv.writer(file)
    writer.writerows(data)