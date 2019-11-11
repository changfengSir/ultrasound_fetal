import os
import csv

# path = ''
filenames = os.listdir('./')
new_file = []
for name in filenames:
    if not 'Annotation' in name:
        new_file.append(name)

with open('file.csv','w',newline='') as f:
    csvfile = csv.writer(f)
    for i in new_file:
        csvfile.writerow([i])


print(new_file)