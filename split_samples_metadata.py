import glob, csv, os, shutil

project_file_dict = {}

metadata_file_list = glob.glob("*.csv")
for metadata_file_name in metadata_file_list:
	with open(metadata_file_name) as metadata_file:
		csv_reader = csv.reader(metadata_file)
		project = ""
		read_file_list_str = ""
		for row in csv_reader:
			if row[0] == "isolate-type": project = row[1]
			if row[0] == "read-files": read_file_list_str = row[1]

	file_list_to_insert = []
	for file_name in read_file_list_str.split(','):
		file_prefix = file_name[:file_name.find('.')]
		file_list_to_insert.append(file_prefix)

	file_list_to_insert.append(metadata_file_name)
	if project in project_file_dict.keys():
		project_file_dict[project] += (file_list_to_insert)
	else:
		project_file_dict[project] = file_list_to_insert

for proj_name, file_list in project_file_dict.items():
	if not os.path.exists(proj_name):
		os.makedirs(proj_name)
	for file_name in file_list:
		if ".csv" in file_name: shutil.move(file_name, proj_name+'/'+file_name)
		else: shutil.move(file_name+'.good.fq', proj_name+'/')
