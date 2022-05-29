import csv
import os

# expecting the first cell to descrine the current name; remaining cells describe AFIR serial number.
with open('mapping.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        curr_sample_dir_name = row[0]
        if os.path.isdir("./"+curr_sample_dir_name):
            new_name = row[1]+'-'+row[2]+'-'+row[3]+'-'+row[4]
            os.rename(curr_sample_dir_name, new_name)
