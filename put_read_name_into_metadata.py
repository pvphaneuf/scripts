import os
from pprint import pprint


def index_containing_substring(the_list, substring):
    for i, s in enumerate(the_list):
        if substring in s:
              return i
    return -1


log_list = []
dir_list = os.listdir('.')
for dir_name in dir_list:
    if os.path.isdir(dir_name):
        log_file_path = dir_name+"/output/log.txt"
        with open(log_file_path, 'r') as log_file:
            log_list.append(log_file.read())
breseq_read_list_dict = {}
for log_str in log_list:
    log_item_list = log_str.split()
    read_file_list_start_index = index_containing_substring(log_item_list, ".fq")
    read_list = log_item_list[read_file_list_start_index:]
    breseq_dir_name = log_item_list[log_item_list.index("-o")+1]
    breseq_read_list_dict[breseq_dir_name] = read_list
pprint(breseq_read_list_dict)


import csv
afir_breseq_mapping_list = []
with open("mapping.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        afir_breseq_mapping_list.append({"breseq_dir_name":row[1], "ALE-number":row[4], "Flask-number":row[5], "Isolate-number":row[6], "technical-replicate-number":row[7]})
# print(afir_breseq_mapping_list)


dir_list = os.listdir('.')
for file_name in dir_list:
    if ".CSV" in file_name:
        with open(file_name) as metadata_csv_file:
            csv_reader = csv.reader(metadata_csv_file)
            metadata_dict = {rows[0]:rows[1] for rows in csv_reader}
        for mapping_dict in afir_breseq_mapping_list:
            if metadata_dict["ALE-number"]==mapping_dict["ALE-number"] and metadata_dict["Flask-number"]==mapping_dict["Flask-number"] and metadata_dict["Isolate-number"]==mapping_dict["Isolate-number"] and metadata_dict["technical-replicate-number"]==mapping_dict["technical-replicate-number"]:
                breseq_dir_name = mapping_dict["breseq_dir_name"]
                # print('read-files,"'+'.'.join(breseq_read_list_dict[breseq_dir_name]))
                print(breseq_read_list_dict[breseq_dir_name])
                # with open(file_name, "a") as metadata_file:
                    # metadata_file.write('read-files,"'+)
