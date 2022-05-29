import glob, json

afterqc_json_list = glob.glob("*.json")
print("R1\tR2\tgood_reads\tbad_reads")
for afterqc_json_file in afterqc_json_list:
    # print(afterqc_json_file)
    with open(afterqc_json_file, 'r') as f:
        afterqc_data = json.load(f)
    out_str = afterqc_data['command']['read1_file']
    out_str += '\t'+str(afterqc_data['command']['read2_file'])
    out_str += '\t'+str(afterqc_data['afterqc_main_summary']['good_reads'])
    out_str += '\t'+str(afterqc_data['afterqc_main_summary']['bad_reads'])
    print(out_str)