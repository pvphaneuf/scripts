import glob, csv, os, shutil
exp_metadata_dict = {}
for csv_file_name in glob.glob("*.csv"):
    sample_metadata_dict = {}
    with open(csv_file_name) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            sample_metadata_dict[row[0]]=row[1]
    exp_metadata_dict[csv_file_name] = sample_metadata_dict

isolate_type_list = []
for sample_metadata_dict in exp_metadata_dict.values():
    isolate_type_list.append(sample_metadata_dict["isolate-type"])
isolate_type_set = set(isolate_type_list)
for isolate_type in isolate_type_set:
    if not os.path.exists(isolate_type):
        os.makedirs(isolate_type)

for csv_file_name, sample_metadata_dict in exp_metadata_dict.items():
    move_file_list = sample_metadata_dict["read-files"].split(',')
    move_file_list.append(csv_file_name)
    for move_file in move_file_list:
        move_dir_str = sample_metadata_dict["isolate-type"]
        shutil.move(move_file, move_dir_str+"/"+move_file)
