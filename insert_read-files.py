import glob, pprint, csv


''' Expecting the following format in the mapping_file
18-11-0 ROS_KHP_18_11Population_S27_R2_001.fastq,ROS_KHP_18_11Population_S27_R1_001.fastq
18-3-0 ROS_KHP_18_3Population_S29_R2_001.fastq,ROS_KHP_18_3Population_S29_R1_001.fastq
16-28-1 ROS_KHP_16-28_CLONE_S54_L007_R2_001.fastq,ROS_KHP_16-28_CLONE_S54_L007_R1_001.fastq
'''


mapping_file = glob.glob("*.txt")[0]
with open(mapping_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=' ')
    mapping_dict = {row[0]:row[1] for row in csv_reader}



metadata_file_list = glob.glob("*.csv")
for metadata_file_name in metadata_file_list:
    with open(metadata_file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        metadata_dict = {row[0]:row[1] for row in csv_reader}
#        pprint.pprint(metadata_dict)
    for key, read_file_str in mapping_dict.items():
        l = key.split('-')
        if l[0]==metadata_dict["ALE-number"] and l[1]==metadata_dict["Flask-number"] and l[2]==metadata_dict["Isolate-number"]:
            with open(metadata_file_name, 'a') as out_file:
                out_file.write("\n")
                out_file.write('"read-files","'+str(read_file_str)+'"')
