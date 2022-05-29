import os, subprocess, glob, shutil, csv


GDTOOLS_PATH = "~/breseq/breseq-0.31.0-Linux-x86_64/bin/gdtools"


# Rename breseq output dirs to AFIR number.
metadata_file_list = glob.glob("*.csv")
metadata_file_list += glob.glob("*.CSV")
metadata_dict = {}
for metadata_file_name in metadata_file_list:
    with open(metadata_file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        raw_sample_metadata_dict = {rows[0]:rows[1] for rows in csv_reader}
        read_file_list = raw_sample_metadata_dict["read-files"].split(',')
        read_file_name = read_file_list[0]
        raw_sample_name = read_file_name[:read_file_name.find("_S")]
        metadata_dict[raw_sample_name] = raw_sample_metadata_dict

for obj_name in os.listdir('.'):
    if os.path.isdir(obj_name) and obj_name in metadata_dict:
        new_name = \
            metadata_dict[obj_name]["ALE-number"] \
            +'-'+metadata_dict[obj_name]["Flask-number"] \
            +'-'+metadata_dict[obj_name]["Isolate-number"] \
            +'-'+metadata_dict[obj_name]["technical-replicate-number"]
        os.rename(obj_name, new_name)

'''
# Could successfully import duplication.genes.get_genes through
# python imports, therefore executing it through shell command.
cmd_str = "python3 ~/git/duplication/main.py ./"
subprocess.call(cmd_str, shell=True)
'''


# Build the annotated files per breseq report.

# Get reference file list
ref_file_list = glob.glob("*.gff3")
ref_file_list += glob.glob("*.gbk")
ref_file_list += glob.glob("*.gb")

dir_list = os.listdir('.')
for dir_name in dir_list:
    if os.path.isdir(dir_name):
        sample_dir_path = os.path.abspath('.')+"/"+dir_name+'/output/'
        output_gd_file_path = sample_dir_path+"output.gd"
        annotated_gd_file_path = sample_dir_path+"annotated.gd"
        cmd_str = GDTOOLS_PATH
        cmd_str += " annotate -f GD"
        for ref_file_name in ref_file_list:
           cmd_str += " -r " + ref_file_name
        cmd_str += " -o "+annotated_gd_file_path
        cmd_str += " "+output_gd_file_path
        # print(cmd_str)
        subprocess.call(cmd_str, shell=True)


# Remove intermediate breseq processing directories
dir_to_remove_list = ["01_sequence_conversion", \
    "02_reference_alignment", \
    "03_candidate_junctions", \
    "04_candidate_junction_alignment", \
    "05_alignment_correction", \
    "06_bam", \
    "07_error_calibration", \
    "08_mutation_identification", \
    "09_copy_number_variation"]

file_list = os.listdir('.')
for file_name in file_list:
    for dir_to_remove in dir_to_remove_list:
        if os.path.isdir(file_name+'/'+dir_to_remove):
            print("REMOVED:", file_name+'/'+dir_to_remove)
            shutil.rmtree(file_name+'/'+dir_to_remove)
