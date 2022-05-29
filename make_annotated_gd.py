import os
import subprocess
dir_list = os.listdir('.')
ignore_l = [".py", ".gbk", "dups", ".gb", ".csv"]
for dir_name in dir_list:
    if ".py" not in dir_name \
            and ".gbk" not in dir_name \
            and ".gb" not in dir_name \
            and "dups" not in dir_name \
            and ".csv" not in dir_name:
        sample_dir_path = os.path.abspath('.')+"/"+dir_name+'/output/'
        output_gd_file_path = sample_dir_path+"output.gd"
        annotated_gd_file_path = sample_dir_path+"annotated.gd"
        cmd_str = "gdtools annotate -f GD -r bop27_1_4.gb"
        cmd_str += " -o "+annotated_gd_file_path
        cmd_str += " "+output_gd_file_path
        subprocess.call(cmd_str, shell=True)
