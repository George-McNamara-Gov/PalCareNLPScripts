import csv

dataFile = 'outputs/Calibration.csv'

searchFile = 'inputs/FinalSearchTerms.csv'

with open(dataFile, mode= 'r') as file:
    csvFile = csv.reader(file)
    data = list(csvFile)

with open(searchFile, mode= 'r') as file:
    searchTermFile = csv.reader(file)
    searchList = list(searchTermFile)

searchList.remove(['nursing home'])

def isTruePos(r):
    '''
    r : list
    A list containing one row from the csv.
    '''
    #taking list of lists as input, index at x element of list
    check = False
    if r[9] != '0':
        check = True
    return check

def contains(term, s):
    s = s.upper()
    index = s.find(term.upper())
    if index == -1:
        return False
    else:
        return True

def containsNurseOnly(r):
    '''
    r : list
    A list containing one row from the csv.
    '''
    check = False
    if contains('nursing home', r[4]) or contains('nursing home', r[5]):
        check = True
    for term in searchList:
        if contains(term[0], r[4]) or contains(term[0], r[5]):
            check = False
    return check

count = 0
index = 1
for record in data:
    if containsNurseOnly(record) and isTruePos(record):
        print(index)
        count += 1
    index += 1

print(count)