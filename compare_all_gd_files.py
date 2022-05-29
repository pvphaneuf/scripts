__author__ = 'pphaneuf'


from os import listdir
from os.path import isfile, join, splitext
import subprocess


file_names = [f for f in listdir(".") if isfile(join(".", f))]

gd_file_names = []

for file_name in file_names:

    name, extension = splitext(file_name)

    if extension == ".gd":
        gd_file_names.append(file_name)

partial_cmd_str = 'gdtools COMPARE -r NC_000913_3.gb '

cmds_to_execute = []

for gd_file_name in gd_file_names:

    cmds_to_execute.append(partial_cmd_str + gd_file_name)

print(cmds_to_execute)

# for cmd in cmds_to_execute:
#
#     subprocess.call(cmd, shell=True)
