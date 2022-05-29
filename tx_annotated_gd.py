import glob
import subprocess


ssh_private_key_path = "/home/pphaneuf/.ssh/id_rsa"
remote_root_path = "/data2/aledata/fps/breseq/"
relative_gd_file_path_list = glob.glob("**/annotated.gd", recursive=True)
for relative_gd_file_path in relative_gd_file_path_list:
    if "evidence" not in relative_gd_file_path:
        remote_relative_gd_fie_path = relative_gd_file_path[:relative_gd_file_path.rfind('/')]
        remote_path = remote_root_path+remote_relative_gd_fie_path+'/'
        cmd_str = "scp "+relative_gd_file_path+" pphaneuf@ale-analytics.ucsd.edu:"+remote_path
        # print(cmd_str)
        subprocess.call(cmd_str, shell=True)
