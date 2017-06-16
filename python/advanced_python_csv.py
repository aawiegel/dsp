import csv

with open('faculty.csv', 'r') as reader:
    reader = csv.reader(reader)
    faculty = [record for record in reader]
    
for record in faculty[1:]:
    email_list.append(record[3])

with open('emails.csv', 'w', newline='') as email_file:
    writer = csv.writer(email_file, delimiter=',')
    for email in email_list:
        writer.writerow([email])