import os
import shutil


dir_to_remote_list = ["01_sequence_conversion", \
    "02_reference_alignment", \
    "03_candidate_junctions", \
    "04_candidate_junction_alignment", \
    "05_alignment_correction", \
    "06_bam", \
    "07_error_calibration", \
    "08_mutation_identification"]


file_list = os.listdir('.')
for file_name in file_list:
    for dir_to_remove in dir_to_remote_list:
        if os.path.isdir(file_name+'/'+dir_to_remove):
            print("REMOVED:", file_name+'/'+dir_to_remove)
            shutil.rmtree(file_name+'/'+dir_to_remove)
