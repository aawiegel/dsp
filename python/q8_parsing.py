# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv

def read_data(filename):
    
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        premier_list = [record for record in reader]
        
    return premier_list

def get_index_score_diff(goals):
    
    i = 1
    old_diff = 100000000
    for records in goals[1:]:
        diff = abs(int(records[5]) - int(records[6]))
        if diff < old_diff:
            index = i
            old_diff = diff
        i += 1
    
    return index

def get_team(index_value, parsed_data):
    
    return parsed_data[index_value][0]

footballTable = read_data('football.csv')
minRow = get_index_score_diff(footballTable)
print(str(get_team(minRow, footballTable)))