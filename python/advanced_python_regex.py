from collections import defaultdict
import csv
import re
import pprint as pp

with open('faculty.csv', 'r') as reader:
    reader = csv.reader(reader)
    faculty = [record for record in reader]

degrees_list = []
titles_list = []
email_list = []
for record in faculty[1:]:
    degree = re.sub('^ |\.', '', record[1])
    degrees = degree.split(' ')
    for degree in degrees:
        degrees_list.append(degree)
    title = re.sub(' is ', ' of ', record[2])
    titles_list.append(title)
    email_list.append(record[3])
    

    
degree_count = defaultdict(int)
title_count = defaultdict(int)
domain_count = defaultdict(int)

for degree in degrees_list:
    degree_count[degree] += 1
    
pp.pprint(degree_count, width = 2)

for title in titles_list:
    title_count[title] += 1

for email in email_list:
    domain_count[email.split('@')[1]] += 1
    
    
pp.pprint(title_count, width = 2)

pp.pprint(email_list)

pp.pprint(domain_count, width = 2)