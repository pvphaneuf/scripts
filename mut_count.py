import os

dir_list = os.listdir('.')
for dir_name in dir_list:
    sample_dir_path = os.path.abspath('.')+'/'+dir_name+'/output/'
    annotated_gd_file_path = sample_dir_path+"annotated.gd"
    if os.path.isfile(annotated_gd_file_path):
        mut_count = 0
        with open(annotated_gd_file_path) as f:
            for line in f:
                line_list = str(line).strip().split('\t')
                if line_list[0] == 'SNP' \
                    or line_list[0] == 'SUB' \
                    or line_list[0] == 'DEL' \
                    or line_list[0] == 'INS' \
                    or line_list[0] == 'MOB' \
                    or line_list[0] == 'AMP' \
                    or line_list[0] == 'CON' \
                    or line_list[0] == 'INV':
                    mut_count += 1
        print(sample_dir_path, mut_count)
